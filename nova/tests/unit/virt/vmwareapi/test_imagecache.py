begin_unit
comment|'# Copyright (c) 2014 VMware, Inc.'
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
name|'contextlib'
newline|'\n'
name|'import'
name|'datetime'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'oslo_vmware'
op|'.'
name|'objects'
name|'import'
name|'datastore'
name|'as'
name|'ds_obj'
newline|'\n'
name|'from'
name|'oslo_vmware'
name|'import'
name|'vim_util'
name|'as'
name|'vutil'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
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
name|'import'
name|'fake_instance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'ds_util'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'imagecache'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ImageCacheManagerTestCase
name|'class'
name|'ImageCacheManagerTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|REQUIRES_LOCKING
indent|'    '
name|'REQUIRES_LOCKING'
op|'='
name|'True'
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
name|'ImageCacheManagerTestCase'
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
name|'_session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'name'
op|'='
string|"'session'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'='
name|'imagecache'
op|'.'
name|'ImageCacheManager'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
string|"'fake-base-folder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_time'
op|'='
name|'datetime'
op|'.'
name|'datetime'
op|'('
number|'2012'
op|','
number|'11'
op|','
number|'22'
op|','
number|'12'
op|','
number|'00'
op|','
number|'00'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_file_name'
op|'='
string|"'ts-2012-11-22-12-00-00'"
newline|'\n'
name|'fake'
op|'.'
name|'reset'
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
name|'super'
op|'('
name|'ImageCacheManagerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
name|'fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_timestamp_cleanup
dedent|''
name|'def'
name|'test_timestamp_cleanup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_timestamp
indent|'        '
name|'def'
name|'fake_get_timestamp'
op|'('
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-ds-browser'"
op|','
name|'ds_browser'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[fake-ds] fake-path'"
op|','
name|'str'
op|'('
name|'ds_path'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'exists'
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'ts'
op|'='
string|"'%s%s'"
op|'%'
op|'('
name|'imagecache'
op|'.'
name|'TIMESTAMP_PREFIX'
op|','
nl|'\n'
name|'timeutils'
op|'.'
name|'strtime'
op|'('
name|'at'
op|'='
name|'self'
op|'.'
name|'_time'
op|','
nl|'\n'
name|'fmt'
op|'='
name|'imagecache'
op|'.'
name|'TIMESTAMP_FORMAT'
op|')'
op|')'
newline|'\n'
name|'return'
name|'ts'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_imagecache'
op|','
string|"'_get_timestamp'"
op|','
nl|'\n'
name|'fake_get_timestamp'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ds_util'
op|','
string|"'file_delete'"
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_get_timestamp'
op|','
name|'_file_delete'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'exists'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'timestamp_cleanup'
op|'('
nl|'\n'
string|"'fake-dc-ref'"
op|','
string|"'fake-ds-browser'"
op|','
nl|'\n'
name|'ds_obj'
op|'.'
name|'DatastorePath'
op|'('
string|"'fake-ds'"
op|','
string|"'fake-path'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'_file_delete'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'exists'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'timestamp_cleanup'
op|'('
nl|'\n'
string|"'fake-dc-ref'"
op|','
string|"'fake-ds-browser'"
op|','
nl|'\n'
name|'ds_obj'
op|'.'
name|'DatastorePath'
op|'('
string|"'fake-ds'"
op|','
string|"'fake-path'"
op|')'
op|')'
newline|'\n'
name|'expected_ds_path'
op|'='
name|'ds_obj'
op|'.'
name|'DatastorePath'
op|'('
nl|'\n'
string|"'fake-ds'"
op|','
string|"'fake-path'"
op|','
name|'self'
op|'.'
name|'_file_name'
op|')'
newline|'\n'
name|'_file_delete'
op|'.'
name|'assert_called_once_with'
op|'('
name|'self'
op|'.'
name|'_session'
op|','
nl|'\n'
name|'expected_ds_path'
op|','
string|"'fake-dc-ref'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_timestamp
dedent|''
dedent|''
name|'def'
name|'test_get_timestamp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_sub_folders
indent|'        '
name|'def'
name|'fake_get_sub_folders'
op|'('
name|'session'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'fake-ds-browser'"
op|','
name|'ds_browser'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[fake-ds] fake-path'"
op|','
name|'str'
op|'('
name|'ds_path'
op|')'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'exists'
op|':'
newline|'\n'
indent|'                '
name|'files'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'files'
op|'.'
name|'add'
op|'('
name|'self'
op|'.'
name|'_file_name'
op|')'
newline|'\n'
name|'return'
name|'files'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ds_util'
op|','
string|"'get_sub_folders'"
op|','
nl|'\n'
name|'fake_get_sub_folders'
op|')'
nl|'\n'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'exists'
op|'='
name|'True'
newline|'\n'
name|'ts'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'_get_timestamp'
op|'('
nl|'\n'
string|"'fake-ds-browser'"
op|','
nl|'\n'
name|'ds_obj'
op|'.'
name|'DatastorePath'
op|'('
string|"'fake-ds'"
op|','
string|"'fake-path'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_file_name'
op|','
name|'ts'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'exists'
op|'='
name|'False'
newline|'\n'
name|'ts'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'_get_timestamp'
op|'('
nl|'\n'
string|"'fake-ds-browser'"
op|','
nl|'\n'
name|'ds_obj'
op|'.'
name|'DatastorePath'
op|'('
string|"'fake-ds'"
op|','
string|"'fake-path'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'ts'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_timestamp_filename
dedent|''
dedent|''
name|'def'
name|'test_get_timestamp_filename'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'self'
op|'.'
name|'_time'
op|')'
newline|'\n'
name|'fn'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'_get_timestamp_filename'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_file_name'
op|','
name|'fn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_datetime_from_filename
dedent|''
name|'def'
name|'test_get_datetime_from_filename'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'t'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'_get_datetime_from_filename'
op|'('
name|'self'
op|'.'
name|'_file_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_time'
op|','
name|'t'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_ds_browser
dedent|''
name|'def'
name|'test_get_ds_browser'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cache'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'_ds_browser'
newline|'\n'
name|'ds_browser'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'moref'
op|'='
name|'fake'
op|'.'
name|'ManagedObjectReference'
op|'('
string|"'datastore-100'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'cache'
op|'.'
name|'get'
op|'('
name|'moref'
op|'.'
name|'value'
op|')'
op|')'
newline|'\n'
name|'mock_get_method'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'return_value'
op|'='
name|'ds_browser'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vutil'
op|','
string|"'get_object_property'"
op|','
name|'mock_get_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ret'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'_get_ds_browser'
op|'('
name|'moref'
op|')'
newline|'\n'
name|'mock_get_method'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'moref'
op|','
string|"'browser'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIs'
op|'('
name|'ds_browser'
op|','
name|'ret'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIs'
op|'('
name|'ds_browser'
op|','
name|'cache'
op|'.'
name|'get'
op|'('
name|'moref'
op|'.'
name|'value'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_list_base_images
dedent|''
dedent|''
name|'def'
name|'test_list_base_images'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_object_property
indent|'        '
name|'def'
name|'fake_get_object_property'
op|'('
name|'vim'
op|','
name|'mobj'
op|','
name|'property_name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'fake-ds-browser'"
newline|'\n'
nl|'\n'
DECL|function|fake_get_sub_folders
dedent|''
name|'def'
name|'fake_get_sub_folders'
op|'('
name|'session'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'files'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'files'
op|'.'
name|'add'
op|'('
string|"'image-ref-uuid'"
op|')'
newline|'\n'
name|'return'
name|'files'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'vutil'
op|','
string|"'get_object_property'"
op|','
nl|'\n'
name|'fake_get_object_property'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ds_util'
op|','
string|"'get_sub_folders'"
op|','
nl|'\n'
name|'fake_get_sub_folders'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_get_dynamic'
op|','
name|'_get_sub_folders'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fake_ds_ref'
op|'='
name|'fake'
op|'.'
name|'ManagedObjectReference'
op|'('
string|"'fake-ds-ref'"
op|')'
newline|'\n'
name|'datastore'
op|'='
name|'ds_obj'
op|'.'
name|'Datastore'
op|'('
name|'name'
op|'='
string|"'ds'"
op|','
name|'ref'
op|'='
name|'fake_ds_ref'
op|')'
newline|'\n'
name|'ds_path'
op|'='
name|'datastore'
op|'.'
name|'build_path'
op|'('
string|"'base_folder'"
op|')'
newline|'\n'
name|'images'
op|'='
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'_list_datastore_images'
op|'('
nl|'\n'
name|'ds_path'
op|','
name|'datastore'
op|')'
newline|'\n'
name|'originals'
op|'='
name|'set'
op|'('
op|')'
newline|'\n'
name|'originals'
op|'.'
name|'add'
op|'('
string|"'image-ref-uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'{'
string|"'originals'"
op|':'
name|'originals'
op|','
nl|'\n'
string|"'unexplained_images'"
op|':'
op|'['
op|']'
op|'}'
op|','
nl|'\n'
name|'images'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'imagecache'
op|'.'
name|'ImageCacheManager'
op|','
string|"'timestamp_folder_get'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'imagecache'
op|'.'
name|'ImageCacheManager'
op|','
string|"'timestamp_cleanup'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'imagecache'
op|'.'
name|'ImageCacheManager'
op|','
string|"'_get_ds_browser'"
op|')'
newline|'\n'
DECL|member|test_enlist_image
name|'def'
name|'test_enlist_image'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_get_ds_browser'
op|','
nl|'\n'
name|'mock_timestamp_cleanup'
op|','
nl|'\n'
name|'mock_timestamp_folder_get'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_id'
op|'='
string|'"fake_image_id"'
newline|'\n'
name|'dc_ref'
op|'='
string|'"fake_dc_ref"'
newline|'\n'
name|'fake_ds_ref'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'ds'
op|'='
name|'ds_obj'
op|'.'
name|'Datastore'
op|'('
nl|'\n'
name|'ref'
op|'='
name|'fake_ds_ref'
op|','
name|'name'
op|'='
string|"'fake_ds'"
op|','
nl|'\n'
name|'capacity'
op|'='
number|'1'
op|','
nl|'\n'
name|'freespace'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'ds_browser'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_get_ds_browser'
op|'.'
name|'return_value'
op|'='
name|'ds_browser'
newline|'\n'
name|'timestamp_folder_path'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'mock_timestamp_folder_get'
op|'.'
name|'return_value'
op|'='
name|'timestamp_folder_path'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'enlist_image'
op|'('
name|'image_id'
op|','
name|'ds'
op|','
name|'dc_ref'
op|')'
newline|'\n'
nl|'\n'
name|'cache_root_folder'
op|'='
name|'ds'
op|'.'
name|'build_path'
op|'('
string|'"fake-base-folder"'
op|')'
newline|'\n'
name|'mock_get_ds_browser'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'ds'
op|'.'
name|'ref'
op|')'
newline|'\n'
name|'mock_timestamp_folder_get'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'cache_root_folder'
op|','
string|'"fake_image_id"'
op|')'
newline|'\n'
name|'mock_timestamp_cleanup'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'dc_ref'
op|','
name|'ds_browser'
op|','
name|'timestamp_folder_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_age_cached_images
dedent|''
name|'def'
name|'test_age_cached_images'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_ds_browser
indent|'        '
name|'def'
name|'fake_get_ds_browser'
op|'('
name|'ds_ref'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'fake-ds-browser'"
newline|'\n'
nl|'\n'
DECL|function|fake_get_timestamp
dedent|''
name|'def'
name|'fake_get_timestamp'
op|'('
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_get_timestamp_called'
op|'+='
number|'1'
newline|'\n'
name|'path'
op|'='
name|'str'
op|'('
name|'ds_path'
op|')'
newline|'\n'
name|'if'
name|'path'
op|'=='
string|"'[fake-ds] fake-path/fake-image-1'"
op|':'
newline|'\n'
comment|'# No time stamp exists'
nl|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'if'
name|'path'
op|'=='
string|"'[fake-ds] fake-path/fake-image-2'"
op|':'
newline|'\n'
comment|'# Timestamp that will be valid => no deletion'
nl|'\n'
indent|'                '
name|'return'
string|"'ts-2012-11-22-10-00-00'"
newline|'\n'
dedent|''
name|'if'
name|'path'
op|'=='
string|"'[fake-ds] fake-path/fake-image-3'"
op|':'
newline|'\n'
comment|'# Timestamp that will be invalid => deletion'
nl|'\n'
indent|'                '
name|'return'
string|"'ts-2012-11-20-12-00-00'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'fail'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_mkdir
dedent|''
name|'def'
name|'fake_mkdir'
op|'('
name|'session'
op|','
name|'ts_path'
op|','
name|'dc_ref'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
string|"'[fake-ds] fake-path/fake-image-1/ts-2012-11-22-12-00-00'"
op|','
nl|'\n'
name|'str'
op|'('
name|'ts_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_file_delete
dedent|''
name|'def'
name|'fake_file_delete'
op|'('
name|'session'
op|','
name|'ds_path'
op|','
name|'dc_ref'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[fake-ds] fake-path/fake-image-3'"
op|','
name|'str'
op|'('
name|'ds_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_timestamp_cleanup
dedent|''
name|'def'
name|'fake_timestamp_cleanup'
op|'('
name|'dc_ref'
op|','
name|'ds_browser'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[fake-ds] fake-path/fake-image-4'"
op|','
name|'str'
op|'('
name|'ds_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_imagecache'
op|','
string|"'_get_ds_browser'"
op|','
nl|'\n'
name|'fake_get_ds_browser'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_imagecache'
op|','
string|"'_get_timestamp'"
op|','
nl|'\n'
name|'fake_get_timestamp'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ds_util'
op|','
string|"'mkdir'"
op|','
nl|'\n'
name|'fake_mkdir'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'ds_util'
op|','
string|"'file_delete'"
op|','
nl|'\n'
name|'fake_file_delete'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_imagecache'
op|','
string|"'timestamp_cleanup'"
op|','
nl|'\n'
name|'fake_timestamp_cleanup'
op|')'
op|','
nl|'\n'
op|')'
name|'as'
op|'('
name|'_get_ds_browser'
op|','
name|'_get_timestamp'
op|','
name|'_mkdir'
op|','
name|'_file_delete'
op|','
nl|'\n'
name|'_timestamp_cleanup'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'timeutils'
op|'.'
name|'set_time_override'
op|'('
name|'override_time'
op|'='
name|'self'
op|'.'
name|'_time'
op|')'
newline|'\n'
name|'datastore'
op|'='
name|'ds_obj'
op|'.'
name|'Datastore'
op|'('
name|'name'
op|'='
string|"'ds'"
op|','
name|'ref'
op|'='
string|"'fake-ds-ref'"
op|')'
newline|'\n'
name|'dc_info'
op|'='
name|'ds_util'
op|'.'
name|'DcInfo'
op|'('
name|'ref'
op|'='
string|"'dc_ref'"
op|','
name|'name'
op|'='
string|"'name'"
op|','
nl|'\n'
name|'vmFolder'
op|'='
string|"'vmFolder'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_get_timestamp_called'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'originals'
op|'='
name|'set'
op|'('
op|'['
string|"'fake-image-1'"
op|','
string|"'fake-image-2'"
op|','
nl|'\n'
string|"'fake-image-3'"
op|','
string|"'fake-image-4'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'used_images'
op|'='
name|'set'
op|'('
op|'['
string|"'fake-image-4'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'_age_cached_images'
op|'('
nl|'\n'
string|"'fake-context'"
op|','
name|'datastore'
op|','
name|'dc_info'
op|','
nl|'\n'
name|'ds_obj'
op|'.'
name|'DatastorePath'
op|'('
string|"'fake-ds'"
op|','
string|"'fake-path'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'3'
op|','
name|'self'
op|'.'
name|'_get_timestamp_called'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'objects'
op|'.'
name|'block_device'
op|'.'
name|'BlockDeviceMappingList'
op|','
nl|'\n'
string|"'get_by_instance_uuid'"
op|')'
newline|'\n'
DECL|member|test_update
name|'def'
name|'test_update'
op|'('
name|'self'
op|','
name|'mock_get_by_inst'
op|')'
op|':'
newline|'\n'
DECL|function|fake_list_datastore_images
indent|'        '
name|'def'
name|'fake_list_datastore_images'
op|'('
name|'ds_path'
op|','
name|'datastore'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'{'
string|"'unexplained_images'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'originals'"
op|':'
name|'self'
op|'.'
name|'images'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_age_cached_images
dedent|''
name|'def'
name|'fake_age_cached_images'
op|'('
name|'context'
op|','
name|'datastore'
op|','
nl|'\n'
name|'dc_info'
op|','
name|'ds_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'[ds] fake-base-folder'"
op|','
name|'str'
op|'('
name|'ds_path'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'images'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'used_images'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'images'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'originals'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'with'
name|'contextlib'
op|'.'
name|'nested'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_imagecache'
op|','
string|"'_list_datastore_images'"
op|','
nl|'\n'
name|'fake_list_datastore_images'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'_imagecache'
op|','
nl|'\n'
string|"'_age_cached_images'"
op|','
nl|'\n'
name|'fake_age_cached_images'
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'_list_base'
op|','
name|'_age_and_verify'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instances'
op|'='
op|'['
op|'{'
string|"'image_ref'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'inst-1'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'123'"
op|','
nl|'\n'
string|"'vm_state'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'task_state'"
op|':'
string|"''"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'image_ref'"
op|':'
string|"'2'"
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'host'
op|','
nl|'\n'
string|"'name'"
op|':'
string|"'inst-2'"
op|','
nl|'\n'
string|"'uuid'"
op|':'
string|"'456'"
op|','
nl|'\n'
string|"'vm_state'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'task_state'"
op|':'
string|"''"
op|'}'
op|']'
newline|'\n'
name|'all_instances'
op|'='
op|'['
name|'fake_instance'
op|'.'
name|'fake_instance_obj'
op|'('
name|'None'
op|','
op|'**'
name|'instance'
op|')'
nl|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'images'
op|'='
name|'set'
op|'('
op|'['
string|"'1'"
op|','
string|"'2'"
op|']'
op|')'
newline|'\n'
name|'datastore'
op|'='
name|'ds_obj'
op|'.'
name|'Datastore'
op|'('
name|'name'
op|'='
string|"'ds'"
op|','
name|'ref'
op|'='
string|"'fake-ds-ref'"
op|')'
newline|'\n'
name|'dc_info'
op|'='
name|'ds_util'
op|'.'
name|'DcInfo'
op|'('
name|'ref'
op|'='
string|"'dc_ref'"
op|','
name|'name'
op|'='
string|"'name'"
op|','
nl|'\n'
name|'vmFolder'
op|'='
string|"'vmFolder'"
op|')'
newline|'\n'
name|'datastores_info'
op|'='
op|'['
op|'('
name|'datastore'
op|','
name|'dc_info'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_imagecache'
op|'.'
name|'update'
op|'('
string|"'context'"
op|','
name|'all_instances'
op|','
name|'datastores_info'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
