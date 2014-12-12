begin_unit
comment|'# Copyright 2014 Cloudbase Solutions Srl'
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
name|'mock'
newline|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
nl|'\n'
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
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'remotefs'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoteFSTestCase
name|'class'
name|'RemoteFSTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Remote filesystem operations test case."""'
newline|'\n'
nl|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
DECL|member|_test_mount_share
name|'def'
name|'_test_mount_share'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'already_mounted'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'already_mounted'
op|':'
newline|'\n'
indent|'            '
name|'err_msg'
op|'='
string|"'Device or resource busy'"
newline|'\n'
name|'mock_execute'
op|'.'
name|'side_effect'
op|'='
op|'['
nl|'\n'
name|'None'
op|','
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
name|'err_msg'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'remotefs'
op|'.'
name|'mount_share'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_path'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_type'
op|','
nl|'\n'
name|'options'
op|'='
op|'['
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_options'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mock_execute'
op|'.'
name|'assert_any_call'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|')'
newline|'\n'
name|'mock_execute'
op|'.'
name|'assert_any_call'
op|'('
string|"'mount'"
op|','
string|"'-t'"
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_type'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_options'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_path'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_mount_new_share
dedent|''
name|'def'
name|'test_mount_new_share'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_mount_share'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_mount_already_mounted_share
dedent|''
name|'def'
name|'test_mount_already_mounted_share'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_mount_share'
op|'('
name|'already_mounted'
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
op|'.'
name|'object'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
DECL|member|test_unmount_share
name|'def'
name|'test_unmount_share'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remotefs'
op|'.'
name|'unmount_share'
op|'('
nl|'\n'
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'export_path'
op|')'
newline|'\n'
nl|'\n'
name|'mock_execute'
op|'.'
name|'assert_any_call'
op|'('
string|"'umount'"
op|','
name|'mock'
op|'.'
name|'sentinel'
op|'.'
name|'mount_path'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'attempts'
op|'='
number|'3'
op|','
nl|'\n'
name|'delay_on_retry'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
