begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Michael Still and Canonical Inc'
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
name|'import'
name|'mox'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
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
name|'import'
name|'configdrive'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfigDriveTestCase
name|'class'
name|'ConfigDriveTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_create_configdrive_iso
indent|'    '
name|'def'
name|'test_create_configdrive_iso'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'imagefile'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'genisoimage'"
op|','
string|"'-o'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
string|"'-ldots'"
op|','
nl|'\n'
string|"'-allow-lowercase'"
op|','
string|"'-allow-multidot'"
op|','
string|"'-l'"
op|','
nl|'\n'
string|"'-publisher'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
string|"'-quiet'"
op|','
string|"'-J'"
op|','
string|"'-r'"
op|','
nl|'\n'
string|"'-V'"
op|','
string|"'config-2'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'attempts'
op|'='
number|'1'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'False'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
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
name|'with'
name|'configdrive'
op|'.'
name|'ConfigDriveBuilder'
op|'('
op|')'
name|'as'
name|'c'
op|':'
newline|'\n'
indent|'                '
name|'c'
op|'.'
name|'_add_file'
op|'('
string|"'this/is/a/path/hello'"
op|','
string|"'This is some content'"
op|')'
newline|'\n'
op|'('
name|'fd'
op|','
name|'imagefile'
op|')'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
name|'prefix'
op|'='
string|"'cd_iso_'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'close'
op|'('
name|'fd'
op|')'
newline|'\n'
name|'c'
op|'.'
name|'_make_iso9660'
op|'('
name|'imagefile'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check cleanup'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'c'
op|'.'
name|'tempdir'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'imagefile'
op|':'
newline|'\n'
indent|'                '
name|'fileutils'
op|'.'
name|'delete_if_exists'
op|'('
name|'imagefile'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_configdrive_vfat
dedent|''
dedent|''
dedent|''
name|'def'
name|'test_create_configdrive_vfat'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'imagefile'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'mkfs'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'trycmd'"
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'mkfs'
op|'('
string|"'vfat'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'label'
op|'='
string|"'config-2'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'trycmd'
op|'('
string|"'mount'"
op|','
string|"'-o'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
op|'('
name|'None'
op|','
name|'None'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'umount'"
op|','
name|'mox'
op|'.'
name|'IgnoreArg'
op|'('
op|')'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
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
name|'with'
name|'configdrive'
op|'.'
name|'ConfigDriveBuilder'
op|'('
op|')'
name|'as'
name|'c'
op|':'
newline|'\n'
indent|'                '
name|'c'
op|'.'
name|'_add_file'
op|'('
string|"'this/is/a/path/hello'"
op|','
string|"'This is some content'"
op|')'
newline|'\n'
op|'('
name|'fd'
op|','
name|'imagefile'
op|')'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
name|'prefix'
op|'='
string|"'cd_vfat_'"
op|')'
newline|'\n'
name|'os'
op|'.'
name|'close'
op|'('
name|'fd'
op|')'
newline|'\n'
name|'c'
op|'.'
name|'_make_vfat'
op|'('
name|'imagefile'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check cleanup'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'c'
op|'.'
name|'tempdir'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|"# NOTE(mikal): we can't check for a VFAT output here because the"
nl|'\n'
comment|'# filesystem creation stuff has been mocked out because it'
nl|'\n'
comment|'# requires root permissions'
nl|'\n'
nl|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'imagefile'
op|':'
newline|'\n'
indent|'                '
name|'fileutils'
op|'.'
name|'delete_if_exists'
op|'('
name|'imagefile'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
