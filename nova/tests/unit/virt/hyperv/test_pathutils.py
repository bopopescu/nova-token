begin_unit
comment|'#  Copyright 2014 IBM Corp.'
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
name|'os'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'test_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'constants'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'pathutils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PathUtilsTestCase
name|'class'
name|'PathUtilsTestCase'
op|'('
name|'test_base'
op|'.'
name|'HyperVBaseTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V PathUtils class."""'
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
name|'PathUtilsTestCase'
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
name|'fake_instance_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'C:'"
op|','
string|"'fake_instance_dir'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fake_instance_name'
op|'='
string|"'fake_instance_name'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'='
name|'pathutils'
op|'.'
name|'PathUtils'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_smb_conn
dedent|''
name|'def'
name|'_test_smb_conn'
op|'('
name|'self'
op|','
name|'smb_available'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_mock_wmi'
op|'.'
name|'x_wmi'
op|'='
name|'Exception'
newline|'\n'
name|'self'
op|'.'
name|'_mock_wmi'
op|'.'
name|'WMI'
op|'.'
name|'side_effect'
op|'='
name|'None'
name|'if'
name|'smb_available'
name|'else'
name|'Exception'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'_set_smb_conn'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'smb_available'
op|':'
newline|'\n'
indent|'            '
name|'expected_conn'
op|'='
name|'self'
op|'.'
name|'_mock_wmi'
op|'.'
name|'WMI'
op|'.'
name|'return_value'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_conn'
op|','
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'_smb_conn'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'vmutils'
op|'.'
name|'HyperVException'
op|','
nl|'\n'
name|'getattr'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|','
string|"'_smb_conn'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_smb_conn_available
dedent|''
dedent|''
name|'def'
name|'test_smb_conn_available'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_smb_conn'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_smb_conn_unavailable
dedent|''
name|'def'
name|'test_smb_conn_unavailable'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_smb_conn'
op|'('
name|'smb_available'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'pathutils'
op|'.'
name|'PathUtils'
op|','
string|"'rename'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'isfile'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'os'
op|','
string|"'listdir'"
op|')'
newline|'\n'
DECL|member|test_move_folder_files
name|'def'
name|'test_move_folder_files'
op|'('
name|'self'
op|','
name|'mock_listdir'
op|','
name|'mock_isfile'
op|','
name|'mock_rename'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'src_dir'
op|'='
string|"'src'"
newline|'\n'
name|'dest_dir'
op|'='
string|"'dest'"
newline|'\n'
name|'fname'
op|'='
string|"'tmp_file.txt'"
newline|'\n'
name|'subdir'
op|'='
string|"'tmp_folder'"
newline|'\n'
name|'src_fname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'src_dir'
op|','
name|'fname'
op|')'
newline|'\n'
name|'dest_fname'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'dest_dir'
op|','
name|'fname'
op|')'
newline|'\n'
nl|'\n'
comment|'# making sure src_subdir is not moved.'
nl|'\n'
name|'mock_listdir'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fname'
op|','
name|'subdir'
op|']'
newline|'\n'
name|'mock_isfile'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'True'
op|','
name|'False'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'move_folder_files'
op|'('
name|'src_dir'
op|','
name|'dest_dir'
op|')'
newline|'\n'
name|'mock_rename'
op|'.'
name|'assert_called_once_with'
op|'('
name|'src_fname'
op|','
name|'dest_fname'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_mock_lookup_configdrive_path
dedent|''
name|'def'
name|'_mock_lookup_configdrive_path'
op|'('
name|'self'
op|','
name|'ext'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_instance_dir'
op|')'
newline|'\n'
nl|'\n'
DECL|function|mock_exists
name|'def'
name|'mock_exists'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'path'
op|'='
name|'args'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'True'
name|'if'
name|'path'
op|'['
op|'('
name|'path'
op|'.'
name|'rfind'
op|'('
string|"'.'"
op|')'
op|'+'
number|'1'
op|')'
op|':'
op|']'
op|'=='
name|'ext'
name|'else'
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'='
name|'mock_exists'
newline|'\n'
name|'configdrive_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'lookup_configdrive_path'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_instance_name'
op|')'
newline|'\n'
name|'return'
name|'configdrive_path'
newline|'\n'
nl|'\n'
DECL|member|test_lookup_configdrive_path
dedent|''
name|'def'
name|'test_lookup_configdrive_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'format_ext'
name|'in'
name|'constants'
op|'.'
name|'DISK_FORMAT_MAP'
op|':'
newline|'\n'
indent|'            '
name|'configdrive_path'
op|'='
name|'self'
op|'.'
name|'_mock_lookup_configdrive_path'
op|'('
name|'format_ext'
op|')'
newline|'\n'
name|'fake_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'fake_instance_dir'
op|','
nl|'\n'
string|"'configdrive.'"
op|'+'
name|'format_ext'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'configdrive_path'
op|','
name|'fake_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_lookup_configdrive_path_non_exist
dedent|''
dedent|''
name|'def'
name|'test_lookup_configdrive_path_non_exist'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'get_instance_dir'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'fake_instance_dir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'exists'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
name|'return_value'
op|'='
name|'False'
op|')'
newline|'\n'
name|'configdrive_path'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'lookup_configdrive_path'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'fake_instance_name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'configdrive_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'pathutils'
op|'.'
name|'PathUtils'
op|','
string|"'unmount_smb_share'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.path.exists'"
op|')'
newline|'\n'
DECL|member|_test_check_smb_mapping
name|'def'
name|'_test_check_smb_mapping'
op|'('
name|'self'
op|','
name|'mock_exists'
op|','
name|'mock_unmount_smb_share'
op|','
nl|'\n'
name|'existing_mappings'
op|'='
name|'True'
op|','
name|'share_available'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_exists'
op|'.'
name|'return_value'
op|'='
name|'share_available'
newline|'\n'
nl|'\n'
name|'fake_mappings'
op|'='
op|'('
nl|'\n'
op|'['
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'smb_mapping'
op|']'
name|'if'
name|'existing_mappings'
name|'else'
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'_smb_conn'
op|'.'
name|'Msft_SmbMapping'
op|'.'
name|'return_value'
op|'='
op|'('
nl|'\n'
name|'fake_mappings'
op|')'
newline|'\n'
nl|'\n'
name|'ret_val'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'check_smb_mapping'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'share_path'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'existing_mappings'
name|'and'
name|'share_available'
op|','
name|'ret_val'
op|')'
newline|'\n'
name|'if'
name|'existing_mappings'
name|'and'
name|'not'
name|'share_available'
op|':'
newline|'\n'
indent|'            '
name|'mock_unmount_smb_share'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'share_path'
op|','
name|'force'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_check_mapping
dedent|''
dedent|''
name|'def'
name|'test_check_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_check_smb_mapping'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remake_unavailable_mapping
dedent|''
name|'def'
name|'test_remake_unavailable_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_check_smb_mapping'
op|'('
name|'existing_mappings'
op|'='
name|'True'
op|','
nl|'\n'
name|'share_available'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_available_mapping
dedent|''
name|'def'
name|'test_available_mapping'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_check_smb_mapping'
op|'('
name|'existing_mappings'
op|'='
name|'True'
op|','
nl|'\n'
name|'share_available'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_mount_smb_share
dedent|''
name|'def'
name|'test_mount_smb_share'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_create'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'_smb_conn'
op|'.'
name|'Msft_SmbMapping'
op|'.'
name|'Create'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'mount_smb_share'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'share_path'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'username'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'password'
op|')'
newline|'\n'
name|'fake_create'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'RemotePath'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'share_path'
op|','
nl|'\n'
name|'UserName'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'username'
op|','
nl|'\n'
name|'Password'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'password'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_unmount_smb_share
dedent|''
name|'def'
name|'_test_unmount_smb_share'
op|'('
name|'self'
op|','
name|'force'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_mapping'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'smb_mapping_class'
op|'='
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'_smb_conn'
op|'.'
name|'Msft_SmbMapping'
newline|'\n'
name|'smb_mapping_class'
op|'.'
name|'return_value'
op|'='
op|'['
name|'fake_mapping'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'unmount_smb_share'
op|'('
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'share_path'
op|','
nl|'\n'
name|'force'
op|')'
newline|'\n'
nl|'\n'
name|'smb_mapping_class'
op|'.'
name|'assert_called_once_with'
op|'('
nl|'\n'
name|'RemotePath'
op|'='
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'share_path'
op|')'
newline|'\n'
name|'fake_mapping'
op|'.'
name|'Remove'
op|'.'
name|'assert_called_once_with'
op|'('
name|'Force'
op|'='
name|'force'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_soft_unmount_smb_share
dedent|''
name|'def'
name|'test_soft_unmount_smb_share'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_unmount_smb_share'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_force_unmount_smb_share
dedent|''
name|'def'
name|'test_force_unmount_smb_share'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_unmount_smb_share'
op|'('
name|'force'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.path.join'"
op|')'
newline|'\n'
DECL|member|test_get_instances_sub_dir
name|'def'
name|'test_get_instances_sub_dir'
op|'('
name|'self'
op|','
name|'fake_path_join'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|class|WindowsError
indent|'        '
name|'class'
name|'WindowsError'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'            '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'winerror'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'winerror'
op|'='
name|'winerror'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'fake_dir_name'
op|'='
string|'"fake_dir_name"'
newline|'\n'
name|'fake_windows_error'
op|'='
name|'WindowsError'
newline|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'_check_create_dir'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
nl|'\n'
DECL|variable|side_effect
name|'side_effect'
op|'='
name|'WindowsError'
op|'('
name|'pathutils'
op|'.'
name|'ERROR_INVALID_NAME'
op|')'
op|')'
newline|'\n'
name|'with'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'__builtin__.WindowsError'"
op|','
nl|'\n'
name|'fake_windows_error'
op|','
name|'create'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'vmutils'
op|'.'
name|'HyperVException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_pathutils'
op|'.'
name|'_get_instances_sub_dir'
op|','
nl|'\n'
name|'fake_dir_name'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
