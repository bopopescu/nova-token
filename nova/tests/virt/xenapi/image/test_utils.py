begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'tarfile'
newline|'\n'
nl|'\n'
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
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'image'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|GlanceImageTestCase
name|'class'
name|'GlanceImageTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_get_image
indent|'    '
name|'def'
name|'_get_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'utils'
op|'.'
name|'GlanceImage'
op|'('
string|"'context'"
op|','
string|"'href'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_out_glance_services
dedent|''
name|'def'
name|'_stub_out_glance_services'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_service'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'glance'
op|'.'
name|'GlanceImageService'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|'.'
name|'glance'
op|','
string|"'get_remote_image_service'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'glance'
op|'.'
name|'get_remote_image_service'
op|'('
string|"'context'"
op|','
string|"'href'"
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
op|'('
name|'image_service'
op|','
string|"'id'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'image_service'
newline|'\n'
nl|'\n'
DECL|member|test__image_id
dedent|''
name|'def'
name|'test__image_id'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_stub_out_glance_services'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'id'"
op|','
name|'image'
op|'.'
name|'_image_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__image_service
dedent|''
name|'def'
name|'test__image_service'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_service'
op|'='
name|'self'
op|'.'
name|'_stub_out_glance_services'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_service'
op|','
name|'image'
op|'.'
name|'_image_service'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_meta
dedent|''
name|'def'
name|'test_meta'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_service'
op|'='
name|'self'
op|'.'
name|'_stub_out_glance_services'
op|'('
op|')'
newline|'\n'
name|'image_service'
op|'.'
name|'show'
op|'('
string|"'context'"
op|','
string|"'id'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'metadata'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'metadata'"
op|','
name|'image'
op|'.'
name|'meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_meta_caching
dedent|''
name|'def'
name|'test_meta_caching'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_stub_out_glance_services'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
op|')'
newline|'\n'
name|'image'
op|'.'
name|'_cached_meta'
op|'='
string|"'metadata'"
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'metadata'"
op|','
name|'image'
op|'.'
name|'meta'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_download_to
dedent|''
name|'def'
name|'test_download_to'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_service'
op|'='
name|'self'
op|'.'
name|'_stub_out_glance_services'
op|'('
op|')'
newline|'\n'
name|'image_service'
op|'.'
name|'download'
op|'('
string|"'context'"
op|','
string|"'id'"
op|','
string|"'fobj'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'result'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'result'"
op|','
name|'image'
op|'.'
name|'download_to'
op|'('
string|"'fobj'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_raw_tgz_empty_meta
dedent|''
name|'def'
name|'test_is_raw_tgz_empty_meta'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_stub_out_glance_services'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
op|')'
newline|'\n'
name|'image'
op|'.'
name|'_cached_meta'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'False'
op|','
name|'image'
op|'.'
name|'is_raw_tgz'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_is_raw_tgz_for_raw_tgz
dedent|''
name|'def'
name|'test_is_raw_tgz_for_raw_tgz'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_stub_out_glance_services'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
op|')'
newline|'\n'
name|'image'
op|'.'
name|'_cached_meta'
op|'='
op|'{'
string|"'disk_format'"
op|':'
string|"'raw'"
op|','
string|"'container_format'"
op|':'
string|"'tgz'"
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'True'
op|','
name|'image'
op|'.'
name|'is_raw_tgz'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_data
dedent|''
name|'def'
name|'test_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_service'
op|'='
name|'self'
op|'.'
name|'_stub_out_glance_services'
op|'('
op|')'
newline|'\n'
name|'image_service'
op|'.'
name|'download'
op|'('
string|"'context'"
op|','
string|"'id'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'data'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'self'
op|'.'
name|'_get_image'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'data'"
op|','
name|'image'
op|'.'
name|'data'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RawImageTestCase
dedent|''
dedent|''
name|'class'
name|'RawImageTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_size
indent|'    '
name|'def'
name|'test_get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'glance_image'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'utils'
op|'.'
name|'GlanceImage'
op|')'
newline|'\n'
name|'glance_image'
op|'.'
name|'meta'
op|'='
op|'{'
string|"'size'"
op|':'
string|"'123'"
op|'}'
newline|'\n'
name|'raw_image'
op|'='
name|'utils'
op|'.'
name|'RawImage'
op|'('
name|'glance_image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'123'
op|','
name|'raw_image'
op|'.'
name|'get_size'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stream_to
dedent|''
name|'def'
name|'test_stream_to'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'glance_image'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'utils'
op|'.'
name|'GlanceImage'
op|')'
newline|'\n'
name|'glance_image'
op|'.'
name|'download_to'
op|'('
string|"'file'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'result'"
op|')'
newline|'\n'
name|'raw_image'
op|'='
name|'utils'
op|'.'
name|'RawImage'
op|'('
name|'glance_image'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'result'"
op|','
name|'raw_image'
op|'.'
name|'stream_to'
op|'('
string|"'file'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestIterableBasedFile
dedent|''
dedent|''
name|'class'
name|'TestIterableBasedFile'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_constructor
indent|'    '
name|'def'
name|'test_constructor'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|FakeIterable
indent|'        '
name|'class'
name|'FakeIterable'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__iter__
indent|'            '
name|'def'
name|'__iter__'
op|'('
name|'_self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'iterator'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'the_file'
op|'='
name|'utils'
op|'.'
name|'IterableToFileAdapter'
op|'('
name|'FakeIterable'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'iterator'"
op|','
name|'the_file'
op|'.'
name|'iterator'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_read_one_character
dedent|''
name|'def'
name|'test_read_one_character'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'the_file'
op|'='
name|'utils'
op|'.'
name|'IterableToFileAdapter'
op|'('
op|'['
nl|'\n'
string|"'chunk1'"
op|','
string|"'chunk2'"
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'c'"
op|','
name|'the_file'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_read_stores_remaining_characters
dedent|''
name|'def'
name|'test_read_stores_remaining_characters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'the_file'
op|'='
name|'utils'
op|'.'
name|'IterableToFileAdapter'
op|'('
op|'['
nl|'\n'
string|"'chunk1'"
op|','
string|"'chunk2'"
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'the_file'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'hunk1'"
op|','
name|'the_file'
op|'.'
name|'remaining_data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_read_remaining_characters
dedent|''
name|'def'
name|'test_read_remaining_characters'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'the_file'
op|'='
name|'utils'
op|'.'
name|'IterableToFileAdapter'
op|'('
op|'['
nl|'\n'
string|"'chunk1'"
op|','
string|"'chunk2'"
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'c'"
op|','
name|'the_file'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'h'"
op|','
name|'the_file'
op|'.'
name|'read'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_read_reached_end_of_file
dedent|''
name|'def'
name|'test_read_reached_end_of_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'the_file'
op|'='
name|'utils'
op|'.'
name|'IterableToFileAdapter'
op|'('
op|'['
nl|'\n'
string|"'chunk1'"
op|','
string|"'chunk2'"
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'chunk1'"
op|','
name|'the_file'
op|'.'
name|'read'
op|'('
number|'100'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'chunk2'"
op|','
name|'the_file'
op|'.'
name|'read'
op|'('
number|'100'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'the_file'
op|'.'
name|'read'
op|'('
number|'100'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_empty_chunks
dedent|''
name|'def'
name|'test_empty_chunks'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'the_file'
op|'='
name|'utils'
op|'.'
name|'IterableToFileAdapter'
op|'('
op|'['
nl|'\n'
string|"''"
op|','
string|"''"
op|','
string|"'chunk2'"
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'chunk2'"
op|','
name|'the_file'
op|'.'
name|'read'
op|'('
number|'100'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RawTGZTestCase
dedent|''
dedent|''
name|'class'
name|'RawTGZTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_as_tarfile
indent|'    '
name|'def'
name|'test_as_tarfile'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
name|'utils'
op|'.'
name|'RawTGZImage'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'image'
op|','
string|"'_as_file'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|'.'
name|'tarfile'
op|','
string|"'open'"
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'.'
name|'_as_file'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'the_file'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'tarfile'
op|'.'
name|'open'
op|'('
name|'mode'
op|'='
string|"'r|gz'"
op|','
name|'fileobj'
op|'='
string|"'the_file'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'tf'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'image'
op|'.'
name|'_as_tarfile'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'tf'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_as_file
dedent|''
name|'def'
name|'test_as_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'IterableToFileAdapter'"
op|')'
newline|'\n'
name|'glance_image'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'utils'
op|'.'
name|'GlanceImage'
op|')'
newline|'\n'
name|'image'
op|'='
name|'utils'
op|'.'
name|'RawTGZImage'
op|'('
name|'glance_image'
op|')'
newline|'\n'
name|'glance_image'
op|'.'
name|'data'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'iterable-data'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'IterableToFileAdapter'
op|'('
string|"'iterable-data'"
op|')'
op|'.'
name|'AndReturn'
op|'('
string|"'data-as-file'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'image'
op|'.'
name|'_as_file'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'data-as-file'"
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_size
dedent|''
name|'def'
name|'test_get_size'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tar_file'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'tarfile'
op|'.'
name|'TarFile'
op|')'
newline|'\n'
name|'tar_info'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'tarfile'
op|'.'
name|'TarInfo'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'utils'
op|'.'
name|'RawTGZImage'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'image'
op|','
string|"'_as_tarfile'"
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'.'
name|'_as_tarfile'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'tar_file'
op|')'
newline|'\n'
name|'tar_file'
op|'.'
name|'next'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'tar_info'
op|')'
newline|'\n'
name|'tar_info'
op|'.'
name|'size'
op|'='
number|'124'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'image'
op|'.'
name|'get_size'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'124'
op|','
name|'result'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'_tar_info'
op|','
name|'tar_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'_tar_file'
op|','
name|'tar_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_size_called_twice
dedent|''
name|'def'
name|'test_get_size_called_twice'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tar_file'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'tarfile'
op|'.'
name|'TarFile'
op|')'
newline|'\n'
name|'tar_info'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'tarfile'
op|'.'
name|'TarInfo'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'utils'
op|'.'
name|'RawTGZImage'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'image'
op|','
string|"'_as_tarfile'"
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'.'
name|'_as_tarfile'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'tar_file'
op|')'
newline|'\n'
name|'tar_file'
op|'.'
name|'next'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'tar_info'
op|')'
newline|'\n'
name|'tar_info'
op|'.'
name|'size'
op|'='
number|'124'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'.'
name|'get_size'
op|'('
op|')'
newline|'\n'
name|'result'
op|'='
name|'image'
op|'.'
name|'get_size'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'124'
op|','
name|'result'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'_tar_info'
op|','
name|'tar_info'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image'
op|'.'
name|'_tar_file'
op|','
name|'tar_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stream_to_without_size_retrieved
dedent|''
name|'def'
name|'test_stream_to_without_size_retrieved'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'source_tar'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'tarfile'
op|'.'
name|'TarFile'
op|')'
newline|'\n'
name|'first_tarinfo'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'tarfile'
op|'.'
name|'TarInfo'
op|')'
newline|'\n'
name|'target_file'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'file'
op|')'
newline|'\n'
name|'source_file'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'file'
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'utils'
op|'.'
name|'RawTGZImage'
op|'('
name|'None'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'_image_service_and_image_id'
op|'='
op|'('
string|"'service'"
op|','
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'image'
op|','
string|"'_as_tarfile'"
op|','
name|'source_tar'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|'.'
name|'shutil'
op|','
string|"'copyfileobj'"
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'.'
name|'_as_tarfile'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'source_tar'
op|')'
newline|'\n'
name|'source_tar'
op|'.'
name|'next'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'first_tarinfo'
op|')'
newline|'\n'
name|'source_tar'
op|'.'
name|'extractfile'
op|'('
name|'first_tarinfo'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'source_file'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'shutil'
op|'.'
name|'copyfileobj'
op|'('
name|'source_file'
op|','
name|'target_file'
op|')'
newline|'\n'
name|'source_tar'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'.'
name|'stream_to'
op|'('
name|'target_file'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stream_to_with_size_retrieved
dedent|''
name|'def'
name|'test_stream_to_with_size_retrieved'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'source_tar'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'tarfile'
op|'.'
name|'TarFile'
op|')'
newline|'\n'
name|'first_tarinfo'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'tarfile'
op|'.'
name|'TarInfo'
op|')'
newline|'\n'
name|'target_file'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'file'
op|')'
newline|'\n'
name|'source_file'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMock'
op|'('
name|'file'
op|')'
newline|'\n'
name|'first_tarinfo'
op|'.'
name|'size'
op|'='
number|'124'
newline|'\n'
nl|'\n'
name|'image'
op|'='
name|'utils'
op|'.'
name|'RawTGZImage'
op|'('
name|'None'
op|')'
newline|'\n'
name|'image'
op|'.'
name|'_image_service_and_image_id'
op|'='
op|'('
string|"'service'"
op|','
string|"'id'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'image'
op|','
string|"'_as_tarfile'"
op|','
name|'source_tar'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|'.'
name|'shutil'
op|','
string|"'copyfileobj'"
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'.'
name|'_as_tarfile'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'source_tar'
op|')'
newline|'\n'
name|'source_tar'
op|'.'
name|'next'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'first_tarinfo'
op|')'
newline|'\n'
name|'source_tar'
op|'.'
name|'extractfile'
op|'('
name|'first_tarinfo'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'source_file'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'shutil'
op|'.'
name|'copyfileobj'
op|'('
name|'source_file'
op|','
name|'target_file'
op|')'
newline|'\n'
name|'source_tar'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image'
op|'.'
name|'get_size'
op|'('
op|')'
newline|'\n'
name|'image'
op|'.'
name|'stream_to'
op|'('
name|'target_file'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
