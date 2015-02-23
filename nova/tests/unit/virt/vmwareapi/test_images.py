begin_unit
comment|'# Copyright (c) 2014 VMware, Inc.'
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
string|'"""\nTest suite for images.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'contextlib'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tarfile'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'units'
newline|'\n'
name|'from'
name|'oslo_vmware'
name|'import'
name|'rw_handles'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
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
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'vmwareapi'
name|'import'
name|'images'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VMwareImagesTestCase
name|'class'
name|'VMwareImagesTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for Vmware API connection calls."""'
newline|'\n'
nl|'\n'
DECL|member|test_fetch_image
name|'def'
name|'test_fetch_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test fetching images."""'
newline|'\n'
nl|'\n'
name|'dc_name'
op|'='
string|"'fake-dc'"
newline|'\n'
name|'file_path'
op|'='
string|"'fake_file'"
newline|'\n'
name|'ds_name'
op|'='
string|"'ds1'"
newline|'\n'
name|'host'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'port'
op|'='
number|'7443'
newline|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'image_data'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vmdk'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'512'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'read_file_handle'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'write_file_handle'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'read_iter'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
name|'objects'
op|'.'
name|'Instance'
op|'('
name|'id'
op|'='
number|'1'
op|','
nl|'\n'
name|'uuid'
op|'='
string|"'fake-uuid'"
op|','
nl|'\n'
name|'image_ref'
op|'='
name|'image_data'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_read_handle
name|'def'
name|'fake_read_handle'
op|'('
name|'read_iter'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'read_file_handle'
newline|'\n'
nl|'\n'
DECL|function|fake_write_handle
dedent|''
name|'def'
name|'fake_write_handle'
op|'('
name|'host'
op|','
name|'port'
op|','
name|'dc_name'
op|','
name|'ds_name'
op|','
name|'cookies'
op|','
nl|'\n'
name|'file_path'
op|','
name|'file_size'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'write_file_handle'
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
name|'rw_handles'
op|','
string|"'ImageReadHandle'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'fake_read_handle'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'rw_handles'
op|','
string|"'FileWriteHandle'"
op|','
nl|'\n'
name|'side_effect'
op|'='
name|'fake_write_handle'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|','
string|"'start_transfer'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|'.'
name|'IMAGE_API'
op|','
string|"'get'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'image_data'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|'.'
name|'IMAGE_API'
op|','
string|"'download'"
op|','
nl|'\n'
name|'return_value'
op|'='
name|'read_iter'
op|')'
op|','
nl|'\n'
op|')'
name|'as'
op|'('
name|'glance_read'
op|','
name|'http_write'
op|','
name|'start_transfer'
op|','
name|'image_show'
op|','
nl|'\n'
name|'image_download'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'images'
op|'.'
name|'fetch_image'
op|'('
name|'context'
op|','
name|'instance'
op|','
nl|'\n'
name|'host'
op|','
name|'port'
op|','
name|'dc_name'
op|','
nl|'\n'
name|'ds_name'
op|','
name|'file_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'glance_read'
op|'.'
name|'assert_called_once_with'
op|'('
name|'read_iter'
op|')'
newline|'\n'
name|'http_write'
op|'.'
name|'assert_called_once_with'
op|'('
name|'host'
op|','
name|'port'
op|','
name|'dc_name'
op|','
name|'ds_name'
op|','
name|'None'
op|','
nl|'\n'
name|'file_path'
op|','
name|'image_data'
op|'['
string|"'size'"
op|']'
op|')'
newline|'\n'
name|'start_transfer'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'context'
op|','
name|'read_file_handle'
op|','
nl|'\n'
name|'image_data'
op|'['
string|"'size'"
op|']'
op|','
nl|'\n'
name|'write_file_handle'
op|'='
name|'write_file_handle'
op|')'
newline|'\n'
name|'image_download'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|')'
newline|'\n'
name|'image_show'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'image_ref'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_setup_mock_get_remote_image_service
dedent|''
name|'def'
name|'_setup_mock_get_remote_image_service'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_get_remote_image_service'
op|','
nl|'\n'
name|'metadata'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_image_service'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_image_service'
op|'.'
name|'show'
op|'.'
name|'return_value'
op|'='
name|'metadata'
newline|'\n'
name|'mock_get_remote_image_service'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock_image_service'
op|','
string|"'i'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_get_vmdk_name_from_ovf
dedent|''
name|'def'
name|'test_get_vmdk_name_from_ovf'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ovf_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'ovf.xml'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'ovf_path'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'ovf_descriptor'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'vmdk_name'
op|'='
name|'images'
op|'.'
name|'get_vmdk_name_from_ovf'
op|'('
name|'ovf_descriptor'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Damn_Small_Linux-disk1.vmdk"'
op|','
name|'vmdk_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'oslo_vmware.rw_handles.ImageReadHandle'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'oslo_vmware.rw_handles.VmdkWriteHandle'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'tarfile'
op|','
string|"'open'"
op|')'
newline|'\n'
DECL|member|test_fetch_image_ova
name|'def'
name|'test_fetch_image_ova'
op|'('
name|'self'
op|','
name|'mock_tar_open'
op|','
name|'mock_write_class'
op|','
nl|'\n'
name|'mock_read_class'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'ovf_descriptor'
op|'='
name|'None'
newline|'\n'
name|'ovf_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'ovf.xml'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'ovf_path'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'ovf_descriptor'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
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
name|'images'
op|'.'
name|'IMAGE_API'
op|','
string|"'get'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|'.'
name|'IMAGE_API'
op|','
string|"'download'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|','
string|"'start_transfer'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|','
string|"'_build_shadow_vm_config_spec'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'session'
op|','
string|"'_call_method'"
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'mock_image_api_get'
op|','
nl|'\n'
name|'mock_image_api_download'
op|','
nl|'\n'
name|'mock_start_transfer'
op|','
nl|'\n'
name|'mock_build_shadow_vm_config_spec'
op|','
nl|'\n'
name|'mock_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_data'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake-id'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vmdk'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'512'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'image_ref'
op|'='
name|'image_data'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'mock_image_api_get'
op|'.'
name|'return_value'
op|'='
name|'image_data'
newline|'\n'
nl|'\n'
name|'vm_folder_ref'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'res_pool_ref'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_read_handle'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_read_class'
op|'.'
name|'return_value'
op|'='
name|'mock_read_handle'
newline|'\n'
name|'mock_write_handle'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_write_class'
op|'.'
name|'return_value'
op|'='
name|'mock_write_handle'
newline|'\n'
name|'mock_write_handle'
op|'.'
name|'get_imported_vm'
op|'.'
name|'return_value'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'vm_ref'
newline|'\n'
nl|'\n'
name|'mock_ovf'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_ovf'
op|'.'
name|'name'
op|'='
string|"'dsl.ovf'"
newline|'\n'
name|'mock_vmdk'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_vmdk'
op|'.'
name|'name'
op|'='
string|'"Damn_Small_Linux-disk1.vmdk"'
newline|'\n'
nl|'\n'
DECL|function|fake_extract
name|'def'
name|'fake_extract'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'name'
op|'=='
name|'mock_ovf'
op|':'
newline|'\n'
indent|'                    '
name|'m'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'m'
op|'.'
name|'read'
op|'.'
name|'return_value'
op|'='
name|'ovf_descriptor'
newline|'\n'
name|'return'
name|'m'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|'=='
name|'mock_vmdk'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'mock_read_handle'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'mock_tar'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_tar'
op|'.'
name|'__iter__'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'return_value'
op|'='
name|'iter'
op|'('
op|'['
name|'mock_ovf'
op|','
nl|'\n'
name|'mock_vmdk'
op|']'
op|')'
op|')'
newline|'\n'
name|'mock_tar'
op|'.'
name|'extractfile'
op|'='
name|'fake_extract'
newline|'\n'
name|'mock_tar_open'
op|'.'
name|'return_value'
op|'.'
name|'__enter__'
op|'.'
name|'return_value'
op|'='
name|'mock_tar'
newline|'\n'
nl|'\n'
name|'images'
op|'.'
name|'fetch_image_ova'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'session'
op|','
string|"'fake-vm'"
op|','
string|"'fake-datastore'"
op|','
nl|'\n'
name|'vm_folder_ref'
op|','
name|'res_pool_ref'
op|')'
newline|'\n'
nl|'\n'
name|'mock_tar_open'
op|'.'
name|'assert_called_once_with'
op|'('
name|'mode'
op|'='
string|"'r|'"
op|','
nl|'\n'
name|'fileobj'
op|'='
name|'mock_read_handle'
op|')'
newline|'\n'
name|'mock_start_transfer'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
nl|'\n'
name|'mock_read_handle'
op|','
number|'512'
op|','
name|'write_file_handle'
op|'='
name|'mock_write_handle'
op|')'
newline|'\n'
nl|'\n'
name|'mock_call_method'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'session'
op|'.'
name|'vim'
op|','
string|'"UnregisterVM"'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'oslo_vmware.rw_handles.ImageReadHandle'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'oslo_vmware.rw_handles.VmdkWriteHandle'"
op|')'
newline|'\n'
DECL|member|test_fetch_image_stream_optimized
name|'def'
name|'test_fetch_image_stream_optimized'
op|'('
name|'self'
op|','
nl|'\n'
name|'mock_write_class'
op|','
nl|'\n'
name|'mock_read_class'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test fetching streamOptimized disk image."""'
newline|'\n'
name|'session'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
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
name|'images'
op|'.'
name|'IMAGE_API'
op|','
string|"'get'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|'.'
name|'IMAGE_API'
op|','
string|"'download'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|','
string|"'start_transfer'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'images'
op|','
string|"'_build_shadow_vm_config_spec'"
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'session'
op|','
string|"'_call_method'"
op|')'
nl|'\n'
op|')'
name|'as'
op|'('
name|'mock_image_api_get'
op|','
nl|'\n'
name|'mock_image_api_download'
op|','
nl|'\n'
name|'mock_start_transfer'
op|','
nl|'\n'
name|'mock_build_shadow_vm_config_spec'
op|','
nl|'\n'
name|'mock_call_method'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'image_data'
op|'='
op|'{'
string|"'id'"
op|':'
string|"'fake-id'"
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vmdk'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'512'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'.'
name|'image_ref'
op|'='
name|'image_data'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'mock_image_api_get'
op|'.'
name|'return_value'
op|'='
name|'image_data'
newline|'\n'
nl|'\n'
name|'vm_folder_ref'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'res_pool_ref'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'context'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_read_handle'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_read_class'
op|'.'
name|'return_value'
op|'='
name|'mock_read_handle'
newline|'\n'
name|'mock_write_handle'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_write_class'
op|'.'
name|'return_value'
op|'='
name|'mock_write_handle'
newline|'\n'
name|'mock_write_handle'
op|'.'
name|'get_imported_vm'
op|'.'
name|'return_value'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'vm_ref'
newline|'\n'
nl|'\n'
name|'images'
op|'.'
name|'fetch_image_stream_optimized'
op|'('
nl|'\n'
name|'context'
op|','
name|'instance'
op|','
name|'session'
op|','
string|"'fake-vm'"
op|','
string|"'fake-datastore'"
op|','
nl|'\n'
name|'vm_folder_ref'
op|','
name|'res_pool_ref'
op|')'
newline|'\n'
nl|'\n'
name|'mock_start_transfer'
op|'.'
name|'assert_called_once_with'
op|'('
name|'context'
op|','
nl|'\n'
name|'mock_read_handle'
op|','
number|'512'
op|','
name|'write_file_handle'
op|'='
name|'mock_write_handle'
op|')'
newline|'\n'
nl|'\n'
name|'mock_call_method'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'session'
op|'.'
name|'vim'
op|','
string|'"UnregisterVM"'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_from_image_with_image_ref
dedent|''
dedent|''
name|'def'
name|'test_from_image_with_image_ref'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raw_disk_size_in_gb'
op|'='
number|'83'
newline|'\n'
name|'raw_disk_size_in_bytes'
op|'='
name|'raw_disk_size_in_gb'
op|'*'
name|'units'
op|'.'
name|'Gi'
newline|'\n'
name|'image_id'
op|'='
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'mdata'
op|'='
op|'{'
string|"'size'"
op|':'
name|'raw_disk_size_in_bytes'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
string|"'vmdk'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|'"vmware_ostype"'
op|':'
name|'constants'
op|'.'
name|'DEFAULT_OS_TYPE'
op|','
nl|'\n'
string|'"vmware_adaptertype"'
op|':'
name|'constants'
op|'.'
name|'DEFAULT_ADAPTER_TYPE'
op|','
nl|'\n'
string|'"vmware_disktype"'
op|':'
name|'constants'
op|'.'
name|'DEFAULT_DISK_TYPE'
op|','
nl|'\n'
string|'"hw_vif_model"'
op|':'
name|'constants'
op|'.'
name|'DEFAULT_VIF_MODEL'
op|','
nl|'\n'
string|'"vmware_linked_clone"'
op|':'
name|'True'
op|'}'
op|'}'
newline|'\n'
name|'mdata'
op|'='
name|'objects'
op|'.'
name|'ImageMeta'
op|'.'
name|'from_dict'
op|'('
name|'mdata'
op|')'
newline|'\n'
name|'img_props'
op|'='
name|'images'
op|'.'
name|'VMwareImage'
op|'.'
name|'from_image'
op|'('
name|'image_id'
op|','
name|'mdata'
op|')'
newline|'\n'
nl|'\n'
name|'image_size_in_kb'
op|'='
name|'raw_disk_size_in_bytes'
op|'/'
name|'units'
op|'.'
name|'Ki'
newline|'\n'
nl|'\n'
comment|'# assert that defaults are set and no value returned is left empty'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'constants'
op|'.'
name|'DEFAULT_OS_TYPE'
op|','
name|'img_props'
op|'.'
name|'os_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'constants'
op|'.'
name|'DEFAULT_ADAPTER_TYPE'
op|','
nl|'\n'
name|'img_props'
op|'.'
name|'adapter_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'constants'
op|'.'
name|'DEFAULT_DISK_TYPE'
op|','
name|'img_props'
op|'.'
name|'disk_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'constants'
op|'.'
name|'DEFAULT_VIF_MODEL'
op|','
name|'img_props'
op|'.'
name|'vif_model'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'img_props'
op|'.'
name|'linked_clone'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'image_size_in_kb'
op|','
name|'img_props'
op|'.'
name|'file_size_in_kb'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_image_build
dedent|''
name|'def'
name|'_image_build'
op|'('
name|'self'
op|','
name|'image_lc_setting'
op|','
name|'global_lc_setting'
op|','
nl|'\n'
name|'disk_format'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_DISK_FORMAT'
op|','
nl|'\n'
name|'os_type'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_OS_TYPE'
op|','
nl|'\n'
name|'adapter_type'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_ADAPTER_TYPE'
op|','
nl|'\n'
name|'disk_type'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_DISK_TYPE'
op|','
nl|'\n'
name|'vif_model'
op|'='
name|'constants'
op|'.'
name|'DEFAULT_VIF_MODEL'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'use_linked_clone'
op|'='
name|'global_lc_setting'
op|','
name|'group'
op|'='
string|"'vmware'"
op|')'
newline|'\n'
name|'raw_disk_size_in_gb'
op|'='
number|'93'
newline|'\n'
name|'raw_disk_size_in_btyes'
op|'='
name|'raw_disk_size_in_gb'
op|'*'
name|'units'
op|'.'
name|'Gi'
newline|'\n'
nl|'\n'
name|'image_id'
op|'='
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'get_valid_image_id'
op|'('
op|')'
newline|'\n'
name|'mdata'
op|'='
op|'{'
string|"'size'"
op|':'
name|'raw_disk_size_in_btyes'
op|','
nl|'\n'
string|"'disk_format'"
op|':'
name|'disk_format'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|'"vmware_ostype"'
op|':'
name|'os_type'
op|','
nl|'\n'
string|'"vmware_adaptertype"'
op|':'
name|'adapter_type'
op|','
nl|'\n'
string|'"vmware_disktype"'
op|':'
name|'disk_type'
op|','
nl|'\n'
string|'"hw_vif_model"'
op|':'
name|'vif_model'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'if'
name|'image_lc_setting'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'mdata'
op|'['
string|"'properties'"
op|']'
op|'['
string|'"vmware_linked_clone"'
op|']'
op|'='
name|'image_lc_setting'
newline|'\n'
nl|'\n'
dedent|''
name|'mdata'
op|'='
name|'objects'
op|'.'
name|'ImageMeta'
op|'.'
name|'from_dict'
op|'('
name|'mdata'
op|')'
newline|'\n'
name|'return'
name|'images'
op|'.'
name|'VMwareImage'
op|'.'
name|'from_image'
op|'('
name|'image_id'
op|','
name|'mdata'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_nf
dedent|''
name|'def'
name|'test_use_linked_clone_override_nf'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_props'
op|'='
name|'self'
op|'.'
name|'_image_build'
op|'('
name|'None'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'image_props'
op|'.'
name|'linked_clone'
op|','
nl|'\n'
string|'"No overrides present but still overridden!"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_nt
dedent|''
name|'def'
name|'test_use_linked_clone_override_nt'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_props'
op|'='
name|'self'
op|'.'
name|'_image_build'
op|'('
name|'None'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'image_props'
op|'.'
name|'linked_clone'
op|','
nl|'\n'
string|'"No overrides present but still overridden!"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_ny
dedent|''
name|'def'
name|'test_use_linked_clone_override_ny'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_props'
op|'='
name|'self'
op|'.'
name|'_image_build'
op|'('
name|'None'
op|','
string|'"yes"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'image_props'
op|'.'
name|'linked_clone'
op|','
nl|'\n'
string|'"No overrides present but still overridden!"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_ft
dedent|''
name|'def'
name|'test_use_linked_clone_override_ft'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_props'
op|'='
name|'self'
op|'.'
name|'_image_build'
op|'('
name|'False'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'image_props'
op|'.'
name|'linked_clone'
op|','
nl|'\n'
string|'"image level metadata failed to override global"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_string_nt
dedent|''
name|'def'
name|'test_use_linked_clone_override_string_nt'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_props'
op|'='
name|'self'
op|'.'
name|'_image_build'
op|'('
string|'"no"'
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'image_props'
op|'.'
name|'linked_clone'
op|','
nl|'\n'
string|'"image level metadata failed to override global"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_linked_clone_override_string_yf
dedent|''
name|'def'
name|'test_use_linked_clone_override_string_yf'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image_props'
op|'='
name|'self'
op|'.'
name|'_image_build'
op|'('
string|'"yes"'
op|','
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'image_props'
op|'.'
name|'linked_clone'
op|','
nl|'\n'
string|'"image level metadata failed to override global"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_disk_format_iso
dedent|''
name|'def'
name|'test_use_disk_format_iso'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
name|'self'
op|'.'
name|'_image_build'
op|'('
name|'None'
op|','
name|'True'
op|','
name|'disk_format'
op|'='
string|"'iso'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'iso'"
op|','
name|'image'
op|'.'
name|'file_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'image'
op|'.'
name|'is_iso'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_use_bad_disk_format
dedent|''
name|'def'
name|'test_use_bad_disk_format'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidDiskFormat'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_image_build'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'True'
op|','
nl|'\n'
name|'disk_format'
op|'='
string|"'bad_disk_format'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_no_defaults
dedent|''
name|'def'
name|'test_image_no_defaults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
name|'self'
op|'.'
name|'_image_build'
op|'('
name|'False'
op|','
name|'False'
op|','
nl|'\n'
name|'disk_format'
op|'='
string|"'iso'"
op|','
nl|'\n'
name|'os_type'
op|'='
string|"'otherGuest'"
op|','
nl|'\n'
name|'adapter_type'
op|'='
string|"'lsiLogic'"
op|','
nl|'\n'
name|'disk_type'
op|'='
string|"'preallocated'"
op|','
nl|'\n'
name|'vif_model'
op|'='
string|"'e1000e'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'iso'"
op|','
name|'image'
op|'.'
name|'file_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'otherGuest'"
op|','
name|'image'
op|'.'
name|'os_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'lsiLogic'"
op|','
name|'image'
op|'.'
name|'adapter_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'preallocated'"
op|','
name|'image'
op|'.'
name|'disk_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'e1000e'"
op|','
name|'image'
op|'.'
name|'vif_model'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'image'
op|'.'
name|'linked_clone'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_image_defaults
dedent|''
name|'def'
name|'test_image_defaults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'image'
op|'='
name|'images'
op|'.'
name|'VMwareImage'
op|'('
name|'image_id'
op|'='
string|"'fake-image-id'"
op|')'
newline|'\n'
nl|'\n'
comment|"# N.B. We intentially don't use the defined constants here. Amongst"
nl|'\n'
comment|"# other potential failures, we're interested in changes to their"
nl|'\n'
comment|'# values, which would not otherwise be picked up.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'otherGuest'"
op|','
name|'image'
op|'.'
name|'os_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'lsiLogic'"
op|','
name|'image'
op|'.'
name|'adapter_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'preallocated'"
op|','
name|'image'
op|'.'
name|'disk_type'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'e1000'"
op|','
name|'image'
op|'.'
name|'vif_model'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
