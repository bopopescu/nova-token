begin_unit
comment|'#   Copyright 2012 OpenStack LLC.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'datetime'
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
op|'.'
name|'contrib'
name|'import'
name|'volume_actions'
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
op|'.'
name|'rpc'
name|'import'
name|'common'
name|'as'
name|'rpc_common'
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
DECL|function|stub_volume_get
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
indent|'    '
name|'volume'
op|'='
name|'fakes'
op|'.'
name|'stub_volume'
op|'('
name|'volume_id'
op|')'
newline|'\n'
name|'if'
name|'volume_id'
op|'=='
number|'5'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'in-use'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'volume'
op|'['
string|"'status'"
op|']'
op|'='
string|"'available'"
newline|'\n'
dedent|''
name|'return'
name|'volume'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_upload_volume_to_image_service
dedent|''
name|'def'
name|'stub_upload_volume_to_image_service'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
name|'metadata'
op|','
nl|'\n'
name|'force'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ret'
op|'='
op|'{'
string|'"id"'
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|'"updated_at"'
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|'"status"'
op|':'
string|"'uploading'"
op|','
nl|'\n'
string|'"display_description"'
op|':'
name|'volume'
op|'['
string|"'display_description'"
op|']'
op|','
nl|'\n'
string|'"size"'
op|':'
name|'volume'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
string|'"volume_type"'
op|':'
name|'volume'
op|'['
string|"'volume_type'"
op|']'
op|','
nl|'\n'
string|'"image_id"'
op|':'
number|'1'
op|','
nl|'\n'
string|'"container_format"'
op|':'
string|"'bare'"
op|','
nl|'\n'
string|'"disk_format"'
op|':'
string|"'raw'"
op|','
nl|'\n'
string|'"image_name"'
op|':'
string|"'image_name'"
op|'}'
newline|'\n'
name|'return'
name|'ret'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeImageActionsTest
dedent|''
name|'class'
name|'VolumeImageActionsTest'
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
name|'VolumeImageActionsTest'
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
name|'volume_actions'
op|'.'
name|'VolumeActionsController'
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
string|"'get'"
op|','
name|'stub_volume_get'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_copy_volume_to_image
dedent|''
name|'def'
name|'test_copy_volume_to_image'
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
nl|'\n'
string|'"copy_volume_to_image"'
op|','
nl|'\n'
name|'stub_upload_volume_to_image_service'
op|')'
newline|'\n'
nl|'\n'
name|'id'
op|'='
number|'1'
newline|'\n'
name|'vol'
op|'='
op|'{'
string|'"container_format"'
op|':'
string|"'bare'"
op|','
nl|'\n'
string|'"disk_format"'
op|':'
string|"'raw'"
op|','
nl|'\n'
string|'"image_name"'
op|':'
string|"'image_name'"
op|','
nl|'\n'
string|'"force"'
op|':'
name|'True'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"os-volume_upload_image"'
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
string|"'/v1/tenant1/volumes/%s/action'"
op|'%'
name|'id'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_volume_upload_image'
op|'('
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'os-volume_upload_image'"
op|':'
op|'{'
string|"'id'"
op|':'
name|'id'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|','
number|'1'
op|')'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'uploading'"
op|','
nl|'\n'
string|"'display_description'"
op|':'
string|"'displaydesc'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'volume_type'"
op|':'
op|'{'
string|"'name'"
op|':'
string|"'vol_type_name'"
op|'}'
op|','
nl|'\n'
string|"'image_id'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'container_format'"
op|':'
string|"'bare'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'raw'"
op|','
nl|'\n'
string|"'image_name'"
op|':'
string|"'image_name'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_copy_volume_to_image_volumenotfound
dedent|''
name|'def'
name|'test_copy_volume_to_image_volumenotfound'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|stub_volume_get_raise_exc
indent|'        '
name|'def'
name|'stub_volume_get_raise_exc'
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
name|'raise'
name|'exception'
op|'.'
name|'VolumeNotFound'
op|'('
name|'volume_id'
op|'='
name|'volume_id'
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
name|'stub_volume_get_raise_exc'
op|')'
newline|'\n'
nl|'\n'
name|'id'
op|'='
number|'1'
newline|'\n'
name|'vol'
op|'='
op|'{'
string|'"container_format"'
op|':'
string|"'bare'"
op|','
nl|'\n'
string|'"disk_format"'
op|':'
string|"'raw'"
op|','
nl|'\n'
string|'"image_name"'
op|':'
string|"'image_name'"
op|','
nl|'\n'
string|'"force"'
op|':'
name|'True'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"os-volume_upload_image"'
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
string|"'/v1/tenant1/volumes/%s/action'"
op|'%'
name|'id'
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
name|'_volume_upload_image'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'id'
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_copy_volume_to_image_invalidvolume
dedent|''
name|'def'
name|'test_copy_volume_to_image_invalidvolume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|stub_upload_volume_to_image_service_raise
indent|'        '
name|'def'
name|'stub_upload_volume_to_image_service_raise'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
nl|'\n'
name|'metadata'
op|','
name|'force'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolume'
newline|'\n'
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
nl|'\n'
string|'"copy_volume_to_image"'
op|','
nl|'\n'
name|'stub_upload_volume_to_image_service_raise'
op|')'
newline|'\n'
nl|'\n'
name|'id'
op|'='
number|'1'
newline|'\n'
name|'vol'
op|'='
op|'{'
string|'"container_format"'
op|':'
string|"'bare'"
op|','
nl|'\n'
string|'"disk_format"'
op|':'
string|"'raw'"
op|','
nl|'\n'
string|'"image_name"'
op|':'
string|"'image_name'"
op|','
nl|'\n'
string|'"force"'
op|':'
name|'True'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"os-volume_upload_image"'
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
string|"'/v1/tenant1/volumes/%s/action'"
op|'%'
name|'id'
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
name|'_volume_upload_image'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'id'
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_copy_volume_to_image_valueerror
dedent|''
name|'def'
name|'test_copy_volume_to_image_valueerror'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|stub_upload_volume_to_image_service_raise
indent|'        '
name|'def'
name|'stub_upload_volume_to_image_service_raise'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
nl|'\n'
name|'metadata'
op|','
name|'force'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'ValueError'
newline|'\n'
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
nl|'\n'
string|'"copy_volume_to_image"'
op|','
nl|'\n'
name|'stub_upload_volume_to_image_service_raise'
op|')'
newline|'\n'
nl|'\n'
name|'id'
op|'='
number|'1'
newline|'\n'
name|'vol'
op|'='
op|'{'
string|'"container_format"'
op|':'
string|"'bare'"
op|','
nl|'\n'
string|'"disk_format"'
op|':'
string|"'raw'"
op|','
nl|'\n'
string|'"image_name"'
op|':'
string|"'image_name'"
op|','
nl|'\n'
string|'"force"'
op|':'
name|'True'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"os-volume_upload_image"'
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
string|"'/v1/tenant1/volumes/%s/action'"
op|'%'
name|'id'
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
name|'_volume_upload_image'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'id'
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_copy_volume_to_image_remoteerror
dedent|''
name|'def'
name|'test_copy_volume_to_image_remoteerror'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|stub_upload_volume_to_image_service_raise
indent|'        '
name|'def'
name|'stub_upload_volume_to_image_service_raise'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'volume'
op|','
nl|'\n'
name|'metadata'
op|','
name|'force'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'rpc_common'
op|'.'
name|'RemoteError'
newline|'\n'
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
nl|'\n'
string|'"copy_volume_to_image"'
op|','
nl|'\n'
name|'stub_upload_volume_to_image_service_raise'
op|')'
newline|'\n'
nl|'\n'
name|'id'
op|'='
number|'1'
newline|'\n'
name|'vol'
op|'='
op|'{'
string|'"container_format"'
op|':'
string|"'bare'"
op|','
nl|'\n'
string|'"disk_format"'
op|':'
string|"'raw'"
op|','
nl|'\n'
string|'"image_name"'
op|':'
string|"'image_name'"
op|','
nl|'\n'
string|'"force"'
op|':'
name|'True'
op|'}'
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"os-volume_upload_image"'
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
string|"'/v1/tenant1/volumes/%s/action'"
op|'%'
name|'id'
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
name|'_volume_upload_image'
op|','
nl|'\n'
name|'req'
op|','
nl|'\n'
name|'id'
op|','
nl|'\n'
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
