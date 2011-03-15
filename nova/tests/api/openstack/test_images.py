begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
string|'"""\nTests of the new image services, both as a service layer,\nand as a WSGI layer\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'glance'
name|'import'
name|'client'
name|'as'
name|'glance_client'
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
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'images'
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
DECL|class|BaseImageServiceTests
name|'class'
name|'BaseImageServiceTests'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Tasks to test for all image services"""'
newline|'\n'
nl|'\n'
DECL|member|test_create
name|'def'
name|'test_create'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'fixture'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'test image'"
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'progress'"
op|':'
name|'None'
op|'}'
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
nl|'\n'
name|'id'
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
name|'id'
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
nl|'\n'
indent|'        '
name|'fixture'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'test image'"
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'progress'"
op|':'
name|'None'
op|'}'
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
nl|'\n'
name|'id'
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
name|'id'
op|')'
newline|'\n'
nl|'\n'
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
DECL|member|test_update
dedent|''
name|'def'
name|'test_update'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'fixture'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'test image'"
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'progress'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
name|'id'
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
name|'fixture'
op|'['
string|"'status'"
op|']'
op|'='
string|"'in progress'"
newline|'\n'
nl|'\n'
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
name|'id'
op|','
name|'fixture'
op|')'
newline|'\n'
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
name|'id'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|"'in progress'"
op|','
name|'new_image_data'
op|'['
string|"'status'"
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
nl|'\n'
indent|'        '
name|'fixtures'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'test image 1'"
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'progress'"
op|':'
name|'None'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'name'"
op|':'
string|"'test image 2'"
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'instance_id'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'progress'"
op|':'
name|'None'
op|'}'
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
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'LocalImageServiceTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|','
nl|'\n'
DECL|class|LocalImageServiceTest
name|'BaseImageServiceTests'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Tests the local image service"""'
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
name|'LocalImageServiceTest'
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
name|'tempdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'images_path'
op|'='
name|'self'
op|'.'
name|'tempdir'
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
name|'service_class'
op|'='
string|"'nova.image.local.LocalImageService'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'service_class'
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
name|'None'
op|','
name|'None'
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
name|'shutil'
op|'.'
name|'rmtree'
op|'('
name|'self'
op|'.'
name|'tempdir'
op|')'
newline|'\n'
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
name|'LocalImageServiceTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'class'
name|'GlanceImageServiceTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|','
nl|'\n'
DECL|class|GlanceImageServiceTest
name|'BaseImageServiceTests'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Tests the Glance image service, in particular that metadata translation\n    works properly.\n\n    At a high level, the translations involved are:\n\n        1. Glance -> ImageService - This is needed so we can support\n           multple ImageServices (Glance, Local, etc)\n\n        2. ImageService -> API - This is needed so we can support multple\n           APIs (OpenStack, EC2)\n    """'
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
name|'GlanceImageServiceTest'
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
name|'stub_out_glance'
op|'('
name|'self'
op|'.'
name|'stubs'
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
name|'service_class'
op|'='
string|"'nova.image.glance.GlanceImageService'"
newline|'\n'
name|'self'
op|'.'
name|'service'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'service_class'
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
name|'None'
op|','
name|'None'
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
name|'self'
op|'.'
name|'sent_to_glance'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_glance_add_image'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'self'
op|'.'
name|'sent_to_glance'
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
name|'GlanceImageServiceTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
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
string|'"""\n        Ensure that a instance_id is stored in Glance as a image property\n        string and then converted back to an instance_id integer attribute.\n        """'
newline|'\n'
name|'fixture'
op|'='
op|'{'
string|"'instance_id'"
op|':'
number|'42'
op|','
string|"'name'"
op|':'
string|"'test image'"
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
string|"'properties'"
op|':'
op|'{'
string|"'instance_id'"
op|':'
string|"'42'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'self'
op|'.'
name|'sent_to_glance'
op|'['
string|"'metadata'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
comment|"# The ImageService shouldn't leak the fact that the instance_id"
nl|'\n'
comment|'# happens to be stored as a property in Glance'
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'id'"
op|':'
name|'image_id'
op|','
string|"'instance_id'"
op|':'
number|'42'
op|','
string|"'name'"
op|':'
string|"'test image'"
op|'}'
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
string|"'id'"
op|':'
name|'image_id'
op|','
string|"'name'"
op|':'
string|"'test image'"
op|','
string|"'properties'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertDictMatch'
op|'('
name|'self'
op|'.'
name|'sent_to_glance'
op|'['
string|"'metadata'"
op|']'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageControllerWithGlanceServiceTest
dedent|''
dedent|''
name|'class'
name|'ImageControllerWithGlanceServiceTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""Test of the OpenStack API /images application controller"""'
newline|'\n'
nl|'\n'
comment|'# FIXME(sirp): The ImageService and API use two different formats for'
nl|'\n'
comment|'# timestamps. Ultimately, the ImageService should probably use datetime'
nl|'\n'
comment|'# objects'
nl|'\n'
DECL|variable|NOW_SERVICE_STR
name|'NOW_SERVICE_STR'
op|'='
string|'"2010-10-11T10:30:22"'
newline|'\n'
DECL|variable|NOW_API_STR
name|'NOW_API_STR'
op|'='
string|'"2010-10-11T10:30:22Z"'
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
name|'ImageControllerWithGlanceServiceTest'
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
name|'orig_image_service'
op|'='
name|'FLAGS'
op|'.'
name|'image_service'
newline|'\n'
name|'FLAGS'
op|'.'
name|'image_service'
op|'='
string|"'nova.image.glance.GlanceImageService'"
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
name|'FakeAuthManager'
op|'.'
name|'reset_fake_data'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
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
name|'fakes'
op|'.'
name|'stub_out_auth'
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
name|'fixtures'
op|'='
name|'self'
op|'.'
name|'_make_image_fixtures'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_glance'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'initial_fixtures'
op|'='
name|'fixtures'
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
name|'FLAGS'
op|'.'
name|'image_service'
op|'='
name|'self'
op|'.'
name|'orig_image_service'
newline|'\n'
name|'super'
op|'('
name|'ImageControllerWithGlanceServiceTest'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_image_index
dedent|''
name|'def'
name|'test_get_image_index'
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
string|"'/v1.0/images'"
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
name|'image_metas'
op|'='
name|'json'
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
name|'expected'
op|'='
op|'['
op|'{'
string|"'id'"
op|':'
number|'123'
op|','
string|"'name'"
op|':'
string|"'public image'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'124'
op|','
string|"'name'"
op|':'
string|"'queued backup'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'125'
op|','
string|"'name'"
op|':'
string|"'saving backup'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'126'
op|','
string|"'name'"
op|':'
string|"'active backup'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'127'
op|','
string|"'name'"
op|':'
string|"'killed backup'"
op|'}'
op|']'
newline|'\n'
nl|'\n'
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
DECL|member|test_get_image_details
dedent|''
name|'def'
name|'test_get_image_details'
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
string|"'/v1.0/images/detail'"
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
name|'image_metas'
op|'='
name|'json'
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
name|'expected'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'123'
op|','
string|"'name'"
op|':'
string|"'public image'"
op|','
string|"'updated'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
nl|'\n'
string|"'created'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
string|"'status'"
op|':'
string|"'ACTIVE'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'124'
op|','
string|"'name'"
op|':'
string|"'queued backup'"
op|','
string|"'serverId'"
op|':'
number|'42'
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
string|"'created'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'QUEUED'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'125'
op|','
string|"'name'"
op|':'
string|"'saving backup'"
op|','
string|"'serverId'"
op|':'
number|'42'
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
string|"'created'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'SAVING'"
op|','
string|"'progress'"
op|':'
number|'0'
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'126'
op|','
string|"'name'"
op|':'
string|"'active backup'"
op|','
string|"'serverId'"
op|':'
number|'42'
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
string|"'created'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'ACTIVE'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
number|'127'
op|','
string|"'name'"
op|':'
string|"'killed backup'"
op|','
string|"'serverId'"
op|':'
number|'42'
op|','
nl|'\n'
string|"'updated'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
string|"'created'"
op|':'
name|'self'
op|'.'
name|'NOW_API_STR'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'FAILED'"
op|'}'
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
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
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_make_image_fixtures
name|'def'
name|'_make_image_fixtures'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        """'
newline|'\n'
name|'fixtures'
op|'='
op|'['
op|']'
newline|'\n'
name|'public_image'
op|'='
op|'{'
string|"'id'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'public image'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|'}'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'public_image'
op|')'
newline|'\n'
nl|'\n'
name|'queued_backup'
op|'='
op|'{'
string|"'id'"
op|':'
number|'124'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'queued backup'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'queued'"
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'42'
op|'}'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'queued_backup'
op|')'
newline|'\n'
nl|'\n'
name|'saving_backup'
op|'='
op|'{'
string|"'id'"
op|':'
number|'125'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'saving backup'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'saving'"
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'42'
op|','
nl|'\n'
string|"'progress'"
op|':'
number|'0'
op|'}'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'saving_backup'
op|')'
newline|'\n'
nl|'\n'
name|'active_backup'
op|'='
op|'{'
string|"'id'"
op|':'
number|'126'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'active backup'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'active'"
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'42'
op|'}'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'active_backup'
op|')'
newline|'\n'
nl|'\n'
name|'killed_backup'
op|'='
op|'{'
string|"'id'"
op|':'
number|'127'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'killed backup'"
op|','
nl|'\n'
string|"'is_public'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'killed'"
op|','
nl|'\n'
string|"'instance_id'"
op|':'
number|'42'
op|'}'
newline|'\n'
name|'fixtures'
op|'.'
name|'append'
op|'('
name|'killed_backup'
op|')'
newline|'\n'
nl|'\n'
name|'base_attrs'
op|'='
op|'{'
string|"'created_at'"
op|':'
name|'cls'
op|'.'
name|'NOW_SERVICE_STR'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'cls'
op|'.'
name|'NOW_SERVICE_STR'
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
op|'}'
newline|'\n'
nl|'\n'
name|'for'
name|'fixture'
name|'in'
name|'fixtures'
op|':'
newline|'\n'
indent|'            '
name|'fixture'
op|'.'
name|'update'
op|'('
name|'base_attrs'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'fixtures'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
