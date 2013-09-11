begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2013 The Johns Hopkins University/Applied Physics Laboratory'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'volume'
op|'.'
name|'encryptors'
name|'import'
name|'test_cryptsetup'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'encryptors'
name|'import'
name|'luks'
newline|'\n'
nl|'\n'
nl|'\n'
string|'"""\nThe utility of these test cases is limited given the simplicity of the\nLuksEncryptor class. The attach_volume method has the only significant logic\nto handle cases where the volume has not previously been formatted, but\nexercising this logic requires "real" devices and actually executing the\nvarious cryptsetup commands rather than simply logging them.\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LuksEncryptorTestCase
name|'class'
name|'LuksEncryptorTestCase'
op|'('
name|'test_cryptsetup'
op|'.'
name|'CryptsetupEncryptorTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_create
indent|'    '
name|'def'
name|'_create'
op|'('
name|'self'
op|','
name|'connection_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'luks'
op|'.'
name|'LuksEncryptor'
op|'('
name|'connection_info'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'LuksEncryptorTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__format_volume
dedent|''
name|'def'
name|'test__format_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'encryptor'
op|'.'
name|'_format_volume'
op|'('
string|'"passphrase"'
op|')'
newline|'\n'
nl|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'cryptsetup'"
op|','
string|"'--batch-mode'"
op|','
string|"'luksFormat'"
op|','
nl|'\n'
string|"'--key-file=-'"
op|','
name|'self'
op|'.'
name|'dev_path'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'self'
op|'.'
name|'executes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__open_volume
dedent|''
name|'def'
name|'test__open_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'encryptor'
op|'.'
name|'_open_volume'
op|'('
string|'"passphrase"'
op|')'
newline|'\n'
nl|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'cryptsetup'"
op|','
string|"'luksOpen'"
op|','
string|"'--key-file=-'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'dev_path'
op|','
name|'self'
op|'.'
name|'dev_name'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'self'
op|'.'
name|'executes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_attach_volume
dedent|''
name|'def'
name|'test_attach_volume'
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
name|'Set'
op|'('
name|'self'
op|'.'
name|'encryptor'
op|','
string|"'_get_key'"
op|','
nl|'\n'
name|'test_cryptsetup'
op|'.'
name|'fake__get_key'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'encryptor'
op|'.'
name|'attach_volume'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'cryptsetup'"
op|','
string|"'luksOpen'"
op|','
string|"'--key-file=-'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'dev_path'
op|','
name|'self'
op|'.'
name|'dev_name'
op|')'
op|','
nl|'\n'
op|'('
string|"'ln'"
op|','
string|"'--symbolic'"
op|','
string|"'--force'"
op|','
nl|'\n'
string|"'/dev/mapper/%s'"
op|'%'
name|'self'
op|'.'
name|'dev_name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'symlink_path'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'self'
op|'.'
name|'executes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test__close_volume
dedent|''
name|'def'
name|'test__close_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'encryptor'
op|'.'
name|'detach_volume'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'cryptsetup'"
op|','
string|"'luksClose'"
op|','
name|'self'
op|'.'
name|'dev_name'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'self'
op|'.'
name|'executes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_detach_volume
dedent|''
name|'def'
name|'test_detach_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'encryptor'
op|'.'
name|'detach_volume'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'expected_commands'
op|'='
op|'['
op|'('
string|"'cryptsetup'"
op|','
string|"'luksClose'"
op|','
name|'self'
op|'.'
name|'dev_name'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected_commands'
op|','
name|'self'
op|'.'
name|'executes'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
