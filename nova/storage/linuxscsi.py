begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# (c) Copyright 2013 Hewlett-Packard Development Company, L.P.'
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
string|'"""Generic linux scsi subsystem utilities."""'
newline|'\n'
nl|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'loopingcall'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
nl|'\n'
DECL|function|echo_scsi_command
name|'def'
name|'echo_scsi_command'
op|'('
name|'path'
op|','
name|'content'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Used to echo strings to scsi subsystem."""'
newline|'\n'
name|'args'
op|'='
op|'['
string|'"-a"'
op|','
name|'path'
op|']'
newline|'\n'
name|'kwargs'
op|'='
name|'dict'
op|'('
name|'process_input'
op|'='
name|'content'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tee'"
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|rescan_hosts
dedent|''
name|'def'
name|'rescan_hosts'
op|'('
name|'hbas'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'for'
name|'hba'
name|'in'
name|'hbas'
op|':'
newline|'\n'
indent|'        '
name|'echo_scsi_command'
op|'('
string|'"/sys/class/scsi_host/%s/scan"'
nl|'\n'
op|'%'
name|'hba'
op|'['
string|"'host_device'"
op|']'
op|','
string|'"- - -"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_device_list
dedent|''
dedent|''
name|'def'
name|'get_device_list'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sginfo'"
op|','
string|"'-r'"
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'devices'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'out'
op|':'
newline|'\n'
indent|'        '
name|'line'
op|'='
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'devices'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'devices'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_device_info
dedent|''
name|'def'
name|'get_device_info'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sg_scan'"
op|','
name|'device'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'dev_info'
op|'='
op|'{'
string|"'device'"
op|':'
name|'device'
op|','
string|"'host'"
op|':'
name|'None'
op|','
nl|'\n'
string|"'channel'"
op|':'
name|'None'
op|','
string|"'id'"
op|':'
name|'None'
op|','
string|"'lun'"
op|':'
name|'None'
op|'}'
newline|'\n'
name|'if'
name|'out'
op|':'
newline|'\n'
indent|'        '
name|'line'
op|'='
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'line'
op|'='
name|'line'
op|'.'
name|'replace'
op|'('
name|'device'
op|'+'
string|'": "'
op|','
string|'""'
op|')'
newline|'\n'
name|'info'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'item'
name|'in'
name|'info'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'='"
name|'in'
name|'item'
op|':'
newline|'\n'
indent|'                '
name|'pair'
op|'='
name|'item'
op|'.'
name|'split'
op|'('
string|"'='"
op|')'
newline|'\n'
name|'dev_info'
op|'['
name|'pair'
op|'['
number|'0'
op|']'
op|']'
op|'='
name|'pair'
op|'['
number|'1'
op|']'
newline|'\n'
dedent|''
name|'elif'
string|"'scsi'"
name|'in'
name|'item'
op|':'
newline|'\n'
indent|'                '
name|'dev_info'
op|'['
string|"'host'"
op|']'
op|'='
name|'item'
op|'.'
name|'replace'
op|'('
string|"'scsi'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'dev_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_wait_for_remove
dedent|''
name|'def'
name|'_wait_for_remove'
op|'('
name|'device'
op|','
name|'tries'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'tries'
op|'='
name|'tries'
op|'+'
number|'1'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Trying (%(tries)s) to remove device %(device)s"'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'tries'"
op|':'
name|'tries'
op|','
string|"'device'"
op|':'
name|'device'
op|'['
string|'"device"'
op|']'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'path'
op|'='
string|'"/sys/bus/scsi/drivers/sd/%s:%s:%s:%s/delete"'
newline|'\n'
name|'echo_scsi_command'
op|'('
name|'path'
op|'%'
op|'('
name|'device'
op|'['
string|'"host"'
op|']'
op|','
name|'device'
op|'['
string|'"channel"'
op|']'
op|','
nl|'\n'
name|'device'
op|'['
string|'"id"'
op|']'
op|','
name|'device'
op|'['
string|'"lun"'
op|']'
op|')'
op|','
nl|'\n'
string|'"1"'
op|')'
newline|'\n'
nl|'\n'
name|'devices'
op|'='
name|'get_device_list'
op|'('
op|')'
newline|'\n'
name|'if'
name|'device'
op|'['
string|'"device"'
op|']'
name|'not'
name|'in'
name|'devices'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'loopingcall'
op|'.'
name|'LoopingCallDone'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_device
dedent|''
dedent|''
name|'def'
name|'remove_device'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'tries'
op|'='
number|'0'
newline|'\n'
name|'timer'
op|'='
name|'loopingcall'
op|'.'
name|'FixedIntervalLoopingCall'
op|'('
name|'_wait_for_remove'
op|','
name|'device'
op|','
nl|'\n'
name|'tries'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'2'
op|')'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'stop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|find_multipath_device
dedent|''
name|'def'
name|'find_multipath_device'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Try and discover the multipath device for a volume."""'
newline|'\n'
name|'mdev'
op|'='
name|'None'
newline|'\n'
name|'devices'
op|'='
op|'['
op|']'
newline|'\n'
name|'out'
op|'='
name|'None'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
op|'('
name|'out'
op|','
name|'err'
op|')'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'multipath'"
op|','
string|"'-l'"
op|','
name|'device'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Multipath call failed exit (%(code)s)"'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'code'"
op|':'
name|'exc'
op|'.'
name|'exit_code'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'out'
op|':'
newline|'\n'
indent|'        '
name|'lines'
op|'='
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
name|'lines'
op|'='
name|'lines'
op|'.'
name|'split'
op|'('
string|'"\\n"'
op|')'
newline|'\n'
name|'if'
name|'lines'
op|':'
newline|'\n'
indent|'            '
name|'line'
op|'='
name|'lines'
op|'['
number|'0'
op|']'
newline|'\n'
name|'info'
op|'='
name|'line'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
newline|'\n'
comment|'# device line output is different depending'
nl|'\n'
comment|'# on /etc/multipath.conf settings.'
nl|'\n'
name|'if'
name|'info'
op|'['
number|'1'
op|']'
op|'['
op|':'
number|'2'
op|']'
op|'=='
string|'"dm"'
op|':'
newline|'\n'
indent|'                '
name|'mdev'
op|'='
string|'"/dev/%s"'
op|'%'
name|'info'
op|'['
number|'1'
op|']'
newline|'\n'
name|'mdev_id'
op|'='
name|'info'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'info'
op|'['
number|'2'
op|']'
op|'['
op|':'
number|'2'
op|']'
op|'=='
string|'"dm"'
op|':'
newline|'\n'
indent|'                '
name|'mdev'
op|'='
string|'"/dev/%s"'
op|'%'
name|'info'
op|'['
number|'2'
op|']'
newline|'\n'
name|'mdev_id'
op|'='
name|'info'
op|'['
number|'1'
op|']'
op|'.'
name|'replace'
op|'('
string|"'('"
op|','
string|"''"
op|')'
newline|'\n'
name|'mdev_id'
op|'='
name|'mdev_id'
op|'.'
name|'replace'
op|'('
string|"')'"
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'mdev'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Couldn\'t find multipath device %s"'
op|')'
op|','
name|'line'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Found multipath device = %s"'
op|')'
op|','
name|'mdev'
op|')'
newline|'\n'
name|'device_lines'
op|'='
name|'lines'
op|'['
number|'3'
op|':'
op|']'
newline|'\n'
name|'for'
name|'dev_line'
name|'in'
name|'device_lines'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'dev_line'
op|'.'
name|'find'
op|'('
string|'"policy"'
op|')'
op|'!='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'dev_line'
op|'='
name|'dev_line'
op|'.'
name|'lstrip'
op|'('
string|"' |-`'"
op|')'
newline|'\n'
name|'dev_info'
op|'='
name|'dev_line'
op|'.'
name|'split'
op|'('
op|')'
newline|'\n'
name|'address'
op|'='
name|'dev_info'
op|'['
number|'0'
op|']'
op|'.'
name|'split'
op|'('
string|'":"'
op|')'
newline|'\n'
nl|'\n'
name|'dev'
op|'='
op|'{'
string|"'device'"
op|':'
string|"'/dev/%s'"
op|'%'
name|'dev_info'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'address'
op|'['
number|'0'
op|']'
op|','
string|"'channel'"
op|':'
name|'address'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
string|"'id'"
op|':'
name|'address'
op|'['
number|'2'
op|']'
op|','
string|"'lun'"
op|':'
name|'address'
op|'['
number|'3'
op|']'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'devices'
op|'.'
name|'append'
op|'('
name|'dev'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'mdev'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'info'
op|'='
op|'{'
string|'"device"'
op|':'
name|'mdev'
op|','
nl|'\n'
string|'"id"'
op|':'
name|'mdev_id'
op|','
nl|'\n'
string|'"devices"'
op|':'
name|'devices'
op|'}'
newline|'\n'
name|'return'
name|'info'
newline|'\n'
dedent|''
name|'return'
name|'None'
newline|'\n'
dedent|''
endmarker|''
end_unit
