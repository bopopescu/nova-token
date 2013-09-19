begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright (c) 2012 NTT DOCOMO, INC.'
nl|'\n'
comment|'#    Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'#    Copyright 2011 Ilya Alekseyev'
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
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'mox'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'cmd'
name|'import'
name|'baremetal_deploy_helper'
name|'as'
name|'bmdh'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'base'
name|'as'
name|'bm_db_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
name|'as'
name|'bm_db'
newline|'\n'
nl|'\n'
name|'bmdh'
op|'.'
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.virt.baremetal.deploy_helper'"
op|')'
newline|'\n'
nl|'\n'
name|'_PXECONF_DEPLOY'
op|'='
string|'"""\ndefault deploy\n\nlabel deploy\nkernel deploy_kernel\nappend initrd=deploy_ramdisk\nipappend 3\n\nlabel boot\nkernel kernel\nappend initrd=ramdisk root=${ROOT}\n"""'
newline|'\n'
nl|'\n'
name|'_PXECONF_BOOT'
op|'='
string|'"""\ndefault boot\n\nlabel deploy\nkernel deploy_kernel\nappend initrd=deploy_ramdisk\nipappend 3\n\nlabel boot\nkernel kernel\nappend initrd=ramdisk root=UUID=12345678-1234-1234-1234-1234567890abcdef\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|WorkerTestCase
name|'class'
name|'WorkerTestCase'
op|'('
name|'bm_db_base'
op|'.'
name|'BMDBTestCase'
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
name|'WorkerTestCase'
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
name|'worker'
op|'='
name|'bmdh'
op|'.'
name|'Worker'
op|'('
op|')'
newline|'\n'
comment|'# Make tearDown() fast'
nl|'\n'
name|'self'
op|'.'
name|'worker'
op|'.'
name|'queue_timeout'
op|'='
number|'0.1'
newline|'\n'
name|'self'
op|'.'
name|'worker'
op|'.'
name|'start'
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
name|'if'
name|'self'
op|'.'
name|'worker'
op|'.'
name|'isAlive'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'worker'
op|'.'
name|'stop'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'worker'
op|'.'
name|'join'
op|'('
name|'timeout'
op|'='
number|'1'
op|')'
newline|'\n'
dedent|''
name|'super'
op|'('
name|'WorkerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|wait_queue_empty
dedent|''
name|'def'
name|'wait_queue_empty'
op|'('
name|'self'
op|','
name|'timeout'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'_'
name|'in'
name|'xrange'
op|'('
name|'int'
op|'('
name|'timeout'
op|'/'
number|'0.1'
op|')'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'bmdh'
op|'.'
name|'QUEUE'
op|'.'
name|'empty'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'break'
newline|'\n'
dedent|''
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_run_calls_deploy
dedent|''
dedent|''
name|'def'
name|'test_run_calls_deploy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check all queued requests are passed to deploy()."""'
newline|'\n'
name|'history'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_deploy
name|'def'
name|'fake_deploy'
op|'('
op|'**'
name|'params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'history'
op|'.'
name|'append'
op|'('
name|'params'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'bmdh'
op|','
string|"'deploy'"
op|','
name|'fake_deploy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bm_db'
op|','
string|"'bm_node_update'"
op|')'
newline|'\n'
comment|'# update is called twice inside Worker.run'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'6'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bm_db'
op|'.'
name|'bm_node_update'
op|'('
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
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'params_list'
op|'='
op|'['
op|'{'
string|"'fake1'"
op|':'
string|"''"
op|'}'
op|','
op|'{'
string|"'fake2'"
op|':'
string|"''"
op|'}'
op|','
op|'{'
string|"'fake3'"
op|':'
string|"''"
op|'}'
op|']'
newline|'\n'
name|'for'
op|'('
name|'dep_id'
op|','
name|'params'
op|')'
name|'in'
name|'enumerate'
op|'('
name|'params_list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bmdh'
op|'.'
name|'QUEUE'
op|'.'
name|'put'
op|'('
op|'('
name|'dep_id'
op|','
name|'params'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'wait_queue_empty'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'params_list'
op|','
name|'history'
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
DECL|member|test_run_with_failing_deploy
dedent|''
name|'def'
name|'test_run_with_failing_deploy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check a worker keeps on running even if deploy() raises\n        an exception.\n        """'
newline|'\n'
name|'history'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|fake_deploy
name|'def'
name|'fake_deploy'
op|'('
op|'**'
name|'params'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'history'
op|'.'
name|'append'
op|'('
name|'params'
op|')'
newline|'\n'
comment|'# always fail'
nl|'\n'
name|'raise'
name|'Exception'
op|'('
string|"'test'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'bmdh'
op|','
string|"'deploy'"
op|','
name|'fake_deploy'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bm_db'
op|','
string|"'bm_node_update'"
op|')'
newline|'\n'
comment|'# update is called twice inside Worker.run'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
number|'6'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bm_db'
op|'.'
name|'bm_node_update'
op|'('
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
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'params_list'
op|'='
op|'['
op|'{'
string|"'fake1'"
op|':'
string|"''"
op|'}'
op|','
op|'{'
string|"'fake2'"
op|':'
string|"''"
op|'}'
op|','
op|'{'
string|"'fake3'"
op|':'
string|"''"
op|'}'
op|']'
newline|'\n'
name|'for'
op|'('
name|'dep_id'
op|','
name|'params'
op|')'
name|'in'
name|'enumerate'
op|'('
name|'params_list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'bmdh'
op|'.'
name|'QUEUE'
op|'.'
name|'put'
op|'('
op|'('
name|'dep_id'
op|','
name|'params'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'wait_queue_empty'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'params_list'
op|','
name|'history'
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
nl|'\n'
DECL|class|PhysicalWorkTestCase
dedent|''
dedent|''
name|'class'
name|'PhysicalWorkTestCase'
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
name|'PhysicalWorkTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|function|noop
name|'def'
name|'noop'
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
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'time'
op|','
string|"'sleep'"
op|','
name|'noop'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deploy
dedent|''
name|'def'
name|'test_deploy'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check loosely all functions are called with right args."""'
newline|'\n'
name|'address'
op|'='
string|"'127.0.0.1'"
newline|'\n'
name|'port'
op|'='
number|'3306'
newline|'\n'
name|'iqn'
op|'='
string|"'iqn.xyz'"
newline|'\n'
name|'lun'
op|'='
number|'1'
newline|'\n'
name|'image_path'
op|'='
string|"'/tmp/xyz/image'"
newline|'\n'
name|'pxe_config_path'
op|'='
string|"'/tmp/abc/pxeconfig'"
newline|'\n'
name|'root_mb'
op|'='
number|'128'
newline|'\n'
name|'swap_mb'
op|'='
number|'64'
newline|'\n'
nl|'\n'
name|'dev'
op|'='
string|"'/dev/fake'"
newline|'\n'
name|'root_part'
op|'='
string|"'/dev/fake-part1'"
newline|'\n'
name|'swap_part'
op|'='
string|"'/dev/fake-part2'"
newline|'\n'
name|'root_uuid'
op|'='
string|"'12345678-1234-1234-12345678-12345678abcdef'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'get_dev'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'get_image_mb'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'discovery'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'login_iscsi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'logout_iscsi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'make_partitions'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'is_block_device'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'dd'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'mkswap'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'block_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'switch_pxe_config'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'notify'"
op|')'
newline|'\n'
nl|'\n'
name|'bmdh'
op|'.'
name|'get_dev'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|','
name|'lun'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'get_image_mb'
op|'('
name|'image_path'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'1'
op|')'
comment|'# < root_mb'
newline|'\n'
name|'bmdh'
op|'.'
name|'discovery'
op|'('
name|'address'
op|','
name|'port'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'login_iscsi'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'is_block_device'
op|'('
name|'dev'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'make_partitions'
op|'('
name|'dev'
op|','
name|'root_mb'
op|','
name|'swap_mb'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'is_block_device'
op|'('
name|'root_part'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'is_block_device'
op|'('
name|'swap_part'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'dd'
op|'('
name|'image_path'
op|','
name|'root_part'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'mkswap'
op|'('
name|'swap_part'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'block_uuid'
op|'('
name|'root_part'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'root_uuid'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'logout_iscsi'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'switch_pxe_config'
op|'('
name|'pxe_config_path'
op|','
name|'root_uuid'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'notify'
op|'('
name|'address'
op|','
number|'10000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'bmdh'
op|'.'
name|'deploy'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|','
name|'lun'
op|','
name|'image_path'
op|','
name|'pxe_config_path'
op|','
nl|'\n'
name|'root_mb'
op|','
name|'swap_mb'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_always_logout_iscsi
dedent|''
name|'def'
name|'test_always_logout_iscsi'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""logout_iscsi() must be called once login_iscsi() is called."""'
newline|'\n'
name|'address'
op|'='
string|"'127.0.0.1'"
newline|'\n'
name|'port'
op|'='
number|'3306'
newline|'\n'
name|'iqn'
op|'='
string|"'iqn.xyz'"
newline|'\n'
name|'lun'
op|'='
number|'1'
newline|'\n'
name|'image_path'
op|'='
string|"'/tmp/xyz/image'"
newline|'\n'
name|'pxe_config_path'
op|'='
string|"'/tmp/abc/pxeconfig'"
newline|'\n'
name|'root_mb'
op|'='
number|'128'
newline|'\n'
name|'swap_mb'
op|'='
number|'64'
newline|'\n'
nl|'\n'
name|'dev'
op|'='
string|"'/dev/fake'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'get_dev'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'get_image_mb'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'discovery'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'login_iscsi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'logout_iscsi'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bmdh'
op|','
string|"'work_on_disk'"
op|')'
newline|'\n'
nl|'\n'
DECL|class|TestException
name|'class'
name|'TestException'
op|'('
name|'Exception'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'bmdh'
op|'.'
name|'get_dev'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|','
name|'lun'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'dev'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'get_image_mb'
op|'('
name|'image_path'
op|')'
op|'.'
name|'AndReturn'
op|'('
number|'1'
op|')'
comment|'# < root_mb'
newline|'\n'
name|'bmdh'
op|'.'
name|'discovery'
op|'('
name|'address'
op|','
name|'port'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'login_iscsi'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'work_on_disk'
op|'('
name|'dev'
op|','
name|'root_mb'
op|','
name|'swap_mb'
op|','
name|'image_path'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'TestException'
op|')'
newline|'\n'
name|'bmdh'
op|'.'
name|'logout_iscsi'
op|'('
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'TestException'
op|','
nl|'\n'
name|'bmdh'
op|'.'
name|'deploy'
op|','
nl|'\n'
name|'address'
op|','
name|'port'
op|','
name|'iqn'
op|','
name|'lun'
op|','
name|'image_path'
op|','
nl|'\n'
name|'pxe_config_path'
op|','
name|'root_mb'
op|','
name|'swap_mb'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SwitchPxeConfigTestCase
dedent|''
dedent|''
name|'class'
name|'SwitchPxeConfigTestCase'
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
name|'SwitchPxeConfigTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
op|'('
name|'fd'
op|','
name|'self'
op|'.'
name|'fname'
op|')'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'write'
op|'('
name|'fd'
op|','
name|'_PXECONF_DEPLOY'
op|')'
newline|'\n'
name|'os'
op|'.'
name|'close'
op|'('
name|'fd'
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
name|'os'
op|'.'
name|'unlink'
op|'('
name|'self'
op|'.'
name|'fname'
op|')'
newline|'\n'
name|'super'
op|'('
name|'SwitchPxeConfigTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_switch_pxe_config
dedent|''
name|'def'
name|'test_switch_pxe_config'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'bmdh'
op|'.'
name|'switch_pxe_config'
op|'('
name|'self'
op|'.'
name|'fname'
op|','
nl|'\n'
string|"'12345678-1234-1234-1234-1234567890abcdef'"
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'self'
op|'.'
name|'fname'
op|','
string|"'r'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'pxeconf'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'pxeconf'
op|','
name|'_PXECONF_BOOT'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|OtherFunctionTestCase
dedent|''
dedent|''
name|'class'
name|'OtherFunctionTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_get_dev
indent|'    '
name|'def'
name|'test_get_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected'
op|'='
string|"'/dev/disk/by-path/ip-1.2.3.4:5678-iscsi-iqn.fake-lun-9'"
newline|'\n'
name|'actual'
op|'='
name|'bmdh'
op|'.'
name|'get_dev'
op|'('
string|"'1.2.3.4'"
op|','
number|'5678'
op|','
string|"'iqn.fake'"
op|','
number|'9'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'expected'
op|','
name|'actual'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_image_mb
dedent|''
name|'def'
name|'test_get_image_mb'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mb'
op|'='
number|'1024'
op|'*'
number|'1024'
newline|'\n'
name|'size'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|function|fake_getsize
name|'def'
name|'fake_getsize'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'size'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|'.'
name|'path'
op|','
string|"'getsize'"
op|','
name|'fake_getsize'
op|')'
newline|'\n'
name|'size'
op|'='
number|'0'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bmdh'
op|'.'
name|'get_image_mb'
op|'('
string|"'x'"
op|')'
op|','
number|'0'
op|')'
newline|'\n'
name|'size'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bmdh'
op|'.'
name|'get_image_mb'
op|'('
string|"'x'"
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'size'
op|'='
name|'mb'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bmdh'
op|'.'
name|'get_image_mb'
op|'('
string|"'x'"
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'size'
op|'='
name|'mb'
op|'+'
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'bmdh'
op|'.'
name|'get_image_mb'
op|'('
string|"'x'"
op|')'
op|','
number|'2'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
