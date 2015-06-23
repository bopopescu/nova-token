begin_unit
comment|'#    Copyright 2010 OpenStack Foundation'
nl|'\n'
comment|'#    (c) Copyright 2012-2013 Hewlett-Packard Development Company, L.P.'
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
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'storage'
name|'import'
name|'linuxscsi'
newline|'\n'
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
nl|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StorageLinuxSCSITestCase
name|'class'
name|'StorageLinuxSCSITestCase'
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
name|'StorageLinuxSCSITestCase'
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
name|'executes'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'fake_stat_result'
op|'='
name|'os'
op|'.'
name|'stat'
op|'('
name|'__file__'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_execute
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'executes'
op|'.'
name|'append'
op|'('
name|'cmd'
op|')'
newline|'\n'
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
DECL|function|fake_stat
dedent|''
name|'def'
name|'fake_stat'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'fake_stat_result'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|','
string|"'stat'"
op|','
name|'fake_stat'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_multipath_device_3par
dedent|''
name|'def'
name|'test_find_multipath_device_3par'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_execute
indent|'        '
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'out'
op|'='
op|'('
string|'"350002ac20398383d dm-3 3PARdata,VV\\n"'
nl|'\n'
string|'"size=2.0G features=\'0\' hwhandler=\'0\' wp=rw\\n"'
nl|'\n'
string|'"`-+- policy=\'round-robin 0\' prio=-1 status=active\\n"'
nl|'\n'
string|'"  |- 0:0:0:1 sde 8:64 active undef running\\n"'
nl|'\n'
string|'"  `- 2:0:0:1 sdf 8:80 active undef running\\n"'
nl|'\n'
op|')'
newline|'\n'
name|'return'
name|'out'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'linuxscsi'
op|'.'
name|'find_multipath_device'
op|'('
string|"'/dev/sde'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"info = %s"'
op|'%'
name|'info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"350002ac20398383d"'
op|','
name|'info'
op|'['
string|'"name"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"350002ac20398383d"'
op|','
name|'info'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/mapper/350002ac20398383d"'
op|','
name|'info'
op|'['
string|'"device"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sde"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'device'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'channel'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"1"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'lun'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sdf"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'device'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"2"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'channel'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"1"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'lun'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_multipath_device_3par_ufn
dedent|''
name|'def'
name|'test_find_multipath_device_3par_ufn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_execute
indent|'        '
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'out'
op|'='
op|'('
string|'"mpath6 (350002ac20398383d) dm-3 3PARdata,VV\\n"'
nl|'\n'
string|'"size=2.0G features=\'0\' hwhandler=\'0\' wp=rw\\n"'
nl|'\n'
string|'"`-+- policy=\'round-robin 0\' prio=-1 status=active\\n"'
nl|'\n'
string|'"  |- 0:0:0:1 sde 8:64 active undef running\\n"'
nl|'\n'
string|'"  `- 2:0:0:1 sdf 8:80 active undef running\\n"'
nl|'\n'
op|')'
newline|'\n'
name|'return'
name|'out'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'linuxscsi'
op|'.'
name|'find_multipath_device'
op|'('
string|"'/dev/sde'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"info = %s"'
op|'%'
name|'info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"mpath6"'
op|','
name|'info'
op|'['
string|'"name"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"350002ac20398383d"'
op|','
name|'info'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/mapper/mpath6"'
op|','
name|'info'
op|'['
string|'"device"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sde"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'device'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'channel'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"1"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'lun'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sdf"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'device'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"2"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'channel'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"1"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'lun'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_multipath_device_svc
dedent|''
name|'def'
name|'test_find_multipath_device_svc'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_execute
indent|'        '
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'out'
op|'='
op|'('
string|'"36005076da00638089c000000000004d5 dm-2 IBM,2145\\n"'
nl|'\n'
string|'"size=954M features=\'1 queue_if_no_path\' hwhandler=\'0\'"'
nl|'\n'
string|'" wp=rw\\n"'
nl|'\n'
string|'"|-+- policy=\'round-robin 0\' prio=-1 status=active\\n"'
nl|'\n'
string|'"| |- 6:0:2:0 sde 8:64  active undef  running\\n"'
nl|'\n'
string|'"| `- 6:0:4:0 sdg 8:96  active undef  running\\n"'
nl|'\n'
string|'"`-+- policy=\'round-robin 0\' prio=-1 status=enabled\\n"'
nl|'\n'
string|'"  |- 6:0:3:0 sdf 8:80  active undef  running\\n"'
nl|'\n'
string|'"  `- 6:0:5:0 sdh 8:112 active undef  running\\n"'
nl|'\n'
op|')'
newline|'\n'
name|'return'
name|'out'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'linuxscsi'
op|'.'
name|'find_multipath_device'
op|'('
string|"'/dev/sde'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"info = %s"'
op|'%'
name|'info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"36005076da00638089c000000000004d5"'
op|','
name|'info'
op|'['
string|'"name"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"36005076da00638089c000000000004d5"'
op|','
name|'info'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/mapper/36005076da00638089c000000000004d5"'
op|','
nl|'\n'
name|'info'
op|'['
string|'"device"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sde"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'device'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"6"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'channel'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"2"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'lun'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sdf"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'2'
op|']'
op|'['
string|"'device'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"6"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'2'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'2'
op|']'
op|'['
string|"'channel'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"3"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'2'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'2'
op|']'
op|'['
string|"'lun'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_find_multipath_device_ds8000
dedent|''
name|'def'
name|'test_find_multipath_device_ds8000'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|function|fake_execute
indent|'        '
name|'def'
name|'fake_execute'
op|'('
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'out'
op|'='
op|'('
string|'"36005076303ffc48e0000000000000101 dm-2 IBM,2107900\\n"'
nl|'\n'
string|'"size=1.0G features=\'1 queue_if_no_path\' hwhandler=\'0\'"'
nl|'\n'
string|'" wp=rw\\n"'
nl|'\n'
string|'"`-+- policy=\'round-robin 0\' prio=-1 status=active\\n"'
nl|'\n'
string|'"  |- 6:0:2:0 sdd 8:64  active undef  running\\n"'
nl|'\n'
string|'"  `- 6:1:0:3 sdc 8:32  active undef  running\\n"'
nl|'\n'
op|')'
newline|'\n'
name|'return'
name|'out'
op|','
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|','
string|"'execute'"
op|','
name|'fake_execute'
op|')'
newline|'\n'
nl|'\n'
name|'info'
op|'='
name|'linuxscsi'
op|'.'
name|'find_multipath_device'
op|'('
string|"'/dev/sdd'"
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
string|'"info = %s"'
op|'%'
name|'info'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"36005076303ffc48e0000000000000101"'
op|','
name|'info'
op|'['
string|'"name"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"36005076303ffc48e0000000000000101"'
op|','
name|'info'
op|'['
string|'"id"'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/mapper/36005076303ffc48e0000000000000101"'
op|','
nl|'\n'
name|'info'
op|'['
string|'"device"'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sdd"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'device'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"6"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'channel'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"2"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'lun'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"/dev/sdc"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'device'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"6"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'host'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"1"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'channel'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"0"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"3"'
op|','
name|'info'
op|'['
string|"'devices'"
op|']'
op|'['
number|'1'
op|']'
op|'['
string|"'lun'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit