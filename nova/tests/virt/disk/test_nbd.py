begin_unit
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
name|'os'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'fixtures'
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
name|'disk'
op|'.'
name|'mount'
name|'import'
name|'nbd'
newline|'\n'
nl|'\n'
DECL|variable|ORIG_EXISTS
name|'ORIG_EXISTS'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
newline|'\n'
DECL|variable|ORIG_LISTDIR
name|'ORIG_LISTDIR'
op|'='
name|'os'
op|'.'
name|'listdir'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_exists_no_users
name|'def'
name|'_fake_exists_no_users'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/sys/block/nbd'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
op|'.'
name|'endswith'
op|'('
string|"'pid'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'ORIG_EXISTS'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_listdir_nbd_devices
dedent|''
name|'def'
name|'_fake_listdir_nbd_devices'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/sys/block'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
string|"'nbd0'"
op|','
string|"'nbd1'"
op|']'
newline|'\n'
dedent|''
name|'return'
name|'ORIG_LISTDIR'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_exists_all_used
dedent|''
name|'def'
name|'_fake_exists_all_used'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/sys/block/nbd'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'ORIG_EXISTS'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_detect_nbd_devices_none
dedent|''
name|'def'
name|'_fake_detect_nbd_devices_none'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_detect_nbd_devices
dedent|''
name|'def'
name|'_fake_detect_nbd_devices'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'['
string|"'nbd0'"
op|','
string|"'nbd1'"
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fake_noop
dedent|''
name|'def'
name|'_fake_noop'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NbdTestCase
dedent|''
name|'class'
name|'NbdTestCase'
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
name|'NbdTestCase'
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
op|'.'
name|'Set'
op|'('
name|'nbd'
op|'.'
name|'NbdMount'
op|','
string|"'_detect_nbd_devices'"
op|','
nl|'\n'
name|'_fake_detect_nbd_devices'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.listdir'"
op|','
nl|'\n'
name|'_fake_listdir_nbd_devices'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_nbd_no_devices
dedent|''
name|'def'
name|'test_nbd_no_devices'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nbd'
op|'.'
name|'NbdMount'
op|','
string|"'_detect_nbd_devices'"
op|','
nl|'\n'
name|'_fake_detect_nbd_devices_none'
op|')'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'n'
op|'.'
name|'_allocate_nbd'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_nbd_no_free_devices
dedent|''
name|'def'
name|'test_nbd_no_free_devices'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'_fake_exists_all_used'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'n'
op|'.'
name|'_allocate_nbd'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_nbd_not_loaded
dedent|''
name|'def'
name|'test_nbd_not_loaded'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
nl|'\n'
comment|'# Fake out os.path.exists'
nl|'\n'
DECL|function|fake_exists
name|'def'
name|'fake_exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/sys/block/nbd'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'ORIG_EXISTS'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
name|'fake_exists'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# This should fail, as we don\'t have the module "loaded"'
nl|'\n'
comment|'# TODO(mikal): work out how to force english as the gettext language'
nl|'\n'
comment|'# so that the error check always passes'
nl|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'n'
op|'.'
name|'_allocate_nbd'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'nbd unavailable: module not loaded'"
op|','
name|'n'
op|'.'
name|'error'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_nbd_allocation
dedent|''
name|'def'
name|'test_nbd_allocation'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'_fake_exists_no_users'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'random.shuffle'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Allocate a nbd device'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'/dev/nbd0'"
op|','
name|'n'
op|'.'
name|'_allocate_nbd'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_nbd_allocation_one_in_use
dedent|''
name|'def'
name|'test_nbd_allocation_one_in_use'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'random.shuffle'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Fake out os.path.exists'
nl|'\n'
DECL|function|fake_exists
name|'def'
name|'fake_exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/sys/block/nbd'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'path'
op|'=='
string|"'/sys/block/nbd0/pid'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'path'
op|'.'
name|'endswith'
op|'('
string|"'pid'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'ORIG_EXISTS'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
name|'fake_exists'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Allocate a nbd device, should not be the in use one'
nl|'\n'
comment|'# TODO(mikal): Note that there is a leak here, as the in use nbd device'
nl|'\n'
comment|'# is removed from the list, but not returned so it will never be'
nl|'\n'
comment|'# re-added. I will fix this in a later patch.'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'/dev/nbd1'"
op|','
name|'n'
op|'.'
name|'_allocate_nbd'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inner_get_dev_no_devices
dedent|''
name|'def'
name|'test_inner_get_dev_no_devices'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nbd'
op|'.'
name|'NbdMount'
op|','
string|"'_detect_nbd_devices'"
op|','
nl|'\n'
name|'_fake_detect_nbd_devices_none'
op|')'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'n'
op|'.'
name|'_inner_get_dev'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inner_get_dev_qemu_fails
dedent|''
name|'def'
name|'test_inner_get_dev_qemu_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'_fake_exists_no_users'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# We have a trycmd that always fails'
nl|'\n'
DECL|function|fake_trycmd
name|'def'
name|'fake_trycmd'
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
name|'return'
string|"''"
op|','
string|"'broken'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.trycmd'"
op|','
name|'fake_trycmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Error logged, no device consumed'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'n'
op|'.'
name|'_inner_get_dev'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'n'
op|'.'
name|'error'
op|'.'
name|'startswith'
op|'('
string|"'qemu-nbd error'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inner_get_dev_qemu_timeout
dedent|''
name|'def'
name|'test_inner_get_dev_qemu_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'_fake_exists_no_users'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# We have a trycmd that always passed'
nl|'\n'
DECL|function|fake_trycmd
name|'def'
name|'fake_trycmd'
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
name|'return'
string|"''"
op|','
string|"''"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.trycmd'"
op|','
name|'fake_trycmd'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'time.sleep'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Error logged, no device consumed'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'n'
op|'.'
name|'_inner_get_dev'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'n'
op|'.'
name|'error'
op|'.'
name|'endswith'
op|'('
string|"'did not show up'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_exists_one
dedent|''
name|'def'
name|'fake_exists_one'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
comment|'# We need the pid file for the device which is allocated to exist, but'
nl|'\n'
comment|'# only once it is allocated to us'
nl|'\n'
indent|'        '
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/sys/block/nbd'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path'
op|'=='
string|"'/sys/block/nbd1/pid'"
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'path'
op|'.'
name|'endswith'
op|'('
string|"'pid'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'ORIG_EXISTS'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_trycmd_creates_pid
dedent|''
name|'def'
name|'fake_trycmd_creates_pid'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_exists_two
indent|'        '
name|'def'
name|'fake_exists_two'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path'
op|'.'
name|'startswith'
op|'('
string|"'/sys/block/nbd'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'path'
op|'=='
string|"'/sys/block/nbd0/pid'"
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'path'
op|'.'
name|'endswith'
op|'('
string|"'pid'"
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'return'
name|'ORIG_EXISTS'
op|'('
name|'path'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'fake_exists_two'
op|')'
op|')'
newline|'\n'
name|'return'
string|"''"
op|','
string|"''"
newline|'\n'
nl|'\n'
DECL|member|test_inner_get_dev_works
dedent|''
name|'def'
name|'test_inner_get_dev_works'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'random.shuffle'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_exists_one'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.trycmd'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_trycmd_creates_pid'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.execute'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# No error logged, device consumed'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'n'
op|'.'
name|'_inner_get_dev'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'n'
op|'.'
name|'linked'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'n'
op|'.'
name|'error'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'/dev/nbd0'"
op|','
name|'n'
op|'.'
name|'device'
op|')'
newline|'\n'
nl|'\n'
comment|'# Free'
nl|'\n'
name|'n'
op|'.'
name|'unget_dev'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'n'
op|'.'
name|'linked'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'n'
op|'.'
name|'error'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'n'
op|'.'
name|'device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unget_dev_simple
dedent|''
name|'def'
name|'test_unget_dev_simple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|"# This test is just checking we don't get an exception when we unget"
nl|'\n'
comment|"# something we don't have"
nl|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.execute'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
name|'n'
op|'.'
name|'unget_dev'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dev
dedent|''
name|'def'
name|'test_get_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'random.shuffle'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.execute'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_exists_one'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.trycmd'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_trycmd_creates_pid'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# No error logged, device consumed'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'n'
op|'.'
name|'get_dev'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'n'
op|'.'
name|'linked'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'n'
op|'.'
name|'error'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'/dev/nbd0'"
op|','
name|'n'
op|'.'
name|'device'
op|')'
newline|'\n'
nl|'\n'
comment|'# Free'
nl|'\n'
name|'n'
op|'.'
name|'unget_dev'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'n'
op|'.'
name|'linked'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"''"
op|','
name|'n'
op|'.'
name|'error'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertIsNone'
op|'('
name|'n'
op|'.'
name|'device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_dev_timeout
dedent|''
name|'def'
name|'test_get_dev_timeout'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Always fail to get a device'
nl|'\n'
DECL|function|fake_get_dev_fails
indent|'        '
name|'def'
name|'fake_get_dev_fails'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nbd'
op|'.'
name|'NbdMount'
op|','
string|"'_inner_get_dev'"
op|','
name|'fake_get_dev_fails'
op|')'
newline|'\n'
nl|'\n'
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'random.shuffle'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'time.sleep'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.execute'"
op|','
name|'_fake_noop'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_exists_one'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.trycmd'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'fake_trycmd_creates_pid'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
op|'('
string|"'nova.virt.disk.mount.api.'"
nl|'\n'
string|"'MAX_DEVICE_WAIT'"
op|')'
op|','
op|'-'
number|'10'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# No error logged, device consumed'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'n'
op|'.'
name|'get_dev'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_do_mount_need_to_specify_fs_type
dedent|''
name|'def'
name|'test_do_mount_need_to_specify_fs_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mikal): Bug 1094373 saw a regression where we failed to'
nl|'\n'
comment|'# communicate a failed mount properly.'
nl|'\n'
DECL|function|fake_trycmd
indent|'        '
name|'def'
name|'fake_trycmd'
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
name|'return'
string|"''"
op|','
string|"'broken'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.trycmd'"
op|','
name|'fake_trycmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'imgfile'
op|'='
name|'tempfile'
op|'.'
name|'NamedTemporaryFile'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'addCleanup'
op|'('
name|'imgfile'
op|'.'
name|'close'
op|')'
newline|'\n'
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'mount'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'imgfile'
op|'.'
name|'name'
op|','
name|'tempdir'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_returns_true
name|'def'
name|'fake_returns_true'
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
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'mount'
op|'.'
name|'get_dev'
op|'='
name|'fake_returns_true'
newline|'\n'
name|'mount'
op|'.'
name|'map_dev'
op|'='
name|'fake_returns_true'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mount'
op|'.'
name|'do_mount'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_device_creation_race
dedent|''
name|'def'
name|'test_device_creation_race'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Make sure that even if two threads create instances at the same time'
nl|'\n'
comment|'# they cannot choose the same nbd number (see bug 1207422)'
nl|'\n'
nl|'\n'
indent|'        '
name|'tempdir'
op|'='
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'TempDir'
op|'('
op|')'
op|')'
op|'.'
name|'path'
newline|'\n'
name|'free_devices'
op|'='
name|'_fake_detect_nbd_devices'
op|'('
name|'None'
op|')'
op|'['
op|':'
op|']'
newline|'\n'
name|'chosen_devices'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_find_unused
name|'def'
name|'fake_find_unused'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'/dev'"
op|','
name|'free_devices'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|function|delay_and_remove_device
dedent|''
name|'def'
name|'delay_and_remove_device'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# Ensure that context switch happens before the device is marked'
nl|'\n'
comment|'# as used. This will cause a failure without nbd-allocation-lock'
nl|'\n'
comment|'# in place.'
nl|'\n'
indent|'            '
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.1'
op|')'
newline|'\n'
nl|'\n'
comment|'# We always choose the top device in find_unused - remove it now.'
nl|'\n'
name|'free_devices'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'return'
string|"''"
op|','
string|"''"
newline|'\n'
nl|'\n'
DECL|function|pid_exists
dedent|''
name|'def'
name|'pid_exists'
op|'('
name|'pidfile'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'pidfile'
name|'not'
name|'in'
op|'['
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'/sys/block'"
op|','
name|'dev'
op|','
string|"'pid'"
op|')'
nl|'\n'
name|'for'
name|'dev'
name|'in'
name|'free_devices'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nbd'
op|'.'
name|'NbdMount'
op|','
string|"'_allocate_nbd'"
op|','
name|'fake_find_unused'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'nova.utils.trycmd'"
op|','
nl|'\n'
name|'delay_and_remove_device'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
string|"'os.path.exists'"
op|','
nl|'\n'
name|'pid_exists'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|function|get_a_device
name|'def'
name|'get_a_device'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'n'
op|'='
name|'nbd'
op|'.'
name|'NbdMount'
op|'('
name|'None'
op|','
name|'tempdir'
op|')'
newline|'\n'
name|'n'
op|'.'
name|'get_dev'
op|'('
op|')'
newline|'\n'
name|'chosen_devices'
op|'.'
name|'append'
op|'('
name|'n'
op|'.'
name|'device'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'thread1'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'get_a_device'
op|')'
newline|'\n'
name|'thread2'
op|'='
name|'eventlet'
op|'.'
name|'spawn'
op|'('
name|'get_a_device'
op|')'
newline|'\n'
name|'thread1'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'thread2'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'2'
op|','
name|'len'
op|'('
name|'chosen_devices'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertNotEqual'
op|'('
name|'chosen_devices'
op|'['
number|'0'
op|']'
op|','
name|'chosen_devices'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
