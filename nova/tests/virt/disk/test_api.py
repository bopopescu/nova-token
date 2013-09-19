begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
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
name|'tempfile'
newline|'\n'
nl|'\n'
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
name|'import'
name|'api'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APITestCase
name|'class'
name|'APITestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_can_resize_need_fs_type_specified
indent|'    '
name|'def'
name|'test_can_resize_need_fs_type_specified'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(mikal): Bug 1094373 saw a regression where we failed to'
nl|'\n'
comment|'# treat a failure to mount as a failure to be able to resize the'
nl|'\n'
comment|'# filesystem'
nl|'\n'
DECL|function|_fake_get_disk_size
indent|'        '
name|'def'
name|'_fake_get_disk_size'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
number|'10'
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
nl|'\n'
string|"'nova.virt.disk.api.get_disk_size'"
op|','
name|'_fake_get_disk_size'
op|')'
op|')'
newline|'\n'
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
name|'self'
op|'.'
name|'useFixture'
op|'('
name|'fixtures'
op|'.'
name|'MonkeyPatch'
op|'('
nl|'\n'
string|"'nova.virt.disk.mount.nbd.NbdMount.get_dev'"
op|','
nl|'\n'
name|'fake_returns_true'
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
nl|'\n'
string|"'nova.virt.disk.mount.nbd.NbdMount.map_dev'"
op|','
nl|'\n'
name|'fake_returns_true'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Force the use of localfs, which is what was used during the failure'
nl|'\n'
comment|'# reported in the bug'
nl|'\n'
DECL|function|fake_import_fails
name|'def'
name|'fake_import_fails'
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
name|'raise'
name|'Exception'
op|'('
string|"'Failed'"
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
nl|'\n'
string|"'nova.openstack.common.importutils.import_module'"
op|','
nl|'\n'
name|'fake_import_fails'
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
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'api'
op|'.'
name|'is_image_partitionless'
op|'('
name|'imgfile'
op|','
name|'use_cow'
op|'='
name|'True'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
