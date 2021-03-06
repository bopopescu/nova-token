begin_unit
comment|'# Copyright (c) 2014 The Johns Hopkins University/Applied Physics Laboratory'
nl|'\n'
comment|'# All Rights Reserved'
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
nl|'\n'
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
op|'.'
name|'virt'
op|'.'
name|'libvirt'
op|'.'
name|'storage'
name|'import'
name|'dmcrypt'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtDmcryptTestCase
name|'class'
name|'LibvirtDmcryptTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
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
name|'LibvirtDmcryptTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'CIPHER'
op|'='
string|"'cipher'"
newline|'\n'
name|'self'
op|'.'
name|'KEY_SIZE'
op|'='
number|'256'
newline|'\n'
name|'self'
op|'.'
name|'NAME'
op|'='
string|"'disk'"
newline|'\n'
name|'self'
op|'.'
name|'TARGET'
op|'='
name|'dmcrypt'
op|'.'
name|'volume_name'
op|'('
name|'self'
op|'.'
name|'NAME'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'PATH'
op|'='
string|"'/dev/nova-lvm/instance_disk'"
newline|'\n'
name|'self'
op|'.'
name|'KEY'
op|'='
name|'range'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'KEY_SIZE'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'KEY_STR'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
op|'['
string|'"%02x"'
op|'%'
name|'x'
name|'for'
name|'x'
name|'in'
name|'range'
op|'('
number|'0'
op|','
name|'self'
op|'.'
name|'KEY_SIZE'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_create_volume
name|'def'
name|'test_create_volume'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dmcrypt'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'TARGET'
op|','
name|'self'
op|'.'
name|'PATH'
op|','
name|'self'
op|'.'
name|'CIPHER'
op|','
nl|'\n'
name|'self'
op|'.'
name|'KEY_SIZE'
op|','
name|'self'
op|'.'
name|'KEY'
op|')'
newline|'\n'
nl|'\n'
name|'mock_execute'
op|'.'
name|'assert_has_calls'
op|'('
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'cryptsetup'"
op|','
string|"'create'"
op|','
name|'self'
op|'.'
name|'TARGET'
op|','
name|'self'
op|'.'
name|'PATH'
op|','
nl|'\n'
string|"'--cipher='"
op|'+'
name|'self'
op|'.'
name|'CIPHER'
op|','
nl|'\n'
string|"'--key-size='"
op|'+'
name|'str'
op|'('
name|'self'
op|'.'
name|'KEY_SIZE'
op|')'
op|','
nl|'\n'
string|"'--key-file=-'"
op|','
name|'process_input'
op|'='
name|'self'
op|'.'
name|'KEY_STR'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.libvirt.storage.dmcrypt.LOG'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_create_volume_fail
name|'def'
name|'test_create_volume_fail'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_log'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_execute'
op|'.'
name|'side_effect'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|','
nl|'\n'
name|'dmcrypt'
op|'.'
name|'create_volume'
op|','
name|'self'
op|'.'
name|'TARGET'
op|','
name|'self'
op|'.'
name|'PATH'
op|','
nl|'\n'
name|'self'
op|'.'
name|'CIPHER'
op|','
name|'self'
op|'.'
name|'KEY_SIZE'
op|','
name|'self'
op|'.'
name|'KEY'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_execute'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_log'
op|'.'
name|'error'
op|'.'
name|'call_count'
op|')'
comment|'# error logged'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_delete_volume
name|'def'
name|'test_delete_volume'
op|'('
name|'self'
op|','
name|'mock_execute'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dmcrypt'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'TARGET'
op|')'
newline|'\n'
nl|'\n'
name|'mock_execute'
op|'.'
name|'assert_has_calls'
op|'('
op|'['
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'cryptsetup'"
op|','
string|"'remove'"
op|','
name|'self'
op|'.'
name|'TARGET'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.libvirt.storage.dmcrypt.LOG'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_delete_volume_fail
name|'def'
name|'test_delete_volume_fail'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_log'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_execute'
op|'.'
name|'side_effect'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|','
nl|'\n'
name|'dmcrypt'
op|'.'
name|'delete_volume'
op|','
name|'self'
op|'.'
name|'TARGET'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_execute'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_log'
op|'.'
name|'error'
op|'.'
name|'call_count'
op|')'
comment|'# error logged'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.virt.libvirt.storage.dmcrypt.LOG'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'nova.utils.execute'"
op|')'
newline|'\n'
DECL|member|test_delete_missing_volume
name|'def'
name|'test_delete_missing_volume'
op|'('
name|'self'
op|','
name|'mock_execute'
op|','
name|'mock_log'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_execute'
op|'.'
name|'side_effect'
op|'='
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
name|'exit_code'
op|'='
number|'4'
op|')'
newline|'\n'
nl|'\n'
name|'dmcrypt'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'TARGET'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_log'
op|'.'
name|'debug'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'0'
op|','
name|'mock_log'
op|'.'
name|'error'
op|'.'
name|'call_count'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|"'os.listdir'"
op|')'
newline|'\n'
DECL|member|test_list_volumes
name|'def'
name|'test_list_volumes'
op|'('
name|'self'
op|','
name|'mock_listdir'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_listdir'
op|'.'
name|'return_value'
op|'='
op|'['
name|'self'
op|'.'
name|'TARGET'
op|','
string|"'/dev/mapper/disk'"
op|']'
newline|'\n'
name|'encrypted_volumes'
op|'='
name|'dmcrypt'
op|'.'
name|'list_volumes'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'1'
op|','
name|'mock_listdir'
op|'.'
name|'call_count'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
op|'['
name|'self'
op|'.'
name|'TARGET'
op|']'
op|','
name|'encrypted_volumes'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
