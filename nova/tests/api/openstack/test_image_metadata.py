begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'json'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
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
name|'import'
name|'nova'
op|'.'
name|'wsgi'
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
DECL|class|ImageMetaDataTest
name|'class'
name|'ImageMetaDataTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|IMAGE_FIXTURES
indent|'    '
name|'IMAGE_FIXTURES'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'image1'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'container_format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'checksum'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created_at'"
op|':'
string|"'2011-03-22T17:40:15'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
string|"'2011-03-22T17:40:15'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'location'"
op|':'
string|"'file:///var/lib/glance/images/1'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'key1'"
op|':'
string|"'value1'"
op|','
nl|'\n'
string|"'key2'"
op|':'
string|"'value2'"
op|'}'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'5882349'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'image2'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'container_format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'checksum'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created_at'"
op|':'
string|"'2011-03-22T17:40:15'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
string|"'2011-03-22T17:40:15'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'location'"
op|':'
string|"'file:///var/lib/glance/images/2'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'key1'"
op|':'
string|"'value1'"
op|','
nl|'\n'
string|"'key2'"
op|':'
string|"'value2'"
op|'}'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'5882349'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'image3'"
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'container_format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'checksum'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created_at'"
op|':'
string|"'2011-03-22T17:40:15'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
string|"'2011-03-22T17:40:15'"
op|','
nl|'\n'
string|"'id'"
op|':'
string|"'3'"
op|','
nl|'\n'
string|"'location'"
op|':'
string|"'file:///var/lib/glance/images/2'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
op|'}'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'5882349'
op|'}'
op|','
nl|'\n'
op|']'
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
name|'ImageMetaDataTest'
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
name|'image_service'
op|'='
string|"'nova.image.glance.GlanceImageService'"
op|')'
newline|'\n'
comment|'# NOTE(dprince) max out properties/metadata in image 3 for testing'
nl|'\n'
name|'img3'
op|'='
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|'['
number|'2'
op|']'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'img3'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'key%i'"
op|'%'
name|'num'
op|']'
op|'='
string|'"blah"'
newline|'\n'
dedent|''
name|'fakes'
op|'.'
name|'stub_out_glance'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index
dedent|''
name|'def'
name|'test_index'
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
string|"'/v1.1/123/images/1/metadata'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'expected'
op|'='
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|'['
number|'0'
op|']'
op|'['
string|"'properties'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'expected'
op|')'
op|','
name|'len'
op|'('
name|'res_dict'
op|'['
string|"'metadata'"
op|']'
op|')'
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'res_dict'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'value'
op|','
name|'res_dict'
op|'['
string|"'metadata'"
op|']'
op|'['
name|'key'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show
dedent|''
dedent|''
name|'def'
name|'test_show'
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
string|"'/v1.1/fake/images/1/metadata/key1'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'meta'"
name|'in'
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
nl|'\n'
DECL|member|test_show_not_found
dedent|''
name|'def'
name|'test_show_not_found'
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
string|"'/v1.1/fake/images/1/metadata/key9'"
op|')'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create
dedent|''
name|'def'
name|'test_create'
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
string|"'/v1.1/fake/images/2/metadata'"
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
string|'\'{"metadata": {"key9": "value9"}}\''
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'actual_output'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'expected_output'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'key1'"
op|':'
string|"'value1'"
op|','
nl|'\n'
string|"'key2'"
op|':'
string|"'value2'"
op|','
nl|'\n'
string|"'key9'"
op|':'
string|"'value9'"
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
name|'assertEqual'
op|'('
name|'expected_output'
op|','
name|'actual_output'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_all
dedent|''
name|'def'
name|'test_update_all'
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
string|"'/v1.1/fake/images/1/metadata'"
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
name|'body'
op|'='
string|'\'{"metadata": {"key9": "value9"}}\''
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'actual_output'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'expected_output'
op|'='
op|'{'
nl|'\n'
string|"'metadata'"
op|':'
op|'{'
nl|'\n'
string|"'key9'"
op|':'
string|"'value9'"
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
name|'assertEqual'
op|'('
name|'expected_output'
op|','
name|'actual_output'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item
dedent|''
name|'def'
name|'test_update_item'
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
string|"'/v1.1/fake/images/1/metadata/key1'"
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
name|'body'
op|'='
string|'\'{"meta": {"key1": "zz"}}\''
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'actual_output'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected_output'
op|'='
op|'{'
nl|'\n'
string|"'meta'"
op|':'
op|'{'
nl|'\n'
string|"'key1'"
op|':'
string|"'zz'"
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
name|'actual_output'
op|','
name|'expected_output'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_bad_body
dedent|''
name|'def'
name|'test_update_item_bad_body'
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
string|"'/v1.1/fake/images/1/metadata/key1'"
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
name|'body'
op|'='
string|'\'{"key1": "zz"}\''
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_too_many_keys
dedent|''
name|'def'
name|'test_update_item_too_many_keys'
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
string|"'/v1.1/fake/images/1/metadata/key1'"
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
name|'body'
op|'='
string|'\'{"meta": {"key1": "value1", "key2": "value2"}}\''
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_body_uri_mismatch
dedent|''
name|'def'
name|'test_update_item_body_uri_mismatch'
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
string|"'/v1.1/fake/images/1/metadata/bad'"
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
name|'body'
op|'='
string|'\'{"meta": {"key1": "value1"}}\''
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'400'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_update_item_xml
dedent|''
name|'def'
name|'test_update_item_xml'
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
string|"'/v1.1/fake/images/1/metadata/key1'"
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
name|'body'
op|'='
string|'\'<meta key="key1">five</meta>\''
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/xml"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'actual_output'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'expected_output'
op|'='
op|'{'
nl|'\n'
string|"'meta'"
op|':'
op|'{'
nl|'\n'
string|"'key1'"
op|':'
string|"'five'"
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
name|'actual_output'
op|','
name|'expected_output'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete
dedent|''
name|'def'
name|'test_delete'
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
string|"'/v1.1/fake/images/2/metadata/key1'"
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'204'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_not_found
dedent|''
name|'def'
name|'test_delete_not_found'
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
string|"'/v1.1/fake/images/2/metadata/blah'"
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_metadata_items_on_create
dedent|''
name|'def'
name|'test_too_many_metadata_items_on_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'data'
op|'='
op|'{'
string|'"metadata"'
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'for'
name|'num'
name|'in'
name|'range'
op|'('
name|'FLAGS'
op|'.'
name|'quota_metadata_items'
op|'+'
number|'1'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'metadata'"
op|']'
op|'['
string|"'key%i'"
op|'%'
name|'num'
op|']'
op|'='
string|'"blah"'
newline|'\n'
dedent|''
name|'json_string'
op|'='
name|'str'
op|'('
name|'data'
op|')'
op|'.'
name|'replace'
op|'('
string|'"\\\'"'
op|','
string|'"\\""'
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
string|"'/v1.1/fake/images/2/metadata'"
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
name|'json_string'
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'413'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_too_many_metadata_items_on_put
dedent|''
name|'def'
name|'test_too_many_metadata_items_on_put'
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
string|"'/v1.1/fake/images/3/metadata/blah'"
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
name|'body'
op|'='
string|'\'{"meta": {"blah": "blah"}}\''
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
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'413'
op|','
name|'res'
op|'.'
name|'status_int'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
