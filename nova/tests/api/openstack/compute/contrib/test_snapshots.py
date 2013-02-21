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
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
name|'volumes'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
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
name|'timeutils'
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
name|'volume'
name|'import'
name|'cinder'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SnapshotApiTest
name|'class'
name|'SnapshotApiTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'SnapshotApiTest'
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
string|"'Volumes'"
op|']'
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
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'os-snapshots'"
op|','
op|')'
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
name|'snapshot'
op|'='
op|'{'
string|'"volume_id"'
op|':'
number|'12'
op|','
nl|'\n'
string|'"force"'
op|':'
name|'False'
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
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-snapshots'"
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
number|'200'
op|')'
newline|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'snapshot'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'displayName'"
op|']'
op|','
nl|'\n'
name|'snapshot'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'displayDescription'"
op|']'
op|','
nl|'\n'
name|'snapshot'
op|'['
string|"'display_description'"
op|']'
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
name|'snapshot'
op|'='
op|'{'
string|'"volume_id"'
op|':'
number|'12'
op|','
nl|'\n'
string|'"force"'
op|':'
name|'True'
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
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-snapshots'"
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
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'snapshot'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'displayName'"
op|']'
op|','
nl|'\n'
name|'snapshot'
op|'['
string|"'display_name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'displayDescription'"
op|']'
op|','
nl|'\n'
name|'snapshot'
op|'['
string|"'display_description'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Test invalid force paramter'
nl|'\n'
name|'snapshot'
op|'='
op|'{'
string|'"volume_id"'
op|':'
number|'12'
op|','
nl|'\n'
string|'"force"'
op|':'
string|"'**&&^^%%$$##@@'"
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
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-snapshots'"
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
number|'123'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-snapshots/%d'"
op|'%'
name|'snapshot_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
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
name|'snapshot_id'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-snapshots/%d'"
op|'%'
name|'snapshot_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
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
number|'404'
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
number|'123'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-snapshots/%d'"
op|'%'
name|'snapshot_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
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
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'snapshot'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'resp_dict'
op|'['
string|"'snapshot'"
op|']'
op|'['
string|"'id'"
op|']'
op|','
name|'str'
op|'('
name|'snapshot_id'
op|')'
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
name|'snapshot_id'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-snapshots/%d'"
op|'%'
name|'snapshot_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
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
name|'resp'
op|'.'
name|'status_int'
op|','
number|'404'
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
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-snapshots/detail'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'GET'"
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
name|'resp'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'resp'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'snapshots'"
name|'in'
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
name|'len'
op|'('
name|'resp_snapshots'
op|')'
op|','
number|'3'
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
name|'resp_snapshot'
op|'['
string|"'id'"
op|']'
op|','
number|'102'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SnapshotSerializerTest
dedent|''
dedent|''
name|'class'
name|'SnapshotSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_verify_snapshot
indent|'    '
name|'def'
name|'_verify_snapshot'
op|'('
name|'self'
op|','
name|'snap'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'tree'
op|'.'
name|'tag'
op|','
string|"'snapshot'"
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'attr'
name|'in'
op|'('
string|"'id'"
op|','
string|"'status'"
op|','
string|"'size'"
op|','
string|"'createdAt'"
op|','
nl|'\n'
string|"'displayName'"
op|','
string|"'displayDescription'"
op|','
string|"'volumeId'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'snap'
op|'['
name|'attr'
op|']'
op|')'
op|','
name|'tree'
op|'.'
name|'get'
op|'('
name|'attr'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_show_create_serializer
dedent|''
dedent|''
name|'def'
name|'test_snapshot_show_create_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'volumes'
op|'.'
name|'SnapshotTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_snapshot'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'snap_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'snap_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'createdAt'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'displayName'
op|'='
string|"'snap_name'"
op|','
nl|'\n'
name|'displayDescription'
op|'='
string|"'snap_desc'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
op|')'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'dict'
op|'('
name|'snapshot'
op|'='
name|'raw_snapshot'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_verify_snapshot'
op|'('
name|'raw_snapshot'
op|','
name|'tree'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_snapshot_index_detail_serializer
dedent|''
name|'def'
name|'test_snapshot_index_detail_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'serializer'
op|'='
name|'volumes'
op|'.'
name|'SnapshotsTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_snapshots'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'snap1_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'snap1_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'createdAt'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'displayName'
op|'='
string|"'snap1_name'"
op|','
nl|'\n'
name|'displayDescription'
op|'='
string|"'snap1_desc'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol1_id'"
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'snap2_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'snap2_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'createdAt'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'displayName'
op|'='
string|"'snap2_name'"
op|','
nl|'\n'
name|'displayDescription'
op|'='
string|"'snap2_desc'"
op|','
nl|'\n'
name|'volumeId'
op|'='
string|"'vol2_id'"
op|','
nl|'\n'
op|')'
op|']'
newline|'\n'
name|'text'
op|'='
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'dict'
op|'('
name|'snapshots'
op|'='
name|'raw_snapshots'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'snapshots'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'raw_snapshots'
op|')'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'idx'
op|','
name|'child'
name|'in'
name|'enumerate'
op|'('
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_verify_snapshot'
op|'('
name|'raw_snapshots'
op|'['
name|'idx'
op|']'
op|','
name|'child'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
