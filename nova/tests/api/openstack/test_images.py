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
indent|'    '
string|'"""\n    Tasks to test for all image services.\n    """'
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
indent|'    '
string|'"""\n    Test of the OpenStack API /images application controller w/Glance.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|IMAGE_FIXTURES
name|'IMAGE_FIXTURES'
op|'='
op|'['
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'23g2ogk23k4hhkk4k42l'"
op|','
nl|'\n'
string|"'imageId'"
op|':'
string|"'23g2ogk23k4hhkk4k42l'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'public image #1'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'str'
op|'('
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'str'
op|'('
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
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
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'image_type'"
op|':'
string|"'kernel'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'id'"
op|':'
string|"'slkduhfas73kkaskgdas'"
op|','
nl|'\n'
string|"'imageId'"
op|':'
string|"'slkduhfas73kkaskgdas'"
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'public image #2'"
op|','
nl|'\n'
string|"'created_at'"
op|':'
name|'str'
op|'('
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|"'updated_at'"
op|':'
name|'str'
op|'('
name|'datetime'
op|'.'
name|'datetime'
op|'.'
name|'utcnow'
op|'('
op|')'
op|')'
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
string|"'is_public'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'status'"
op|':'
string|"'available'"
op|','
nl|'\n'
string|"'image_type'"
op|':'
string|"'ramdisk'"
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
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
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
name|'request'
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
name|'response'
op|'='
name|'request'
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
name|'response_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'response_list'
op|'='
name|'response_dict'
op|'['
string|'"images"'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'image'
name|'in'
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|':'
newline|'\n'
indent|'            '
name|'test_image'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image'
op|'['
string|'"id"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'image'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'test_image'
name|'in'
name|'response_list'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'response_list'
op|')'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_image_index_v1_1
dedent|''
name|'def'
name|'test_get_image_index_v1_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/images'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
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
name|'response_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'response_list'
op|'='
name|'response_dict'
op|'['
string|'"images"'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'image'
name|'in'
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|':'
newline|'\n'
indent|'            '
name|'href'
op|'='
string|'"http://localhost/v1.1/images/%s"'
op|'%'
name|'image'
op|'['
string|'"id"'
op|']'
newline|'\n'
name|'test_image'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image'
op|'['
string|'"id"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'image'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://localhost/v1.1/images/%s"'
op|'%'
name|'image'
op|'['
string|'"id"'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/xml"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'print'
name|'test_image'
newline|'\n'
name|'print'
newline|'\n'
name|'print'
name|'response_list'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'test_image'
name|'in'
name|'response_list'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'response_list'
op|')'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|')'
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
name|'request'
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
name|'response'
op|'='
name|'request'
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
name|'response_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'response_list'
op|'='
name|'response_dict'
op|'['
string|'"images"'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'image'
name|'in'
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|':'
newline|'\n'
indent|'            '
name|'test_image'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image'
op|'['
string|'"id"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'image'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
string|'"updated"'
op|':'
name|'image'
op|'['
string|'"updated_at"'
op|']'
op|','
nl|'\n'
string|'"created"'
op|':'
name|'image'
op|'['
string|'"created_at"'
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'image'
op|'['
string|'"status"'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'test_image'
name|'in'
name|'response_list'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'response_list'
op|')'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_image_details_v1_1
dedent|''
name|'def'
name|'test_get_image_details_v1_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/images/detail'"
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
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
name|'response_dict'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'response_list'
op|'='
name|'response_dict'
op|'['
string|'"images"'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'image'
name|'in'
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|':'
newline|'\n'
indent|'            '
name|'href'
op|'='
string|'"http://localhost/v1.1/images/%s"'
op|'%'
name|'image'
op|'['
string|'"id"'
op|']'
newline|'\n'
name|'test_image'
op|'='
op|'{'
nl|'\n'
string|'"id"'
op|':'
name|'image'
op|'['
string|'"id"'
op|']'
op|','
nl|'\n'
string|'"name"'
op|':'
name|'image'
op|'['
string|'"name"'
op|']'
op|','
nl|'\n'
string|'"updated"'
op|':'
name|'image'
op|'['
string|'"updated_at"'
op|']'
op|','
nl|'\n'
string|'"created"'
op|':'
name|'image'
op|'['
string|'"created_at"'
op|']'
op|','
nl|'\n'
string|'"status"'
op|':'
name|'image'
op|'['
string|'"status"'
op|']'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"self"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"bookmark"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/xml"'
op|','
nl|'\n'
string|'"href"'
op|':'
name|'href'
op|','
nl|'\n'
op|'}'
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'test_image'
name|'in'
name|'response_list'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'response_list'
op|')'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_image_create_empty
dedent|''
name|'def'
name|'test_get_image_create_empty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/images'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'response'
op|'='
name|'request'
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
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_image_create_bad_no_name
dedent|''
name|'def'
name|'test_get_image_create_bad_no_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/images'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'request'
op|'.'
name|'content_type'
op|'='
string|'"application/json"'
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
nl|'\n'
string|'"serverId"'
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
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
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_image_create_bad_no_id
dedent|''
name|'def'
name|'test_get_image_create_bad_no_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v1.1/images'"
op|')'
newline|'\n'
name|'request'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'request'
op|'.'
name|'content_type'
op|'='
string|'"application/json"'
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'{'
nl|'\n'
string|'"name"'
op|':'
string|'"Snapshot Test"'
op|','
nl|'\n'
op|'}'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
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
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
