begin_unit
comment|'# Copyright 2013 Josh Durgin'
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
name|'volume'
name|'import'
name|'volumes'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'api'
name|'as'
name|'volume_api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeApiTest
name|'class'
name|'VolumeApiTest'
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
name|'VolumeApiTest'
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
name|'volumes'
op|'.'
name|'VolumeController'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_api'
op|'.'
name|'API'
op|','
string|"'get_all'"
op|','
name|'fakes'
op|'.'
name|'stub_volume_get_all'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fakes'
op|'.'
name|'stub_volume_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_api'
op|'.'
name|'API'
op|','
string|"'delete'"
op|','
name|'fakes'
op|'.'
name|'stub_volume_delete'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_create
dedent|''
name|'def'
name|'test_volume_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_api'
op|'.'
name|'API'
op|','
string|'"create"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_create'
op|')'
newline|'\n'
nl|'\n'
name|'vol'
op|'='
op|'{'
string|'"size"'
op|':'
number|'100'
op|','
nl|'\n'
string|'"display_name"'
op|':'
string|'"Volume Test Name"'
op|','
nl|'\n'
string|'"display_description"'
op|':'
string|'"Volume Test Desc"'
op|','
nl|'\n'
string|'"availability_zone"'
op|':'
string|'"zone1:host1"'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"volume"'
op|':'
name|'vol'
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
string|"'/v1/volumes'"
op|')'
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
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'volume'"
op|':'
op|'{'
string|"'status'"
op|':'
string|"'fakestatus'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'Volume Test Desc'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'zone1:host1'"
op|','
nl|'\n'
string|"'display_name'"
op|':'
string|"'Volume Test Name'"
op|','
nl|'\n'
string|"'attachments'"
op|':'
op|'['
op|'{'
string|"'device'"
op|':'
string|"'/'"
op|','
nl|'\n'
string|"'server_id'"
op|':'
string|"'fakeuuid'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'volume_type'"
op|':'
string|"'vol_type_name'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1999'
op|','
number|'1'
op|','
number|'1'
op|','
nl|'\n'
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'100'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'obj'
op|','
name|'expected'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'code'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'location'"
name|'in'
name|'res'
op|'.'
name|'headers'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_creation_fails_with_bad_size
dedent|''
name|'def'
name|'test_volume_creation_fails_with_bad_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vol'
op|'='
op|'{'
string|'"size"'
op|':'
string|"''"
op|','
nl|'\n'
string|'"display_name"'
op|':'
string|'"Volume Test Name"'
op|','
nl|'\n'
string|'"display_description"'
op|':'
string|'"Volume Test Desc"'
op|','
nl|'\n'
string|'"availability_zone"'
op|':'
string|'"zone1:host1"'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"volume"'
op|':'
name|'vol'
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
string|"'/v1/volumes'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_create_no_body
dedent|''
name|'def'
name|'test_volume_create_no_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
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
string|"'/v1/volumes'"
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
name|'HTTPUnprocessableEntity'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'create'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_list
dedent|''
name|'def'
name|'test_volume_list'
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
string|"'/v1/volumes'"
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
name|'expected'
op|'='
op|'{'
string|"'volumes'"
op|':'
op|'['
op|'{'
string|"'status'"
op|':'
string|"'fakestatus'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'displaydesc'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'fakeaz'"
op|','
nl|'\n'
string|"'display_name'"
op|':'
string|"'displayname'"
op|','
nl|'\n'
string|"'attachments'"
op|':'
op|'['
op|'{'
string|"'device'"
op|':'
string|"'/'"
op|','
nl|'\n'
string|"'server_id'"
op|':'
string|"'fakeuuid'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'volume_type'"
op|':'
string|"'vol_type_name'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1999'
op|','
number|'1'
op|','
number|'1'
op|','
nl|'\n'
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'maxDiff'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_list_detail
dedent|''
name|'def'
name|'test_volume_list_detail'
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
string|"'/v1/volumes/detail'"
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
name|'expected'
op|'='
op|'{'
string|"'volumes'"
op|':'
op|'['
op|'{'
string|"'status'"
op|':'
string|"'fakestatus'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'displaydesc'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'fakeaz'"
op|','
nl|'\n'
string|"'display_name'"
op|':'
string|"'displayname'"
op|','
nl|'\n'
string|"'attachments'"
op|':'
op|'['
op|'{'
string|"'device'"
op|':'
string|"'/'"
op|','
nl|'\n'
string|"'server_id'"
op|':'
string|"'fakeuuid'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'volume_type'"
op|':'
string|"'vol_type_name'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1999'
op|','
number|'1'
op|','
number|'1'
op|','
nl|'\n'
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
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
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_show
dedent|''
name|'def'
name|'test_volume_show'
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
string|"'/v1/volumes/1'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'volume'"
op|':'
op|'{'
string|"'status'"
op|':'
string|"'fakestatus'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'displaydesc'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'fakeaz'"
op|','
nl|'\n'
string|"'display_name'"
op|':'
string|"'displayname'"
op|','
nl|'\n'
string|"'attachments'"
op|':'
op|'['
op|'{'
string|"'device'"
op|':'
string|"'/'"
op|','
nl|'\n'
string|"'server_id'"
op|':'
string|"'fakeuuid'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'volume_id'"
op|':'
string|"'1'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'volume_type'"
op|':'
string|"'vol_type_name'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1999'
op|','
number|'1'
op|','
number|'1'
op|','
nl|'\n'
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_show_no_attachments
dedent|''
name|'def'
name|'test_volume_show_no_attachments'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|stub_volume_get
indent|'        '
name|'def'
name|'stub_volume_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fakes'
op|'.'
name|'stub_volume'
op|'('
name|'volume_id'
op|','
name|'attach_status'
op|'='
string|"'detached'"
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
name|'volume_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'stub_volume_get'
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
string|"'/v1/volumes/1'"
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
string|"'1'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'volume'"
op|':'
op|'{'
string|"'status'"
op|':'
string|"'fakestatus'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'displaydesc'"
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
string|"'fakeaz'"
op|','
nl|'\n'
string|"'display_name'"
op|':'
string|"'displayname'"
op|','
nl|'\n'
string|"'attachments'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'volume_type'"
op|':'
string|"'vol_type_name'"
op|','
nl|'\n'
string|"'snapshot_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1999'
op|','
number|'1'
op|','
number|'1'
op|','
nl|'\n'
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_show_no_volume
dedent|''
name|'def'
name|'test_volume_show_no_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_get_notfound'
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
string|"'/v1/volumes/1'"
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
nl|'\n'
name|'req'
op|','
nl|'\n'
number|'1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_delete
dedent|''
name|'def'
name|'test_volume_delete'
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
string|"'/v1/volumes/1'"
op|')'
newline|'\n'
name|'resp'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
number|'1'
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
DECL|member|test_volume_delete_no_volume
dedent|''
name|'def'
name|'test_volume_delete_no_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_api'
op|'.'
name|'API'
op|','
string|'"get"'
op|','
name|'fakes'
op|'.'
name|'stub_volume_get_notfound'
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
string|"'/v1/volumes/1'"
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
name|'delete'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeSerializerTest
dedent|''
dedent|''
name|'class'
name|'VolumeSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_verify_volume_attachment
indent|'    '
name|'def'
name|'_verify_volume_attachment'
op|'('
name|'self'
op|','
name|'attach'
op|','
name|'tree'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'attr'
name|'in'
op|'('
string|"'id'"
op|','
string|"'volume_id'"
op|','
string|"'server_id'"
op|','
string|"'device'"
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
name|'attach'
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
DECL|member|_verify_volume
dedent|''
dedent|''
name|'def'
name|'_verify_volume'
op|'('
name|'self'
op|','
name|'vol'
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
string|"'volume'"
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
string|"'availability_zone'"
op|','
string|"'created_at'"
op|','
nl|'\n'
string|"'display_name'"
op|','
string|"'display_description'"
op|','
string|"'volume_type'"
op|','
nl|'\n'
string|"'snapshot_id'"
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
name|'vol'
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
dedent|''
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'child'
op|'.'
name|'tag'
name|'in'
op|'('
string|"'attachments'"
op|','
string|"'metadata'"
op|')'
op|')'
newline|'\n'
name|'if'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'attachments'"
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'len'
op|'('
name|'child'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'attachment'"
op|','
name|'child'
op|'['
number|'0'
op|']'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_verify_volume_attachment'
op|'('
name|'vol'
op|'['
string|"'attachments'"
op|']'
op|'['
number|'0'
op|']'
op|','
name|'child'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'child'
op|'.'
name|'tag'
op|'=='
string|"'metadata'"
op|':'
newline|'\n'
indent|'                '
name|'not_seen'
op|'='
name|'set'
op|'('
name|'vol'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|')'
newline|'\n'
name|'for'
name|'gr_child'
name|'in'
name|'child'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'gr_child'
op|'.'
name|'tag'
name|'in'
name|'not_seen'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'str'
op|'('
name|'vol'
op|'['
string|"'metadata'"
op|']'
op|'['
name|'gr_child'
op|'.'
name|'tag'
op|']'
op|')'
op|','
nl|'\n'
name|'gr_child'
op|'.'
name|'text'
op|')'
newline|'\n'
name|'not_seen'
op|'.'
name|'remove'
op|'('
name|'gr_child'
op|'.'
name|'tag'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'len'
op|'('
name|'not_seen'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_show_create_serializer
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_volume_show_create_serializer'
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
name|'VolumeTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_volume'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'vol_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'availability_zone'
op|'='
string|"'vol_availability'"
op|','
nl|'\n'
name|'created_at'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'attachments'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
name|'volume_id'
op|'='
string|"'vol_id'"
op|','
nl|'\n'
name|'server_id'
op|'='
string|"'instance_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo'"
op|')'
op|']'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'vol_name'"
op|','
nl|'\n'
name|'display_description'
op|'='
string|"'vol_desc'"
op|','
nl|'\n'
name|'volume_type'
op|'='
string|"'vol_type'"
op|','
nl|'\n'
name|'snapshot_id'
op|'='
string|"'snap_id'"
op|','
nl|'\n'
name|'metadata'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'foo'
op|'='
string|"'bar'"
op|','
nl|'\n'
name|'baz'
op|'='
string|"'quux'"
op|','
nl|'\n'
op|')'
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
name|'volume'
op|'='
name|'raw_volume'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
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
name|'_verify_volume'
op|'('
name|'raw_volume'
op|','
name|'tree'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_volume_index_detail_serializer
dedent|''
name|'def'
name|'test_volume_index_detail_serializer'
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
name|'VolumesTemplate'
op|'('
op|')'
newline|'\n'
name|'raw_volumes'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol1_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'vol1_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'availability_zone'
op|'='
string|"'vol1_availability'"
op|','
nl|'\n'
name|'created_at'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'attachments'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol1_id'"
op|','
nl|'\n'
name|'volume_id'
op|'='
string|"'vol1_id'"
op|','
nl|'\n'
name|'server_id'
op|'='
string|"'instance_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo1'"
op|')'
op|']'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'vol1_name'"
op|','
nl|'\n'
name|'display_description'
op|'='
string|"'vol1_desc'"
op|','
nl|'\n'
name|'volume_type'
op|'='
string|"'vol1_type'"
op|','
nl|'\n'
name|'snapshot_id'
op|'='
string|"'snap1_id'"
op|','
nl|'\n'
name|'metadata'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'foo'
op|'='
string|"'vol1_foo'"
op|','
nl|'\n'
name|'bar'
op|'='
string|"'vol1_bar'"
op|','
nl|'\n'
op|')'
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
string|"'vol2_id'"
op|','
nl|'\n'
name|'status'
op|'='
string|"'vol2_status'"
op|','
nl|'\n'
name|'size'
op|'='
number|'1024'
op|','
nl|'\n'
name|'availability_zone'
op|'='
string|"'vol2_availability'"
op|','
nl|'\n'
name|'created_at'
op|'='
name|'timeutils'
op|'.'
name|'utcnow'
op|'('
op|')'
op|','
nl|'\n'
name|'attachments'
op|'='
op|'['
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'vol2_id'"
op|','
nl|'\n'
name|'volume_id'
op|'='
string|"'vol2_id'"
op|','
nl|'\n'
name|'server_id'
op|'='
string|"'instance_uuid'"
op|','
nl|'\n'
name|'device'
op|'='
string|"'/foo2'"
op|')'
op|']'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'vol2_name'"
op|','
nl|'\n'
name|'display_description'
op|'='
string|"'vol2_desc'"
op|','
nl|'\n'
name|'volume_type'
op|'='
string|"'vol2_type'"
op|','
nl|'\n'
name|'snapshot_id'
op|'='
string|"'snap2_id'"
op|','
nl|'\n'
name|'metadata'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'foo'
op|'='
string|"'vol2_foo'"
op|','
nl|'\n'
name|'bar'
op|'='
string|"'vol2_bar'"
op|','
nl|'\n'
op|')'
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
name|'volumes'
op|'='
name|'raw_volumes'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
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
string|"'volumes'"
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
name|'raw_volumes'
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
name|'_verify_volume'
op|'('
name|'raw_volumes'
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
