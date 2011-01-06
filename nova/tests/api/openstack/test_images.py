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
name|'logging'
newline|'\n'
name|'import'
name|'unittest'
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
name|'unittest'
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
name|'stubs'
op|'.'
name|'UnsetAll'
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
name|'unittest'
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
nl|'\n'
nl|'\n'
DECL|class|ImageControllerWithGlanceServiceTest
dedent|''
dedent|''
name|'class'
name|'ImageControllerWithGlanceServiceTest'
op|'('
name|'unittest'
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
comment|'# Registered images at start of each test.'
nl|'\n'
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
name|'auth_data'
op|'='
op|'{'
op|'}'
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
nl|'\n'
name|'fixture_index'
op|'='
op|'['
name|'dict'
op|'('
name|'id'
op|'='
name|'f'
op|'['
string|"'id'"
op|']'
op|','
name|'name'
op|'='
name|'f'
op|'['
string|"'name'"
op|']'
op|')'
name|'for'
name|'f'
nl|'\n'
name|'in'
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'image'
name|'in'
name|'res_dict'
op|'['
string|"'images'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
name|'fixture_index'
op|'.'
name|'count'
op|'('
name|'image'
op|')'
op|','
nl|'\n'
string|'"image %s not in fixture index!"'
op|'%'
name|'str'
op|'('
name|'image'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_image_details
dedent|''
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
nl|'\n'
DECL|function|_is_equivalent_subset
name|'def'
name|'_is_equivalent_subset'
op|'('
name|'x'
op|','
name|'y'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'set'
op|'('
name|'x'
op|')'
op|'<='
name|'set'
op|'('
name|'y'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'x'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'x'
op|'['
name|'k'
op|']'
op|'!='
name|'y'
op|'['
name|'k'
op|']'
op|':'
newline|'\n'
indent|'                        '
name|'if'
name|'x'
op|'['
name|'k'
op|']'
op|'=='
string|"'active'"
name|'and'
name|'y'
op|'['
name|'k'
op|']'
op|'=='
string|"'available'"
op|':'
newline|'\n'
indent|'                            '
name|'continue'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'image'
name|'in'
name|'res_dict'
op|'['
string|"'images'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'image_fixture'
name|'in'
name|'self'
op|'.'
name|'IMAGE_FIXTURES'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'_is_equivalent_subset'
op|'('
name|'image'
op|','
name|'image_fixture'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertEquals'
op|'('
number|'1'
op|','
number|'2'
op|','
string|'"image %s not in fixtures!"'
op|'%'
nl|'\n'
name|'str'
op|'('
name|'image'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
