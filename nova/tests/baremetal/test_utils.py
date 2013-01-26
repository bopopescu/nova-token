begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# coding=utf-8'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Hewlett-Packard Development Company, L.P.'
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
string|'"""Tests for baremetal utils."""'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'import'
name|'errno'
newline|'\n'
name|'import'
name|'os'
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
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalUtilsTestCase
name|'class'
name|'BareMetalUtilsTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_random_alnum
indent|'    '
name|'def'
name|'test_random_alnum'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'s'
op|'='
name|'utils'
op|'.'
name|'random_alnum'
op|'('
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'s'
op|')'
op|','
number|'10'
op|')'
newline|'\n'
name|'s'
op|'='
name|'utils'
op|'.'
name|'random_alnum'
op|'('
number|'100'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'s'
op|')'
op|','
number|'100'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlink
dedent|''
name|'def'
name|'test_unlink'
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
name|'os'
op|','
string|'"unlink"'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
string|'"/fake/path"'
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
name|'utils'
op|'.'
name|'unlink_without_raise'
op|'('
string|'"/fake/path"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unlink_ENOENT
dedent|''
name|'def'
name|'test_unlink_ENOENT'
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
name|'os'
op|','
string|'"unlink"'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'unlink'
op|'('
string|'"/fake/path"'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'OSError'
op|'('
name|'errno'
op|'.'
name|'ENOENT'
op|')'
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
name|'utils'
op|'.'
name|'unlink_without_raise'
op|'('
string|'"/fake/path"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_link
dedent|''
name|'def'
name|'test_create_link'
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
name|'os'
op|','
string|'"symlink"'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'symlink'
op|'('
string|'"/fake/source"'
op|','
string|'"/fake/link"'
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
name|'utils'
op|'.'
name|'create_link_without_raise'
op|'('
string|'"/fake/source"'
op|','
string|'"/fake/link"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_link_EEXIST
dedent|''
name|'def'
name|'test_create_link_EEXIST'
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
name|'os'
op|','
string|'"symlink"'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'symlink'
op|'('
string|'"/fake/source"'
op|','
string|'"/fake/link"'
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'OSError'
op|'('
name|'errno'
op|'.'
name|'EEXIST'
op|')'
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
name|'utils'
op|'.'
name|'create_link_without_raise'
op|'('
string|'"/fake/source"'
op|','
string|'"/fake/link"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
