begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# coding=utf-8'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011-2013 University of Southern California / ISI'
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
string|'"""\nBaremetal PDU power manager.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
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
string|"'tile_pdu_ip'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'10.0.100.1'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address of tilera pdu'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'tile_pdu_mgr'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'/tftpboot/pdu_mgr'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Management script for tilera pdu'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'tile_pdu_off'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'2'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Power status of tilera PDU is OFF'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'tile_pdu_on'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'1'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Power status of tilera PDU is ON'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'tile_pdu_status'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'9'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Power status of tilera PDU'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'tile_power_wait'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'9'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Wait time in seconds until check the result '"
nl|'\n'
string|"'after tilera power operations'"
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
DECL|class|Pdu
name|'class'
name|'Pdu'
op|'('
name|'base'
op|'.'
name|'PowerManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""PDU Power Driver for Baremetal Nova Compute\n\n    This PowerManager class provides mechanism for controlling the power state\n    of physical hardware via PDU calls.\n    """'
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
name|'exception'
op|'.'
name|'InvalidParameterValue'
op|'('
name|'_'
op|'('
string|'"Node id not supplied "'
nl|'\n'
string|'"to PDU"'
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
name|'exception'
op|'.'
name|'InvalidParameterValue'
op|'('
name|'_'
op|'('
string|'"Address not supplied "'
nl|'\n'
string|'"to PDU"'
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
name|'exception'
op|'.'
name|'InvalidParameterValue'
op|'('
name|'_'
op|'('
string|'"User not supplied "'
nl|'\n'
string|'"to PDU"'
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
name|'exception'
op|'.'
name|'InvalidParameterValue'
op|'('
name|'_'
op|'('
string|'"Password not supplied "'
nl|'\n'
string|'"to PDU"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_exec_pdutool
dedent|''
dedent|''
name|'def'
name|'_exec_pdutool'
op|'('
name|'self'
op|','
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Changes power state of the given node.\n\n        According to the mode (1-ON, 2-OFF, 3-REBOOT), power state can be\n        changed. /tftpboot/pdu_mgr script handles power management of\n        PDU (Power Distribution Unit).\n        """'
newline|'\n'
name|'if'
name|'mode'
op|'=='
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_status'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ping'"
op|','
string|"'-c1'"
op|','
name|'self'
op|'.'
name|'address'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_on'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_off'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_mgr'
op|','
nl|'\n'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_ip'
op|','
name|'mode'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_power_wait'
op|')'
newline|'\n'
name|'return'
name|'mode'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"PDU failed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_is_power
dedent|''
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
name|'_exec_pdutool'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_status'
op|')'
newline|'\n'
name|'return'
name|'out_err'
op|'=='
name|'state'
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
string|'"""Turn the power to this node ON."""'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_exec_pdutool'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_on'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_is_power'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_on'
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
dedent|''
name|'else'
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
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ERROR'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"PDU power on failed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_power_off
dedent|''
dedent|''
name|'def'
name|'_power_off'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Turn the power to this node OFF."""'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_exec_pdutool'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_off'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_is_power'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_off'
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
dedent|''
name|'else'
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
dedent|''
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ERROR'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"PDU power off failed"'
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
string|'"""Turns the power to node ON."""'
newline|'\n'
name|'if'
op|'('
name|'self'
op|'.'
name|'_is_power'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_on'
op|')'
nl|'\n'
name|'and'
name|'self'
op|'.'
name|'state'
op|'=='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|')'
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
string|'"""Cycles the power to a node."""'
newline|'\n'
name|'self'
op|'.'
name|'_power_off'
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
string|'"""Turns the power to node OFF, regardless of current state."""'
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
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'tile_pdu_on'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
