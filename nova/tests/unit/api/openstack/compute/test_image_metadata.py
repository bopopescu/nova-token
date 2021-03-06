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
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
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
name|'image_metadata'
name|'as'
name|'image_metadata_v21'
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
name|'tests'
op|'.'
name|'unit'
name|'import'
name|'image_fixtures'
newline|'\n'
nl|'\n'
DECL|variable|IMAGE_FIXTURES
name|'IMAGE_FIXTURES'
op|'='
name|'image_fixtures'
op|'.'
name|'get_image_fixtures'
op|'('
op|')'
newline|'\n'
DECL|variable|CHK_QUOTA_STR
name|'CHK_QUOTA_STR'
op|'='
string|"'nova.api.openstack.common.check_img_metadata_properties_quota'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_image_123
name|'def'
name|'get_image_123'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'IMAGE_FIXTURES'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageMetaDataTestV21
dedent|''
name|'class'
name|'ImageMetaDataTestV21'
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
name|'image_metadata_v21'
op|'.'
name|'ImageMetadataController'
newline|'\n'
DECL|variable|invalid_request
name|'invalid_request'
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
name|'ImageMetaDataTestV21'
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
name|'self'
op|'.'
name|'controller_class'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_index
name|'def'
name|'test_index'
op|'('
name|'self'
op|','
name|'get_all_mocked'
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
string|"'/v2/fake/images/123/metadata'"
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
op|','
string|"'123'"
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'{'
string|"'key1'"
op|':'
string|"'value1'"
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
name|'get_all_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_show
name|'def'
name|'test_show'
op|'('
name|'self'
op|','
name|'get_mocked'
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
string|"'/v2/fake/images/123/metadata/key1'"
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
string|"'123'"
op|','
string|"'key1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIn'
op|'('
string|"'meta'"
op|','
name|'res_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'meta'"
op|']'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'value1'"
op|','
name|'res_dict'
op|'['
string|"'meta'"
op|']'
op|'['
string|"'key1'"
op|']'
op|')'
newline|'\n'
name|'get_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_show_not_found
name|'def'
name|'test_show_not_found'
op|'('
name|'self'
op|','
name|'_get_mocked'
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
string|"'/v2/fake/images/123/metadata/key9'"
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
string|"'123'"
op|','
string|"'key9'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
string|"'100'"
op|')'
op|')'
newline|'\n'
DECL|member|test_show_image_not_found
name|'def'
name|'test_show_image_not_found'
op|'('
name|'self'
op|','
name|'_get_mocked'
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
string|"'/v2/fake/images/100/metadata/key1'"
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
string|"'100'"
op|','
string|"'key9'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|','
name|'get_mocked'
op|','
name|'update_mocked'
op|','
name|'quota_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_result'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
name|'mock_result'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'key7'"
op|']'
op|'='
string|"'value7'"
newline|'\n'
name|'update_mocked'
op|'.'
name|'return_value'
op|'='
name|'mock_result'
newline|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/images/123/metadata'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"key7"'
op|':'
string|'"value7"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
string|"'123'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'get_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|')'
newline|'\n'
name|'expected'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'properties'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'key1'"
op|':'
string|"'value1'"
op|','
comment|'# existing meta'
nl|'\n'
string|"'key7'"
op|':'
string|"'value7'"
comment|'# new meta'
nl|'\n'
op|'}'
newline|'\n'
name|'quota_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'expected'
op|'['
string|'"properties"'
op|']'
op|')'
newline|'\n'
name|'update_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|','
name|'expected'
op|','
nl|'\n'
name|'data'
op|'='
name|'None'
op|','
name|'purge_props'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'expected_output'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'{'
string|"'key1'"
op|':'
string|"'value1'"
op|','
string|"'key7'"
op|':'
string|"'value7'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_output'
op|','
name|'res'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
string|"'100'"
op|')'
op|')'
newline|'\n'
DECL|member|test_create_image_not_found
name|'def'
name|'test_create_image_not_found'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|','
name|'update_mocked'
op|','
nl|'\n'
name|'quota_mocked'
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
string|"'/v2/fake/images/100/metadata'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"key7"'
op|':'
string|'"value7"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
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
name|'create'
op|','
name|'req'
op|','
string|"'100'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'quota_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'update_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_update_all
name|'def'
name|'test_update_all'
op|'('
name|'self'
op|','
name|'get_mocked'
op|','
name|'update_mocked'
op|','
name|'quota_mocked'
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
string|"'/v2/fake/images/123/metadata'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"key9"'
op|':'
string|'"value9"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
name|'update_all'
op|'('
name|'req'
op|','
string|"'123'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'get_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|')'
newline|'\n'
name|'expected'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'properties'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'key9'"
op|':'
string|"'value9'"
comment|'# replace meta'
nl|'\n'
op|'}'
newline|'\n'
name|'quota_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'expected'
op|'['
string|'"properties"'
op|']'
op|')'
newline|'\n'
name|'update_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|','
name|'expected'
op|','
nl|'\n'
name|'data'
op|'='
name|'None'
op|','
name|'purge_props'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'expected_output'
op|'='
op|'{'
string|"'metadata'"
op|':'
op|'{'
string|"'key9'"
op|':'
string|"'value9'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_output'
op|','
name|'res'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
string|"'100'"
op|')'
op|')'
newline|'\n'
DECL|member|test_update_all_image_not_found
name|'def'
name|'test_update_all_image_not_found'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|','
name|'quota_mocked'
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
string|"'/v2/fake/images/100/metadata'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"key9"'
op|':'
string|'"value9"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
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
name|'update_all'
op|','
name|'req'
op|','
string|"'100'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'quota_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_update_item
name|'def'
name|'test_update_item'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|','
name|'update_mocked'
op|','
name|'quota_mocked'
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
string|"'/v2/fake/images/123/metadata/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"zz"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
name|'update'
op|'('
name|'req'
op|','
string|"'123'"
op|','
string|"'key1'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'expected'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'properties'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'key1'"
op|':'
string|"'zz'"
comment|'# changed meta'
nl|'\n'
op|'}'
newline|'\n'
name|'quota_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'expected'
op|'['
string|'"properties"'
op|']'
op|')'
newline|'\n'
name|'update_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|','
name|'expected'
op|','
nl|'\n'
name|'data'
op|'='
name|'None'
op|','
name|'purge_props'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'expected_output'
op|'='
op|'{'
string|"'meta'"
op|':'
op|'{'
string|"'key1'"
op|':'
string|"'zz'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|','
name|'expected_output'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
string|"'100'"
op|')'
op|')'
newline|'\n'
DECL|member|test_update_item_image_not_found
name|'def'
name|'test_update_item_image_not_found'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|','
name|'quota_mocked'
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
string|"'/v2/fake/images/100/metadata/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"zz"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
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
name|'update'
op|','
name|'req'
op|','
string|"'100'"
op|','
string|"'key1'"
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'quota_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|')'
newline|'\n'
DECL|member|test_update_item_bad_body
name|'def'
name|'test_update_item_bad_body'
op|'('
name|'self'
op|','
name|'get_mocked'
op|','
name|'update_mocked'
op|','
nl|'\n'
name|'quota_mocked'
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
string|"'/v2/fake/images/123/metadata/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"key1"'
op|':'
string|'"zz"'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
string|"b''"
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'invalid_request'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
string|"'123'"
op|','
string|"'key1'"
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'get_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'quota_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'update_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
op|')'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|')'
newline|'\n'
DECL|member|test_update_item_too_many_keys
name|'def'
name|'test_update_item_too_many_keys'
op|'('
name|'self'
op|','
name|'get_mocked'
op|','
name|'update_mocked'
op|','
nl|'\n'
name|'_quota_mocked'
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
string|"'/v2/fake/images/123/metadata/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"foo"'
op|':'
string|'"bar"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
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
name|'update'
op|','
name|'req'
op|','
string|"'123'"
op|','
string|"'key1'"
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'get_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'update_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_update_item_body_uri_mismatch
name|'def'
name|'test_update_item_body_uri_mismatch'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|','
name|'update_mocked'
op|','
nl|'\n'
name|'quota_mocked'
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
string|"'/v2/fake/images/123/metadata/bad'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
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
name|'update'
op|','
name|'req'
op|','
string|"'123'"
op|','
string|"'bad'"
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'quota_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'update_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_delete
name|'def'
name|'test_delete'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|','
name|'update_mocked'
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
string|"'/v2/fake/images/123/metadata/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
name|'res'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'delete'
op|'('
name|'req'
op|','
string|"'123'"
op|','
string|"'key1'"
op|')'
newline|'\n'
name|'expected'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
name|'expected'
op|'['
string|"'properties'"
op|']'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'update_mocked'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
string|"'123'"
op|','
name|'expected'
op|','
nl|'\n'
name|'data'
op|'='
name|'None'
op|','
name|'purge_props'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_delete_not_found
name|'def'
name|'test_delete_not_found'
op|'('
name|'self'
op|','
name|'_get_mocked'
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
string|"'/v2/fake/images/123/metadata/blah'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
nl|'\n'
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
name|'req'
op|','
string|"'123'"
op|','
string|"'blah'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotFound'
op|'('
name|'image_id'
op|'='
string|"'100'"
op|')'
op|')'
newline|'\n'
DECL|member|test_delete_image_not_found
name|'def'
name|'test_delete_image_not_found'
op|'('
name|'self'
op|','
name|'_get_mocked'
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
string|"'/v2/fake/images/100/metadata/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'DELETE'"
newline|'\n'
nl|'\n'
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
name|'req'
op|','
string|"'100'"
op|','
string|"'key1'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
string|"''"
op|')'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_too_many_metadata_items_on_create
name|'def'
name|'test_too_many_metadata_items_on_create'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|','
nl|'\n'
name|'update_mocked'
op|','
name|'_quota_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"foo"'
op|':'
string|'"bar"'
op|'}'
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
string|"'/v2/fake/images/123/metadata'"
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
name|'dump_as_bytes'
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
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
string|"'123'"
op|','
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'update_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
name|'CHK_QUOTA_STR'
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|'('
name|'explanation'
op|'='
string|"''"
op|')'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.update'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
name|'return_value'
op|'='
name|'get_image_123'
op|'('
op|')'
op|')'
newline|'\n'
DECL|member|test_too_many_metadata_items_on_put
name|'def'
name|'test_too_many_metadata_items_on_put'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|','
nl|'\n'
name|'update_mocked'
op|','
name|'_quota_mocked'
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
string|"'/v2/fake/images/123/metadata/blah'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"blah"'
op|':'
string|'"blah"'
op|','
string|'"blah1"'
op|':'
string|'"blah1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'self'
op|'.'
name|'invalid_request'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
string|"'123'"
op|','
string|"'blah'"
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'update_mocked'
op|'.'
name|'called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotAuthorized'
op|'('
name|'image_id'
op|'='
string|"'123'"
op|')'
op|')'
newline|'\n'
DECL|member|test_image_not_authorized_update
name|'def'
name|'test_image_not_authorized_update'
op|'('
name|'self'
op|','
name|'_get_mocked'
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
string|"'/v2/fake/images/123/metadata/key1'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"meta"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
name|'req'
op|','
string|"'123'"
op|','
string|"'key1'"
op|','
nl|'\n'
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
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotAuthorized'
op|'('
name|'image_id'
op|'='
string|"'123'"
op|')'
op|')'
newline|'\n'
DECL|member|test_image_not_authorized_update_all
name|'def'
name|'test_image_not_authorized_update_all'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
number|'131'
newline|'\n'
comment|'# see nova.tests.unit.api.openstack.fakes:_make_image_fixtures'
nl|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/images/%s/metadata/key1'"
nl|'\n'
op|'%'
name|'image_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'PUT'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update_all'
op|','
name|'req'
op|','
name|'image_id'
op|','
nl|'\n'
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
op|'('
string|"'nova.image.api.API.get'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'exception'
op|'.'
name|'ImageNotAuthorized'
op|'('
name|'image_id'
op|'='
string|"'123'"
op|')'
op|')'
newline|'\n'
DECL|member|test_image_not_authorized_create
name|'def'
name|'test_image_not_authorized_create'
op|'('
name|'self'
op|','
name|'_get_mocked'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
number|'131'
newline|'\n'
comment|'# see nova.tests.unit.api.openstack.fakes:_make_image_fixtures'
nl|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/images/%s/metadata/key1'"
nl|'\n'
op|'%'
name|'image_id'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'body'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
string|'"key1"'
op|':'
string|'"value1"'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dump_as_bytes'
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
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
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
name|'image_id'
op|','
nl|'\n'
name|'body'
op|'='
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
