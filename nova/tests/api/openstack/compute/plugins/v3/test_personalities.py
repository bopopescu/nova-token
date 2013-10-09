begin_unit
comment|'# Copyright 2013 IBM Corp.'
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
name|'datetime'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
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
name|'plugins'
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
name|'servers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'manager'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'rpc'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
name|'import'
name|'matchers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
name|'fakes'
op|'.'
name|'FAKE_UUID'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_gen_uuid
name|'def'
name|'fake_gen_uuid'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'FAKE_UUID'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|return_security_group
dedent|''
name|'def'
name|'return_security_group'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ServersControllerCreateTest
dedent|''
name|'class'
name|'ServersControllerCreateTest'
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
string|'"""Shared implementation for tests below that create instance."""'
newline|'\n'
name|'super'
op|'('
name|'ServersControllerCreateTest'
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
name|'flags'
op|'('
name|'verbose'
op|'='
name|'True'
op|','
nl|'\n'
name|'enable_instance_password'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'ext_info'
op|'='
name|'plugins'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'servers'
op|'.'
name|'ServersController'
op|'('
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'set_override'
op|'('
string|"'extensions_blacklist'"
op|','
string|"'os-personality'"
op|','
nl|'\n'
string|"'osapi_v3'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'no_personality_controller'
op|'='
name|'servers'
op|'.'
name|'ServersController'
op|'('
nl|'\n'
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
nl|'\n'
DECL|function|instance_create
name|'def'
name|'instance_create'
op|'('
name|'context'
op|','
name|'inst'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst_type'
op|'='
name|'flavors'
op|'.'
name|'get_flavor_by_flavor_id'
op|'('
number|'3'
op|')'
newline|'\n'
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'def_image_ref'
op|'='
string|"'http://localhost/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_num'
op|'+='
number|'1'
newline|'\n'
name|'instance'
op|'='
name|'fake_instance'
op|'.'
name|'fake_db_instance'
op|'('
op|'**'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'self'
op|'.'
name|'instance_cache_num'
op|','
nl|'\n'
string|"'display_name'"
op|':'
name|'inst'
op|'['
string|"'display_name'"
op|']'
name|'or'
string|"'test'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'FAKE_UUID'
op|','
nl|'\n'
string|"'instance_type'"
op|':'
name|'dict'
op|'('
name|'inst_type'
op|')'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
string|"'1.2.3.4'"
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
string|"'fead::1234'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'inst'
op|'.'
name|'get'
op|'('
string|"'image_ref'"
op|','
name|'def_image_ref'
op|')'
op|','
nl|'\n'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'reservation_id'"
op|':'
name|'inst'
op|'['
string|"'reservation_id'"
op|']'
op|','
nl|'\n'
string|'"created_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'10'
op|','
number|'12'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'11'
op|','
number|'11'
op|','
number|'11'
op|','
number|'0'
op|','
number|'0'
op|')'
op|','
nl|'\n'
string|'"config_drive"'
op|':'
name|'None'
op|','
nl|'\n'
string|'"progress"'
op|':'
number|'0'
op|','
nl|'\n'
string|'"fixed_ips"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|'"task_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"vm_state"'
op|':'
string|'""'
op|','
nl|'\n'
string|'"security_groups"'
op|':'
name|'inst'
op|'['
string|"'security_groups'"
op|']'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'['
name|'instance'
op|'['
string|"'id'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|']'
op|'='
name|'instance'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|instance_get
dedent|''
name|'def'
name|'instance_get'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Stub for compute/api create() pulling in instance after\n            scheduling\n            """'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'instance_cache_by_id'
op|'['
name|'instance_id'
op|']'
newline|'\n'
nl|'\n'
DECL|function|instance_update
dedent|''
name|'def'
name|'instance_update'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'values'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'uuid'
op|']'
newline|'\n'
name|'instance'
op|'.'
name|'update'
op|'('
name|'values'
op|')'
newline|'\n'
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
DECL|function|server_update
dedent|''
name|'def'
name|'server_update'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|','
name|'params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst'
op|'='
name|'self'
op|'.'
name|'instance_cache_by_uuid'
op|'['
name|'instance_uuid'
op|']'
newline|'\n'
name|'inst'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'return'
op|'('
name|'inst'
op|','
name|'inst'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_method
dedent|''
name|'def'
name|'fake_method'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|project_get_networks
dedent|''
name|'def'
name|'project_get_networks'
op|'('
name|'context'
op|','
name|'user_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'dict'
op|'('
name|'id'
op|'='
string|"'1'"
op|','
name|'host'
op|'='
string|"'localhost'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|queue_get_for
dedent|''
name|'def'
name|'queue_get_for'
op|'('
name|'context'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'network_topic'"
newline|'\n'
nl|'\n'
dedent|''
name|'fakes'
op|'.'
name|'stub_out_rate_limiting'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_key_pair_funcs'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
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
name|'uuid'
op|','
string|"'uuid4'"
op|','
name|'fake_gen_uuid'
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
string|"'instance_add_security_group'"
op|','
nl|'\n'
name|'return_security_group'
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
string|"'project_get_networks'"
op|','
nl|'\n'
name|'project_get_networks'
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
string|"'instance_create'"
op|','
name|'instance_create'
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
string|"'instance_system_metadata_update'"
op|','
nl|'\n'
name|'fake_method'
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
string|"'instance_get'"
op|','
name|'instance_get'
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
string|"'instance_update'"
op|','
name|'instance_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'cast'"
op|','
name|'fake_method'
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
string|"'instance_update_and_get_original'"
op|','
nl|'\n'
name|'server_update'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'rpc'
op|','
string|"'queue_get_for'"
op|','
name|'queue_get_for'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'manager'
op|'.'
name|'VlanManager'
op|','
string|"'allocate_fixed_ip'"
op|','
nl|'\n'
name|'fake_method'
op|')'
newline|'\n'
nl|'\n'
name|'return_server'
op|'='
name|'fakes'
op|'.'
name|'fake_instance_get'
op|'('
op|')'
newline|'\n'
name|'return_servers'
op|'='
name|'fakes'
op|'.'
name|'fake_instance_get_all_by_filters'
op|'('
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
string|"'instance_get_all_by_filters'"
op|','
nl|'\n'
name|'return_servers'
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
string|"'instance_get_by_uuid'"
op|','
nl|'\n'
name|'return_server'
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
string|"'instance_add_security_group'"
op|','
nl|'\n'
name|'return_security_group'
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
string|"'instance_update_and_get_original'"
op|','
nl|'\n'
name|'instance_update'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_create_extra
dedent|''
name|'def'
name|'_test_create_extra'
op|'('
name|'self'
op|','
name|'params'
op|','
name|'no_image'
op|'='
name|'False'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'c905cedb-7281-47e4-8a62-f26bc5fc4c77'"
newline|'\n'
name|'server'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|"'server_test'"
op|','
name|'image_ref'
op|'='
name|'image_uuid'
op|','
name|'flavor_ref'
op|'='
number|'2'
op|')'
newline|'\n'
name|'if'
name|'no_image'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'.'
name|'pop'
op|'('
string|"'image_ref'"
op|','
name|'None'
op|')'
newline|'\n'
dedent|''
name|'server'
op|'.'
name|'update'
op|'('
name|'params'
op|')'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'server'
op|'='
name|'server'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers'"
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
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'if'
name|'override_controller'
op|':'
newline|'\n'
indent|'            '
name|'server'
op|'='
name|'override_controller'
op|'.'
name|'create'
op|'('
name|'req'
op|','
name|'body'
op|')'
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'server'
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
op|'.'
name|'obj'
op|'['
string|"'server'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_personality_disabled
dedent|''
dedent|''
name|'def'
name|'test_create_instance_with_personality_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
nl|'\n'
string|"'personality'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
op|','
nl|'\n'
string|'"contents"'
op|':'
string|'"MQ=="'
op|','
nl|'\n'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'injected_files'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
name|'params'
op|','
nl|'\n'
name|'override_controller'
op|'='
name|'self'
op|'.'
name|'no_personality_controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_personality_enabled
dedent|''
name|'def'
name|'test_create_instance_with_personality_enabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
op|'{'
nl|'\n'
string|"'personality'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
op|','
nl|'\n'
string|'"contents"'
op|':'
string|'"MQ=="'
op|','
nl|'\n'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'injected_files'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_create_extra'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_with_personality
dedent|''
name|'def'
name|'test_create_instance_with_personality'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_href'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/flavors/3'"
newline|'\n'
name|'value'
op|'='
string|'"A random string"'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'user_data_test'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'flavor_ref'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'personality'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
op|','
nl|'\n'
string|'"contents"'
op|':'
string|'"MQ=="'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'old_create'
op|'='
name|'compute_api'
op|'.'
name|'API'
op|'.'
name|'create'
newline|'\n'
nl|'\n'
DECL|function|create
name|'def'
name|'create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'injected_files'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'old_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'create'"
op|','
name|'create'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
string|"'/servers'"
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
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
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
op|'.'
name|'obj'
newline|'\n'
nl|'\n'
name|'server'
op|'='
name|'res'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'FAKE_UUID'
op|','
name|'server'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_instance_with_personality_disabled
dedent|''
name|'def'
name|'test_rebuild_instance_with_personality_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'image_href'
op|'='
string|"'http://localhost/v3/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'access_ipv4'
op|'='
string|"'0.0.0.0'"
newline|'\n'
name|'access_ipv6'
op|'='
string|"'fead::1234'"
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'rebuild'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'new_name'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
name|'access_ipv4'
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
name|'access_ipv6'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'personality'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
op|','
nl|'\n'
string|'"contents"'
op|':'
string|'"MQ=="'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'rebuild_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|function|rebuild
name|'def'
name|'rebuild'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'files_to_inject'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rebuild_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'rebuild'"
op|','
name|'rebuild'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/servers/%s/action'"
op|'%'
name|'FAKE_UUID'
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
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'no_personality_controller'
op|'.'
name|'_action_rebuild'
op|'('
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|')'
op|'.'
name|'obj'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'rebuild_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_instance_with_personality
dedent|''
name|'def'
name|'test_rebuild_instance_with_personality'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'image_href'
op|'='
string|"'http://localhost/v3/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'access_ipv4'
op|'='
string|"'0.0.0.0'"
newline|'\n'
name|'access_ipv6'
op|'='
string|"'fead::1234'"
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'rebuild'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'new_name'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
name|'access_ipv4'
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
name|'access_ipv6'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'personality'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
op|','
nl|'\n'
string|'"contents"'
op|':'
string|'"MQ=="'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'rebuild_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|rebuild
name|'def'
name|'rebuild'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'files_to_inject'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
op|'('
string|"'/etc/banner.txt'"
op|','
string|"'MQ=='"
op|')'
op|','
nl|'\n'
name|'kwargs'
op|'['
string|"'files_to_inject'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rebuild_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'rebuild'"
op|','
name|'rebuild'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/servers/%s/action'"
op|'%'
name|'FAKE_UUID'
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
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_action_rebuild'
op|'('
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|')'
op|'.'
name|'obj'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'rebuild_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_bad_personality
dedent|''
name|'def'
name|'test_rebuild_bad_personality'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'image_href'
op|'='
string|"'http://localhost/v3/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|'"rebuild"'
op|':'
op|'{'
nl|'\n'
string|'"image_ref"'
op|':'
name|'image_href'
op|','
nl|'\n'
string|'"personality"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"path"'
op|':'
string|'"/path/to/file"'
op|','
nl|'\n'
string|'"contents"'
op|':'
string|'"INVALID b64"'
op|','
nl|'\n'
op|'}'
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/servers/%s/action'"
op|'%'
name|'FAKE_UUID'
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
name|'_action_rebuild'
op|','
nl|'\n'
name|'req'
op|','
name|'FAKE_UUID'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_instance_without_personality
dedent|''
name|'def'
name|'test_rebuild_instance_without_personality'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'image_href'
op|'='
string|"'http://localhost/v3/images/%s'"
op|'%'
name|'image_uuid'
newline|'\n'
name|'access_ipv4'
op|'='
string|"'0.0.0.0'"
newline|'\n'
name|'access_ipv6'
op|'='
string|"'fead::1234'"
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'rebuild'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'new_name'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_href'
op|','
nl|'\n'
string|"'access_ip_v4'"
op|':'
name|'access_ipv4'
op|','
nl|'\n'
string|"'access_ip_v6'"
op|':'
name|'access_ipv6'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'rebuild_called'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|function|rebuild
name|'def'
name|'rebuild'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertNotIn'
op|'('
string|"'files_to_inject'"
op|','
name|'kwargs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'rebuild_called'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'rebuild'"
op|','
name|'rebuild'
op|')'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/servers/%s/action'"
op|'%'
name|'FAKE_UUID'
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
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_action_rebuild'
op|'('
name|'req'
op|','
nl|'\n'
name|'FAKE_UUID'
op|','
nl|'\n'
name|'body'
op|')'
op|'.'
name|'obj'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'self'
op|'.'
name|'rebuild_called'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_instance_invalid_personality
dedent|''
name|'def'
name|'test_create_instance_invalid_personality'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_uuid'
op|'='
string|"'76fa36fc-c930-4bf3-8c8a-ea2a2420deb6'"
newline|'\n'
name|'flavor_ref'
op|'='
string|"'http://localhost/flavors/3'"
newline|'\n'
nl|'\n'
DECL|function|fake_create
name|'def'
name|'fake_create'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'codec'
op|'='
string|"'utf8'"
newline|'\n'
name|'content'
op|'='
string|"'b25zLiINCg0KLVJpY2hhcmQgQ$$%QQmFjaA=='"
newline|'\n'
name|'start_position'
op|'='
number|'19'
newline|'\n'
name|'end_position'
op|'='
number|'20'
newline|'\n'
name|'msg'
op|'='
string|"'invalid start byte'"
newline|'\n'
name|'raise'
name|'UnicodeDecodeError'
op|'('
name|'codec'
op|','
name|'content'
op|','
name|'start_position'
op|','
nl|'\n'
name|'end_position'
op|','
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'min_count'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'image_uuid'
op|','
nl|'\n'
string|"'flavor_ref'"
op|':'
name|'flavor_ref'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'hello'"
op|':'
string|"'world'"
op|','
nl|'\n'
string|"'open'"
op|':'
string|"'stack'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'personality'"
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
op|','
nl|'\n'
string|'"contents"'
op|':'
string|'"b25zLiINCg0KLVJpY2hhcmQgQ$$%QQmFjaA=="'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
nl|'\n'
string|"'create'"
op|','
nl|'\n'
name|'fake_create'
op|')'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequestV3'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/servers/%s/action'"
op|'%'
name|'FAKE_UUID'
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
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
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
name|'create'
op|','
name|'req'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestServerRebuildRequestXMLDeserializer
dedent|''
dedent|''
name|'class'
name|'TestServerRebuildRequestXMLDeserializer'
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
name|'TestServerRebuildRequestXMLDeserializer'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'ext_info'
op|'='
name|'plugins'
op|'.'
name|'LoadedExtensionInfo'
op|'('
op|')'
newline|'\n'
name|'controller'
op|'='
name|'servers'
op|'.'
name|'ServersController'
op|'('
name|'extension_info'
op|'='
name|'ext_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deserializer'
op|'='
name|'servers'
op|'.'
name|'ActionDeserializer'
op|'('
name|'controller'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'create_deserializer'
op|'='
name|'servers'
op|'.'
name|'CreateDeserializer'
op|'('
name|'controller'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rebuild_request_with_personality
dedent|''
name|'def'
name|'test_rebuild_request_with_personality'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serial_request'
op|'='
string|'"""\n    <rebuild\n        xmlns="http://docs.openstack.org/compute/api/v3"\n        name="foobar"\n        image_ref="1">\n        <metadata>\n            <meta key="My Server Name">Apache1</meta>\n        </metadata>\n        <personality>\n            <file path="/etc/banner.txt">MQ==</file>\n        </personality>\n    </rebuild>\n        """'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'serial_request'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"rebuild"'
op|':'
op|'{'
nl|'\n'
string|'"image_ref"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"foobar"'
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
nl|'\n'
string|'"My Server Name"'
op|':'
string|'"Apache1"'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"personality"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
op|','
nl|'\n'
string|'"contents"'
op|':'
string|'"MQ=="'
op|'}'
nl|'\n'
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'request'
op|'['
string|"'body'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_request_with_personality
dedent|''
name|'def'
name|'test_create_request_with_personality'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serial_request'
op|'='
string|'"""\n    <server  xmlns="http://docs.openstack.org/compute/api/v3"\n        image_ref="1"\n        flavor_ref="2"\n        name="new-server-test">\n        <metadata>\n           <meta key="My Server Name">Apache1</meta>\n        </metadata>\n        <personality>\n           <file path="/etc/banner.txt">MQ==</file>\n        </personality>\n    </server>\n        """'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'create_deserializer'
op|'.'
name|'deserialize'
op|'('
name|'serial_request'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'{'
nl|'\n'
string|'"flavor_ref"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"image_ref"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
nl|'\n'
string|'"My Server Name"'
op|':'
string|'"Apache1"'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"name"'
op|':'
string|'"new-server-test"'
op|','
nl|'\n'
string|'"personality"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"contents"'
op|':'
string|'"MQ=="'
op|','
nl|'\n'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
nl|'\n'
op|'}'
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'request'
op|'['
string|"'body'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_empty_metadata_personality
dedent|''
name|'def'
name|'test_empty_metadata_personality'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serial_request'
op|'='
string|'"""\n<server xmlns="http://docs.openstack.org/compute/api/v2"\n        name="new-server-test"\n        image_ref="1"\n        flavor_ref="2">\n    <metadata/>\n    <personality/>\n</server>"""'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'create_deserializer'
op|'.'
name|'deserialize'
op|'('
name|'serial_request'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'{'
nl|'\n'
string|'"name"'
op|':'
string|'"new-server-test"'
op|','
nl|'\n'
string|'"image_ref"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"flavor_ref"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|'"personality"'
op|':'
op|'['
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'request'
op|'['
string|"'body'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|function|test_multiple_personality_files
dedent|''
name|'def'
name|'test_multiple_personality_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serial_request'
op|'='
string|'"""\n<server xmlns="http://docs.openstack.org/compute/api/v2"\n        name="new-server-test"\n        image_ref="1"\n        flavor_ref="2">\n    <personality>\n        <file path="/etc/banner.txt">MQ==</file>\n        <file path="/etc/hosts">Mg==</file>\n    </personality>\n</server>"""'
newline|'\n'
name|'request'
op|'='
name|'self'
op|'.'
name|'create_deserializer'
op|'.'
name|'deserialize'
op|'('
name|'serial_request'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|'"server"'
op|':'
op|'{'
nl|'\n'
string|'"name"'
op|':'
string|'"new-server-test"'
op|','
nl|'\n'
string|'"image_ref"'
op|':'
string|'"1"'
op|','
nl|'\n'
string|'"flavor_ref"'
op|':'
string|'"2"'
op|','
nl|'\n'
string|'"personality"'
op|':'
op|'['
nl|'\n'
op|'{'
string|'"path"'
op|':'
string|'"/etc/banner.txt"'
op|','
string|'"contents"'
op|':'
string|'"MQ=="'
op|'}'
op|','
nl|'\n'
op|'{'
string|'"path"'
op|':'
string|'"/etc/hosts"'
op|','
string|'"contents"'
op|':'
string|'"Mg=="'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertThat'
op|'('
name|'request'
op|'['
string|"'body'"
op|']'
op|','
name|'matchers'
op|'.'
name|'DictMatches'
op|'('
name|'expected'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
