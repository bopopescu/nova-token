begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Openstack LLC.'
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
nl|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
nl|'\n'
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
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'image'
name|'import'
name|'glance'
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
name|'glance'
name|'import'
name|'stubs'
name|'as'
name|'glance_stubs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NullWriter
name|'class'
name|'NullWriter'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Used to test ImageService.get which takes a writer object"""'
newline|'\n'
nl|'\n'
DECL|member|write
name|'def'
name|'write'
op|'('
name|'self'
op|','
op|'*'
name|'arg'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestGlanceSerializer
dedent|''
dedent|''
name|'class'
name|'TestGlanceSerializer'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_serialize
indent|'    '
name|'def'
name|'test_serialize'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'image1'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'foo'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'prop1'"
op|':'
string|"'propvalue1'"
op|','
nl|'\n'
string|"'mappings'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'aaa'"
op|','
nl|'\n'
string|"'device'"
op|':'
string|"'bbb'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual'"
op|':'
string|"'xxx'"
op|','
nl|'\n'
string|"'device'"
op|':'
string|"'yyy'"
op|'}'
op|']'
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'virtual_device'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/fake'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'virtual_device'"
op|':'
string|"'ephemeral0'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/fake0'"
op|'}'
op|']'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'converted_expected'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
string|"'image1'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'foo'"
op|':'
string|"'bar'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'prop1'"
op|':'
string|"'propvalue1'"
op|','
nl|'\n'
string|"'mappings'"
op|':'
nl|'\n'
string|'\'[{"device": "bbb", "virtual": "aaa"}, \''
nl|'\n'
string|'\'{"device": "yyy", "virtual": "xxx"}]\''
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
nl|'\n'
string|'\'[{"virtual_device": "fake", "device_name": "/dev/fake"}, \''
nl|'\n'
string|'\'{"virtual_device": "ephemeral0", \''
nl|'\n'
string|'\'"device_name": "/dev/fake0"}]\''
op|'}'
op|'}'
newline|'\n'
name|'converted'
op|'='
name|'glance'
op|'.'
name|'_convert_to_string'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'converted'
op|','
name|'converted_expected'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'glance'
op|'.'
name|'_convert_from_string'
op|'('
name|'converted'
op|')'
op|','
name|'metadata'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestGlanceImageService
dedent|''
dedent|''
name|'class'
name|'TestGlanceImageService'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Tests the Glance image service.\n\n    At a high level, the translations involved are:\n\n        1. Glance -> ImageService - This is needed so we can support\n           multple ImageServices (Glance, Local, etc)\n\n        2. ImageService -> API - This is needed so we can support multple\n           APIs (OpenStack, EC2)\n\n    """'
newline|'\n'
DECL|variable|NOW_GLANCE_OLD_FORMAT
name|'NOW_GLANCE_OLD_FORMAT'
op|'='
string|'"2010-10-11T10:30:22"'
newline|'\n'
DECL|variable|NOW_GLANCE_FORMAT
name|'NOW_GLANCE_FORMAT'
op|'='
string|'"2010-10-11T10:30:22.000000"'
newline|'\n'
DECL|variable|NOW_DATETIME
name|'NOW_DATETIME'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2010'
op|','
number|'10'
op|','
number|'11'
op|','
number|'10'
op|','
number|'30'
op|','
number|'22'
op|')'
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
name|'TestGlanceImageService'
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
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_compute_api_snapshot'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'client'
op|'='
name|'glance_stubs'
op|'.'
name|'StubGlanceClient'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'='
name|'glance'
op|'.'
name|'GlanceImageService'
op|'('
name|'client'
op|'='
name|'client'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|','
name|'auth_token'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'delete_all'
op|'('
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
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'UnsetAll'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'TestGlanceImageService'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_make_fixture
name|'def'
name|'_make_fixture'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
op|'{'
string|"'name'"
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
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'fixture'
op|'.'
name|'update'
op|'('
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'fixture'
newline|'\n'
nl|'\n'
DECL|member|_make_datetime_fixture
dedent|''
name|'def'
name|'_make_datetime_fixture'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'created_at'
op|'='
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
name|'updated_at'
op|'='
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|','
nl|'\n'
name|'deleted_at'
op|'='
name|'self'
op|'.'
name|'NOW_GLANCE_FORMAT'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_with_instance_id
dedent|''
name|'def'
name|'test_create_with_instance_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Ensure instance_id is persisted as an image-property"""'
newline|'\n'
name|'fixture'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'test image'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'instance_id'"
op|':'
string|"'42'"
op|','
string|"'user_id'"
op|':'
string|"'fake'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'test image'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'location'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
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
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
string|"'instance_id'"
op|':'
string|"'42'"
op|','
string|"'user_id'"
op|':'
string|"'fake'"
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'image_meta'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'image_metas'
op|'['
number|'0'
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_without_instance_id
dedent|''
name|'def'
name|'test_create_without_instance_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Ensure we can create an image without having to specify an\n        instance_id. Public images are an example of an image not tied to an\n        instance.\n        """'
newline|'\n'
name|'fixture'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'test image'"
op|','
string|"'is_public'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'test image'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'location'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
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
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
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
op|'}'
newline|'\n'
name|'actual'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'actual'
op|','
name|'expected'
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
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'test image'"
op|')'
newline|'\n'
name|'num_images'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertNotEquals'
op|'('
name|'None'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'num_images'
op|'+'
number|'1'
op|','
nl|'\n'
name|'len'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_show_non_existing_image
dedent|''
name|'def'
name|'test_create_and_show_non_existing_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'test image'"
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertNotEquals'
op|'('
name|'None'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'bad image id'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_and_show_non_existing_image_by_name
dedent|''
name|'def'
name|'test_create_and_show_non_existing_image_by_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'test image'"
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertNotEquals'
op|'('
name|'None'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ImageNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'show_by_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'bad image id'"
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
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'test image'"
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
name|'image_id'
op|','
string|"'name'"
op|':'
string|"'test image'"
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertDictListMatch'
op|'('
name|'image_metas'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_default_limit
dedent|''
name|'def'
name|'test_index_default_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'ids'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'i'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'expected'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'meta'
op|','
name|'expected'
op|')'
newline|'\n'
name|'i'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|test_index_marker
dedent|''
dedent|''
name|'def'
name|'test_index_marker'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'ids'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'marker'
op|'='
name|'ids'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'image_metas'
op|')'
op|','
number|'8'
op|')'
newline|'\n'
name|'i'
op|'='
number|'2'
newline|'\n'
name|'for'
name|'meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'expected'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'DONTCARE'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'meta'
op|','
name|'expected'
op|')'
newline|'\n'
name|'i'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|test_index_limit
dedent|''
dedent|''
name|'def'
name|'test_index_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'ids'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'limit'
op|'='
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'image_metas'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_index_marker_and_limit
dedent|''
name|'def'
name|'test_index_marker_and_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'ids'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'marker'
op|'='
name|'ids'
op|'['
number|'3'
op|']'
op|','
name|'limit'
op|'='
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'image_metas'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'i'
op|'='
number|'4'
newline|'\n'
name|'for'
name|'meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'expected'
op|'='
op|'{'
string|"'id'"
op|':'
name|'ids'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'meta'
op|','
name|'expected'
op|')'
newline|'\n'
name|'i'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|test_detail_marker
dedent|''
dedent|''
name|'def'
name|'test_detail_marker'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'ids'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'marker'
op|'='
name|'ids'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'image_metas'
op|')'
op|','
number|'8'
op|')'
newline|'\n'
name|'i'
op|'='
number|'2'
newline|'\n'
name|'for'
name|'meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'ids'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
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
name|'None'
op|','
nl|'\n'
string|"'location'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
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
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'meta'
op|','
name|'expected'
op|')'
newline|'\n'
name|'i'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|test_detail_limit
dedent|''
dedent|''
name|'def'
name|'test_detail_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'ids'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'limit'
op|'='
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'image_metas'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_marker_and_limit
dedent|''
name|'def'
name|'test_detail_marker_and_limit'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'10'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
op|')'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'fixture'
op|')'
newline|'\n'
name|'ids'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'marker'
op|'='
name|'ids'
op|'['
number|'3'
op|']'
op|','
name|'limit'
op|'='
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'len'
op|'('
name|'image_metas'
op|')'
op|','
number|'5'
op|')'
newline|'\n'
name|'i'
op|'='
number|'4'
newline|'\n'
name|'for'
name|'meta'
name|'in'
name|'image_metas'
op|':'
newline|'\n'
indent|'            '
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'ids'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'TestImage %d'"
op|'%'
op|'('
name|'i'
op|')'
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
name|'None'
op|','
nl|'\n'
string|"'location'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
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
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'meta'
op|','
name|'expected'
op|')'
newline|'\n'
name|'i'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
DECL|member|test_update
dedent|''
dedent|''
name|'def'
name|'test_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'test image'"
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'fixture'
op|'['
string|"'name'"
op|']'
op|'='
string|"'new image name'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'update'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image_id'
op|','
name|'fixture'
op|')'
newline|'\n'
nl|'\n'
name|'new_image_data'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'new image name'"
op|','
name|'new_image_data'
op|'['
string|"'name'"
op|']'
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
name|'fixture1'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'test image 1'"
op|')'
newline|'\n'
name|'fixture2'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'test image 2'"
op|')'
newline|'\n'
name|'fixtures'
op|'='
op|'['
name|'fixture1'
op|','
name|'fixture2'
op|']'
newline|'\n'
nl|'\n'
name|'num_images'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'0'
op|','
name|'num_images'
op|','
name|'str'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'ids'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'fixture'
name|'in'
name|'fixtures'
op|':'
newline|'\n'
indent|'            '
name|'new_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'ids'
op|'.'
name|'append'
op|'('
name|'new_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'num_images'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'2'
op|','
name|'num_images'
op|','
name|'str'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'delete'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'ids'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'num_images'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'service'
op|'.'
name|'index'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'num_images'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_passes_through_to_client
dedent|''
name|'def'
name|'test_show_passes_through_to_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'image1'"
op|','
name|'is_public'
op|'='
name|'True'
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'image1'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'location'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
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
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
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
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_raises_when_no_authtoken_in_the_context
dedent|''
name|'def'
name|'test_show_raises_when_no_authtoken_in_the_context'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'image1'"
op|','
nl|'\n'
name|'is_public'
op|'='
name|'False'
op|','
nl|'\n'
name|'properties'
op|'='
op|'{'
string|"'one'"
op|':'
string|"'two'"
op|'}'
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'auth_token'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'ImageNotFound'
op|','
nl|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_passes_through_to_client
dedent|''
name|'def'
name|'test_detail_passes_through_to_client'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_fixture'
op|'('
name|'name'
op|'='
string|"'image10'"
op|','
name|'is_public'
op|'='
name|'True'
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'image_metas'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'expected'
op|'='
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'image_id'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'image10'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'size'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'location'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'None'
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
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'self'
op|'.'
name|'NOW_DATETIME'
op|','
nl|'\n'
string|"'deleted_at'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'deleted'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
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
op|'}'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_metas'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_show_makes_datetimes
dedent|''
name|'def'
name|'test_show_makes_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_datetime_fixture'
op|'('
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'show'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'created_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'updated_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detail_makes_datetimes
dedent|''
name|'def'
name|'test_detail_makes_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_datetime_fixture'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'detail'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'created_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'updated_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_makes_datetimes
dedent|''
name|'def'
name|'test_get_makes_datetimes'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixture'
op|'='
name|'self'
op|'.'
name|'_make_datetime_fixture'
op|'('
op|')'
newline|'\n'
name|'image_id'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'fixture'
op|')'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'writer'
op|'='
name|'NullWriter'
op|'('
op|')'
newline|'\n'
name|'image_meta'
op|'='
name|'self'
op|'.'
name|'service'
op|'.'
name|'get'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'image_id'
op|','
name|'writer'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'created_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_meta'
op|'['
string|"'updated_at'"
op|']'
op|','
name|'self'
op|'.'
name|'NOW_DATETIME'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
