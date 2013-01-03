begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# coding=utf-8'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 Hewlett-Packard Development Company, L.P.'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""\nBaremetal IPMI power manager.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'stat'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'exception'
name|'import'
name|'InvalidParameterValue'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'baremetal_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'utils'
name|'as'
name|'bm_utils'
newline|'\n'
nl|'\n'
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'terminal'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'shellinaboxd'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'path to baremetal terminal program'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'terminal_cert_dir'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'path to baremetal terminal SSL cert(PEM)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'terminal_pid_dir'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$state_path/baremetal/console'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'path to directory stores pidfiles of baremetal_terminal'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'ipmi_power_retry'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'5'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'maximal number of retries for IPMI operations'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|baremetal_group
name|'baremetal_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Baremetal Options'"
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
name|'CONF'
op|'.'
name|'register_group'
op|'('
name|'baremetal_group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'opts'
op|','
name|'baremetal_group'
op|')'
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
DECL|function|_make_password_file
name|'def'
name|'_make_password_file'
op|'('
name|'password'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'fd'
op|','
name|'path'
op|'='
name|'tempfile'
op|'.'
name|'mkstemp'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'fchmod'
op|'('
name|'fd'
op|','
name|'stat'
op|'.'
name|'S_IRUSR'
op|'|'
name|'stat'
op|'.'
name|'S_IWUSR'
op|')'
newline|'\n'
name|'with'
name|'os'
op|'.'
name|'fdopen'
op|'('
name|'fd'
op|','
string|'"w"'
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'        '
name|'f'
op|'.'
name|'write'
op|'('
name|'password'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'path'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_console_pid_path
dedent|''
name|'def'
name|'_get_console_pid_path'
op|'('
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'name'
op|'='
string|'"%s.pid"'
op|'%'
name|'node_id'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'terminal_pid_dir'
op|','
name|'name'
op|')'
newline|'\n'
name|'return'
name|'path'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_console_pid
dedent|''
name|'def'
name|'_get_console_pid'
op|'('
name|'node_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'pid_path'
op|'='
name|'_get_console_pid_path'
op|'('
name|'node_id'
op|')'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'pid_path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'pid_path'
op|','
string|"'r'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'pid_str'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'pid_str'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"pid file %s does not contain any pid"'
op|')'
op|','
name|'pid_path'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IPMI
dedent|''
name|'class'
name|'IPMI'
op|'('
name|'base'
op|'.'
name|'PowerManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""IPMI Power Driver for Baremetal Nova Compute\n\n    This PowerManager class provides mechanism for controlling the power state\n    of physical hardware via IPMI calls. It also provides serial console access\n    where available.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'node'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'state'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'retries'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'node_id'
op|'='
name|'node'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'address'
op|'='
name|'node'
op|'['
string|"'pm_address'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
name|'node'
op|'['
string|"'pm_user'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'password'
op|'='
name|'node'
op|'['
string|"'pm_password'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'port'
op|'='
name|'node'
op|'['
string|"'terminal_port'"
op|']'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'node_id'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidParameterValue'
op|'('
name|'_'
op|'('
string|'"Node id not supplied to IPMI"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'address'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidParameterValue'
op|'('
name|'_'
op|'('
string|'"Address not supplied to IPMI"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'user'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidParameterValue'
op|'('
name|'_'
op|'('
string|'"User not supplied to IPMI"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'password'
op|'=='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'InvalidParameterValue'
op|'('
name|'_'
op|'('
string|'"Password not supplied to IPMI"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_exec_ipmitool
dedent|''
dedent|''
name|'def'
name|'_exec_ipmitool'
op|'('
name|'self'
op|','
name|'command'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
string|"'ipmitool'"
op|','
nl|'\n'
string|"'-I'"
op|','
nl|'\n'
string|"'lanplus'"
op|','
nl|'\n'
string|"'-H'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'address'
op|','
nl|'\n'
string|"'-U'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'user'
op|','
nl|'\n'
string|"'-f'"
op|']'
newline|'\n'
name|'pwfile'
op|'='
name|'_make_password_file'
op|'('
name|'self'
op|'.'
name|'password'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'append'
op|'('
name|'pwfile'
op|')'
newline|'\n'
name|'args'
op|'.'
name|'extend'
op|'('
name|'command'
op|'.'
name|'split'
op|'('
string|'" "'
op|')'
op|')'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
name|'attempts'
op|'='
number|'3'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"ipmitool stdout: \'%(out)s\', stderr: \'%(err)%s\'"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'out'
op|','
name|'err'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'pwfile'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_is_power
dedent|''
dedent|''
name|'def'
name|'_is_power'
op|'('
name|'self'
op|','
name|'state'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'out_err'
op|'='
name|'self'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power status"'
op|')'
newline|'\n'
name|'return'
name|'out_err'
op|'['
number|'0'
op|']'
op|'=='
op|'('
string|'"Chassis Power is %s\\n"'
op|'%'
name|'state'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_power_on
dedent|''
name|'def'
name|'_power_on'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Turn the power to this node ON"""'
newline|'\n'
nl|'\n'
DECL|function|_wait_for_power_on
name|'def'
name|'_wait_for_power_on'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Called at an interval until the node\'s power is on"""'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_is_power'
op|'('
string|'"on"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
newline|'\n'
name|'raise'
name|'utils'
op|'.'
name|'LoopingCallDone'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'retries'
op|'>'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'ipmi_power_retry'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ERROR'
newline|'\n'
name|'raise'
name|'utils'
op|'.'
name|'LoopingCallDone'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'retries'
op|'+='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power on"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"IPMI power on failed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'retries'
op|'='
number|'0'
newline|'\n'
name|'timer'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'_wait_for_power_on'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|')'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_power_off
dedent|''
name|'def'
name|'_power_off'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Turn the power to this node OFF"""'
newline|'\n'
nl|'\n'
DECL|function|_wait_for_power_off
name|'def'
name|'_wait_for_power_off'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
string|'"""Called at an interval until the node\'s power is off"""'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_is_power'
op|'('
string|'"off"'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'raise'
name|'utils'
op|'.'
name|'LoopingCallDone'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'retries'
op|'>'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'ipmi_power_retry'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ERROR'
newline|'\n'
name|'raise'
name|'utils'
op|'.'
name|'LoopingCallDone'
op|'('
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'retries'
op|'+='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"power off"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"IPMI power off failed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'retries'
op|'='
number|'0'
newline|'\n'
name|'timer'
op|'='
name|'utils'
op|'.'
name|'LoopingCall'
op|'('
name|'_wait_for_power_off'
op|')'
newline|'\n'
name|'timer'
op|'.'
name|'start'
op|'('
name|'interval'
op|'='
number|'0.5'
op|')'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_set_pxe_for_next_boot
dedent|''
name|'def'
name|'_set_pxe_for_next_boot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_exec_ipmitool'
op|'('
string|'"chassis bootdev pxe"'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"IPMI set next bootdev failed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|activate_node
dedent|''
dedent|''
name|'def'
name|'activate_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Turns the power to node ON"""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_is_power'
op|'('
string|'"on"'
op|')'
name|'and'
name|'self'
op|'.'
name|'state'
op|'=='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Activate node called, but node %s "'
nl|'\n'
string|'"is already active"'
op|')'
op|'%'
name|'self'
op|'.'
name|'address'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_set_pxe_for_next_boot'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_power_on'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|reboot_node
dedent|''
name|'def'
name|'reboot_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Cycles the power to a node"""'
newline|'\n'
name|'self'
op|'.'
name|'_power_off'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_set_pxe_for_next_boot'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_power_on'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|deactivate_node
dedent|''
name|'def'
name|'deactivate_node'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Turns the power to node OFF, regardless of current state"""'
newline|'\n'
name|'self'
op|'.'
name|'_power_off'
op|'('
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'state'
newline|'\n'
nl|'\n'
DECL|member|is_power_on
dedent|''
name|'def'
name|'is_power_on'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_is_power'
op|'('
string|'"on"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|start_console
dedent|''
name|'def'
name|'start_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'port'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'args'
op|'='
op|'['
op|']'
newline|'\n'
name|'args'
op|'.'
name|'append'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'terminal'
op|')'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'terminal_cert_dir'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'append'
op|'('
string|'"-c"'
op|')'
newline|'\n'
name|'args'
op|'.'
name|'append'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'terminal_cert_dir'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'append'
op|'('
string|'"-t"'
op|')'
newline|'\n'
dedent|''
name|'args'
op|'.'
name|'append'
op|'('
string|'"-p"'
op|')'
newline|'\n'
name|'args'
op|'.'
name|'append'
op|'('
name|'str'
op|'('
name|'self'
op|'.'
name|'port'
op|')'
op|')'
newline|'\n'
name|'args'
op|'.'
name|'append'
op|'('
string|'"--background=%s"'
op|'%'
name|'_get_console_pid_path'
op|'('
name|'self'
op|'.'
name|'node_id'
op|')'
op|')'
newline|'\n'
name|'args'
op|'.'
name|'append'
op|'('
string|'"-s"'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pwfile'
op|'='
name|'_make_password_file'
op|'('
name|'self'
op|'.'
name|'password'
op|')'
newline|'\n'
name|'ipmi_args'
op|'='
string|'"/:%(uid)s:%(gid)s:HOME:ipmitool -H %(address)s"'
string|'" -I lanplus -U %(user)s -f %(pwfile)s sol activate"'
op|'%'
op|'{'
string|"'uid'"
op|':'
name|'os'
op|'.'
name|'getuid'
op|'('
op|')'
op|','
nl|'\n'
string|"'gid'"
op|':'
name|'os'
op|'.'
name|'getgid'
op|'('
op|')'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'self'
op|'.'
name|'address'
op|','
nl|'\n'
string|"'user'"
op|':'
name|'self'
op|'.'
name|'user'
op|','
nl|'\n'
string|"'pwfile'"
op|':'
name|'pwfile'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'args'
op|'.'
name|'append'
op|'('
name|'ipmi_args'
op|')'
newline|'\n'
comment|'# Run shellinaboxd without pipes. Otherwise utils.execute() waits'
nl|'\n'
comment|'# infinitely since shellinaboxd does not close passed fds.'
nl|'\n'
name|'x'
op|'='
op|'['
string|'"\'"'
op|'+'
name|'arg'
op|'.'
name|'replace'
op|'('
string|'"\'"'
op|','
string|'"\'\\\\\'\'"'
op|')'
op|'+'
string|'"\'"'
name|'for'
name|'arg'
name|'in'
name|'args'
op|']'
newline|'\n'
name|'x'
op|'.'
name|'append'
op|'('
string|"'</dev/null'"
op|')'
newline|'\n'
name|'x'
op|'.'
name|'append'
op|'('
string|"'>/dev/null'"
op|')'
newline|'\n'
name|'x'
op|'.'
name|'append'
op|'('
string|"'2>&1'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"' '"
op|'.'
name|'join'
op|'('
name|'x'
op|')'
op|','
name|'shell'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'pwfile'
op|')'
newline|'\n'
nl|'\n'
DECL|member|stop_console
dedent|''
dedent|''
name|'def'
name|'stop_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'console_pid'
op|'='
name|'_get_console_pid'
op|'('
name|'self'
op|'.'
name|'node_id'
op|')'
newline|'\n'
name|'if'
name|'console_pid'
op|':'
newline|'\n'
comment|'# Allow exitcode 99 (RC_UNAUTHORIZED)'
nl|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'kill'"
op|','
string|"'-TERM'"
op|','
name|'str'
op|'('
name|'console_pid'
op|')'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'99'
op|']'
op|')'
newline|'\n'
dedent|''
name|'bm_utils'
op|'.'
name|'unlink_without_raise'
op|'('
name|'_get_console_pid_path'
op|'('
name|'self'
op|'.'
name|'node_id'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
