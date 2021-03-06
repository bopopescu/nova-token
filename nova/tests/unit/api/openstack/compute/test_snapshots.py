begin_unit
comment|'# Copyright 2011 Denali Systems, Inc.'
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
name|'import'
name|'volumes'
name|'as'
name|'volumes_v21'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'volume'
name|'import'
name|'cinder'
newline|'\n'
nl|'\n'
DECL|variable|FAKE_UUID
name|'FAKE_UUID'
op|'='
string|"'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SnapshotApiTestV21
name|'class'
name|'SnapshotApiTestV21'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|controller
indent|'    '
name|'controller'
op|'='
name|'volumes_v21'
op|'.'
name|'SnapshotController'
op|'('
op|')'
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
name|'SnapshotApiTestV21'
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
name|'cinder'
op|'.'
name|'API'
op|','
string|'"create_snapshot"'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_snapshot_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cinder'
op|'.'
name|'API'
op|','
string|'"create_snapshot_force"'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_snapshot_create'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cinder'
op|'.'
name|'API'
op|','
string|'"delete_snapshot"'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_snapshot_delete'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cinder'
op|'.'
name|'API'
op|','
string|'"get_snapshot"'
op|','
name|'fakes'
op|'.'
name|'stub_snapshot_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cinder'
op|'.'
name|'API'
op|','
string|'"get_all_snapshots"'
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'stub_snapshot_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'cinder'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_get'
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
DECL|member|_test_snapshot_create
dedent|''
name|'def'
name|'_test_snapshot_create'
op|'('
name|'self'
op|','
name|'force'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'snapshot'
op|'='
op|'{'
string|'"volume_id"'
op|':'
string|"'12'"
op|','
nl|'\n'
string|'"force"'
op|':'
name|'force'
op|','
nl|'\n'
string|'"display_name"'
op|':'
string|'"Snapshot Test Name"'
op|','
nl|'\n'
string|'"display_description"'
op|':'
string|'"Snapshot Test Desc"'
op|'}'
newline|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'snapshot'
op|'='
name|'snapshot'
op|')'
newline|'\n'
name|'resp_dict'
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
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'snapshot'"
op|','
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'snapshot'
op|'['
string|"'display_name'"
op|']'
op|','
nl|'\n'
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'displayName'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'snapshot'
op|'['
string|"'display_description'"
op|']'
op|','
nl|'\n'
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'displayDescription'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'snapshot'
op|'['
string|"'volume_id'"
op|']'
op|','
nl|'\n'
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'volumeId'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_create
dedent|''
name|'def'
name|'test_snapshot_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_snapshot_create'
op|'('
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_create_force
dedent|''
name|'def'
name|'test_snapshot_create_force'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_snapshot_create'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_create_invalid_force_param
dedent|''
name|'def'
name|'test_snapshot_create_invalid_force_param'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'snapshot'"
op|':'
op|'{'
string|"'volume_id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'force'"
op|':'
string|"'**&&^^%%$$##@@'"
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
DECL|member|test_snapshot_delete
dedent|''
name|'def'
name|'test_snapshot_delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'snapshot_id'
op|'='
string|"'123'"
newline|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
nl|'\n'
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
name|'volumes_v21'
op|'.'
name|'SnapshotController'
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
name|'delete'
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
name|'result'
op|'.'
name|'status_int'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'202'
op|','
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
name|'cinder'
op|'.'
name|'API'
op|','
string|"'delete_snapshot'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'SnapshotNotFound'
op|'('
name|'snapshot_id'
op|'='
name|'FAKE_UUID'
op|')'
op|')'
newline|'\n'
DECL|member|test_delete_snapshot_not_exists
name|'def'
name|'test_delete_snapshot_not_exists'
op|'('
name|'self'
op|','
name|'mock_mr'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'delete'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
name|'FAKE_UUID'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_delete_invalid_id
dedent|''
name|'def'
name|'test_snapshot_delete_invalid_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'delete'
op|','
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'-1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_show
dedent|''
name|'def'
name|'test_snapshot_show'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'snapshot_id'
op|'='
string|"'123'"
newline|'\n'
name|'resp_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'req'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'snapshot'"
op|','
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'snapshot_id'
op|')'
op|','
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_show_invalid_id
dedent|''
name|'def'
name|'test_snapshot_show_invalid_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
nl|'\n'
name|'self'
op|'.'
name|'req'
op|','
string|"'-1'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_detail
dedent|''
name|'def'
name|'test_snapshot_detail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'snapshots'"
op|','
name|'resp_dict'
op|')'
newline|'\n'
name|'resp_snapshots'
op|'='
name|'resp_dict'
op|'['
string|"'snapshots'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'resp_snapshots'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'resp_snapshot'
op|'='
name|'resp_snapshots'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'102'
op|','
name|'resp_snapshot'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_index
dedent|''
name|'def'
name|'test_snapshot_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resp_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'req'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'snapshots'"
op|','
name|'resp_dict'
op|')'
newline|'\n'
name|'resp_snapshots'
op|'='
name|'resp_dict'
op|'['
string|"'snapshots'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'len'
op|'('
name|'resp_snapshots'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
