begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
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
name|'datetime'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
name|'import'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
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
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|MANUAL_INSTANCE_UUID
name|'MANUAL_INSTANCE_UUID'
op|'='
name|'fakes'
op|'.'
name|'FAKE_UUID'
newline|'\n'
DECL|variable|AUTO_INSTANCE_UUID
name|'AUTO_INSTANCE_UUID'
op|'='
name|'fakes'
op|'.'
name|'FAKE_UUID'
op|'.'
name|'replace'
op|'('
string|"'a'"
op|','
string|"'b'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|stub_instance
name|'stub_instance'
op|'='
name|'fakes'
op|'.'
name|'stub_instance'
newline|'\n'
nl|'\n'
DECL|variable|API_DISK_CONFIG
name|'API_DISK_CONFIG'
op|'='
string|"'OS-DCF:diskConfig'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|instance_addresses
name|'def'
name|'instance_addresses'
op|'('
name|'context'
op|','
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DiskConfigTestCase
dedent|''
name|'class'
name|'DiskConfigTestCase'
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
name|'DiskConfigTestCase'
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
name|'verbose'
op|'='
name|'True'
op|','
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
string|"'Disk_config'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_setup_fake_image_service'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'fakes'
op|'.'
name|'stub_out_nw_api'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
nl|'\n'
name|'FAKE_INSTANCES'
op|'='
op|'['
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'1'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'MANUAL_INSTANCE_UUID'
op|','
nl|'\n'
name|'auto_disk_config'
op|'='
name|'False'
op|')'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_instance'
op|'('
number|'2'
op|','
nl|'\n'
name|'uuid'
op|'='
name|'AUTO_INSTANCE_UUID'
op|','
nl|'\n'
name|'auto_disk_config'
op|'='
name|'True'
op|')'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get
name|'def'
name|'fake_instance_get'
op|'('
name|'context'
op|','
name|'id_'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'instance'
name|'in'
name|'FAKE_INSTANCES'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'id_'
op|'=='
name|'instance'
op|'['
string|"'id'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
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
name|'fake_instance_get'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_by_uuid
name|'def'
name|'fake_instance_get_by_uuid'
op|'('
name|'context'
op|','
name|'uuid'
op|','
name|'columns_to_join'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'instance'
name|'in'
name|'FAKE_INSTANCES'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'uuid'
op|'=='
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'instance'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
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
name|'fake_instance_get_by_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_all
name|'def'
name|'fake_instance_get_all'
op|'('
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'FAKE_INSTANCES'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_all'"
op|','
name|'fake_instance_get_all'
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
name|'fake_instance_get_all'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_create
name|'def'
name|'fake_instance_create'
op|'('
name|'context'
op|','
name|'inst_'
op|','
name|'session'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'inst'
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
number|'1'
op|','
nl|'\n'
string|"'uuid'"
op|':'
name|'AUTO_INSTANCE_UUID'
op|','
nl|'\n'
string|"'created_at'"
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
string|"'updated_at'"
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
string|"'progress'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'instance-1'"
op|','
comment|'# this is a property'
nl|'\n'
string|"'task_state'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'vm_state'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'auto_disk_config'"
op|':'
name|'inst_'
op|'['
string|"'auto_disk_config'"
op|']'
op|','
nl|'\n'
string|"'security_groups'"
op|':'
name|'inst_'
op|'['
string|"'security_groups'"
op|']'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_for_create
name|'def'
name|'fake_instance_get_for_create'
op|'('
name|'context'
op|','
name|'id_'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'('
name|'inst'
op|','
name|'inst'
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
name|'db'
op|','
string|"'instance_update_and_get_original'"
op|','
nl|'\n'
name|'fake_instance_get_for_create'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_get_all_for_create
name|'def'
name|'fake_instance_get_all_for_create'
op|'('
name|'context'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'['
name|'inst'
op|']'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
string|"'instance_get_all'"
op|','
nl|'\n'
name|'fake_instance_get_all_for_create'
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
name|'fake_instance_get_all_for_create'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_instance_add_security_group
name|'def'
name|'fake_instance_add_security_group'
op|'('
name|'context'
op|','
name|'instance_id'
op|','
nl|'\n'
name|'security_group_id'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'db'
op|','
nl|'\n'
string|"'instance_add_security_group'"
op|','
nl|'\n'
name|'fake_instance_add_security_group'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'inst'
newline|'\n'
nl|'\n'
dedent|''
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
name|'fake_instance_create'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'compute'
op|'.'
name|'APIRouter'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
string|"'images'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_fake_image_service
dedent|''
name|'def'
name|'_setup_fake_image_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'image_service'
op|'='
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'stub_out_image_service'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'timestamp'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2011'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'2'
op|','
number|'3'
op|')'
newline|'\n'
name|'image'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'88580842-f50a-11e2-8d3a-f23c91aec05e'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'fakeimage7'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'timestamp'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'timestamp'
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
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'ova'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vhd'"
op|','
nl|'\n'
string|"'size'"
op|':'
string|"'74185822'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'auto_disk_config'"
op|':'
string|"'Disabled'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'image_service'
op|'.'
name|'create'
op|'('
name|'None'
op|','
name|'image'
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
name|'DiskConfigTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'FakeImageService_reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|assertDiskConfig
dedent|''
name|'def'
name|'assertDiskConfig'
op|'('
name|'self'
op|','
name|'dict_'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assert_'
op|'('
name|'API_DISK_CONFIG'
name|'in'
name|'dict_'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dict_'
op|'['
name|'API_DISK_CONFIG'
op|']'
op|','
name|'value'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_server
dedent|''
name|'def'
name|'test_show_server'
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
nl|'\n'
string|"'/fake/servers/%s'"
op|'%'
name|'MANUAL_INSTANCE_UUID'
op|')'
newline|'\n'
name|'res'
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
name|'server_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
string|"'MANUAL'"
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
nl|'\n'
string|"'/fake/servers/%s'"
op|'%'
name|'AUTO_INSTANCE_UUID'
op|')'
newline|'\n'
name|'res'
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
name|'server_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
string|"'AUTO'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_servers
dedent|''
name|'def'
name|'test_detail_servers'
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
string|"'/fake/servers/detail'"
op|')'
newline|'\n'
name|'res'
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
name|'server_dicts'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'servers'"
op|']'
newline|'\n'
nl|'\n'
name|'expectations'
op|'='
op|'['
string|"'MANUAL'"
op|','
string|"'AUTO'"
op|']'
newline|'\n'
name|'for'
name|'server_dict'
op|','
name|'expected'
name|'in'
name|'zip'
op|'('
name|'server_dicts'
op|','
name|'expectations'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_image
dedent|''
dedent|''
name|'def'
name|'test_show_image'
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
nl|'\n'
string|"'/fake/images/a440c04b-79fa-479c-bed1-0b816eaec379'"
op|')'
newline|'\n'
name|'res'
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
name|'image_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'image'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'image_dict'
op|','
string|"'MANUAL'"
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
nl|'\n'
string|"'/fake/images/70a599e0-31e7-49b7-b260-868f441e862b'"
op|')'
newline|'\n'
name|'res'
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
name|'image_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'image'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'image_dict'
op|','
string|"'AUTO'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_image
dedent|''
name|'def'
name|'test_detail_image'
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
string|"'/fake/images/detail'"
op|')'
newline|'\n'
name|'res'
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
name|'image_dicts'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'images'"
op|']'
newline|'\n'
nl|'\n'
name|'expectations'
op|'='
op|'['
string|"'MANUAL'"
op|','
string|"'AUTO'"
op|']'
newline|'\n'
name|'for'
name|'image_dict'
op|','
name|'expected'
name|'in'
name|'zip'
op|'('
name|'image_dicts'
op|','
name|'expectations'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(sirp): image fixtures 6 and 7 are setup for'
nl|'\n'
comment|'# auto_disk_config testing'
nl|'\n'
indent|'            '
name|'if'
name|'image_dict'
op|'['
string|"'id'"
op|']'
name|'in'
op|'('
number|'6'
op|','
number|'7'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'image_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_override_auto
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_create_server_override_auto'
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
string|"'/fake/servers'"
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
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'1'"
op|','
nl|'\n'
name|'API_DISK_CONFIG'
op|':'
string|"'AUTO'"
nl|'\n'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
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
name|'res'
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
name|'server_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
string|"'AUTO'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_override_manual
dedent|''
name|'def'
name|'test_create_server_override_manual'
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
string|"'/fake/servers'"
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
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'cedef40a-ed67-4d10-800e-17455edce175'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'1'"
op|','
nl|'\n'
name|'API_DISK_CONFIG'
op|':'
string|"'MANUAL'"
nl|'\n'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
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
name|'res'
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
name|'server_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
string|"'MANUAL'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_detect_from_image
dedent|''
name|'def'
name|'test_create_server_detect_from_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""If user doesn\'t pass in diskConfig for server, use image metadata\n        to specify AUTO or MANUAL.\n        """'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/fake/servers'"
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
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'a440c04b-79fa-479c-bed1-0b816eaec379'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'1'"
op|','
nl|'\n'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
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
name|'res'
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
name|'server_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
string|"'MANUAL'"
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
string|"'/fake/servers'"
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
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'70a599e0-31e7-49b7-b260-868f441e862b'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'1'"
op|','
nl|'\n'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
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
name|'res'
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
name|'server_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
string|"'AUTO'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_detect_from_image_disabled_goes_to_manual
dedent|''
name|'def'
name|'test_create_server_detect_from_image_disabled_goes_to_manual'
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
string|"'/fake/servers'"
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
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'88580842-f50a-11e2-8d3a-f23c91aec05e'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'1'"
op|','
nl|'\n'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
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
name|'res'
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
name|'server_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
string|"'MANUAL'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_errors_when_disabled_and_auto
dedent|''
name|'def'
name|'test_create_server_errors_when_disabled_and_auto'
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
string|"'/fake/servers'"
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
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'88580842-f50a-11e2-8d3a-f23c91aec05e'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'1'"
op|','
nl|'\n'
name|'API_DISK_CONFIG'
op|':'
string|"'AUTO'"
nl|'\n'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
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
name|'res'
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
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_server_when_disabled_and_manual
dedent|''
name|'def'
name|'test_create_server_when_disabled_and_manual'
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
string|"'/fake/servers'"
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
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'server_test'"
op|','
nl|'\n'
string|"'imageRef'"
op|':'
string|"'88580842-f50a-11e2-8d3a-f23c91aec05e'"
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
string|"'1'"
op|','
nl|'\n'
name|'API_DISK_CONFIG'
op|':'
string|"'MANUAL'"
nl|'\n'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
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
name|'res'
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
name|'server_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
op|'['
string|"'server'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDiskConfig'
op|'('
name|'server_dict'
op|','
string|"'MANUAL'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_server_invalid_disk_config
dedent|''
name|'def'
name|'test_update_server_invalid_disk_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Return BadRequest if user passes an invalid diskConfig value.'
nl|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
nl|'\n'
string|"'/fake/servers/%s'"
op|'%'
name|'MANUAL_INSTANCE_UUID'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'req'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'server'"
op|':'
op|'{'
name|'API_DISK_CONFIG'
op|':'
string|"'server_test'"
op|'}'
op|'}'
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
name|'res'
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
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
name|'expected_msg'
op|'='
op|'('
string|'\'{"badRequest": {"message": "%s must be either\''
nl|'\n'
string|'\' \\\'MANUAL\\\' or \\\'AUTO\\\'.", "code": 400}}\''
op|'%'
nl|'\n'
name|'API_DISK_CONFIG'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'body'
op|','
name|'expected_msg'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
