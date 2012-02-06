begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Red Hat, Inc.'
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
name|'string'
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
name|'volume'
name|'import'
name|'iscsi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TargetAdminTestCase
name|'class'
name|'TargetAdminTestCase'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'self'
op|'.'
name|'cmds'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'tid'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'target_name'
op|'='
string|"'iqn.2011-09.org.foo.bar:blaa'"
newline|'\n'
name|'self'
op|'.'
name|'lun'
op|'='
number|'10'
newline|'\n'
name|'self'
op|'.'
name|'path'
op|'='
string|"'/foo/bar/blaa'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'script_template'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_script_params
dedent|''
name|'def'
name|'get_script_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'tid'"
op|':'
name|'self'
op|'.'
name|'tid'
op|','
nl|'\n'
string|"'target_name'"
op|':'
name|'self'
op|'.'
name|'target_name'
op|','
nl|'\n'
string|"'lun'"
op|':'
name|'self'
op|'.'
name|'lun'
op|','
nl|'\n'
string|"'path'"
op|':'
name|'self'
op|'.'
name|'path'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|get_script
dedent|''
name|'def'
name|'get_script'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'script_template'
op|'%'
name|'self'
op|'.'
name|'get_script_params'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|fake_execute
dedent|''
name|'def'
name|'fake_execute'
op|'('
name|'self'
op|','
op|'*'
name|'cmd'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'cmds'
op|'.'
name|'append'
op|'('
name|'string'
op|'.'
name|'join'
op|'('
name|'cmd'
op|')'
op|')'
newline|'\n'
name|'return'
string|'""'
op|','
name|'None'
newline|'\n'
nl|'\n'
DECL|member|clear_cmds
dedent|''
name|'def'
name|'clear_cmds'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cmds'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|verify_cmds
dedent|''
name|'def'
name|'verify_cmds'
op|'('
name|'self'
op|','
name|'cmds'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'cmds'
op|')'
op|','
name|'len'
op|'('
name|'self'
op|'.'
name|'cmds'
op|')'
op|')'
newline|'\n'
name|'for'
name|'a'
op|','
name|'b'
name|'in'
name|'zip'
op|'('
name|'cmds'
op|','
name|'self'
op|'.'
name|'cmds'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'a'
op|','
name|'b'
op|')'
newline|'\n'
nl|'\n'
DECL|member|verify
dedent|''
dedent|''
name|'def'
name|'verify'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'script'
op|'='
name|'self'
op|'.'
name|'get_script'
op|'('
op|')'
newline|'\n'
name|'cmds'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'script'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'line'
op|'.'
name|'strip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'cmds'
op|'.'
name|'append'
op|'('
name|'line'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'verify_cmds'
op|'('
name|'cmds'
op|')'
newline|'\n'
nl|'\n'
DECL|member|run_commands
dedent|''
name|'def'
name|'run_commands'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'tgtadm'
op|'='
name|'iscsi'
op|'.'
name|'get_target_admin'
op|'('
op|')'
newline|'\n'
name|'tgtadm'
op|'.'
name|'set_execute'
op|'('
name|'self'
op|'.'
name|'fake_execute'
op|')'
newline|'\n'
name|'tgtadm'
op|'.'
name|'new_target'
op|'('
name|'self'
op|'.'
name|'target_name'
op|','
name|'self'
op|'.'
name|'tid'
op|')'
newline|'\n'
name|'tgtadm'
op|'.'
name|'show_target'
op|'('
name|'self'
op|'.'
name|'tid'
op|')'
newline|'\n'
name|'tgtadm'
op|'.'
name|'new_logicalunit'
op|'('
name|'self'
op|'.'
name|'tid'
op|','
name|'self'
op|'.'
name|'lun'
op|','
name|'self'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'tgtadm'
op|'.'
name|'delete_logicalunit'
op|'('
name|'self'
op|'.'
name|'tid'
op|','
name|'self'
op|'.'
name|'lun'
op|')'
newline|'\n'
name|'tgtadm'
op|'.'
name|'delete_target'
op|'('
name|'self'
op|'.'
name|'tid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_target_admin
dedent|''
name|'def'
name|'test_target_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'clear_cmds'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'run_commands'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'verify'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TgtAdmTestCase
dedent|''
dedent|''
name|'class'
name|'TgtAdmTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|','
name|'TargetAdminTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'TgtAdmTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'TargetAdminTestCase'
op|'.'
name|'setUp'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'iscsi_helper'
op|'='
string|"'tgtadm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'script_template'
op|'='
string|'"\\n"'
op|'.'
name|'join'
op|'('
op|'['
nl|'\n'
string|'"tgtadm --op new --lld=iscsi --mode=target --tid=%(tid)s "'
nl|'\n'
string|'"--targetname=%(target_name)s"'
op|','
nl|'\n'
string|'"tgtadm --op bind --lld=iscsi --mode=target --initiator-address=ALL "'
nl|'\n'
string|'"--tid=%(tid)s"'
op|','
nl|'\n'
string|'"tgtadm --op show --lld=iscsi --mode=target --tid=%(tid)s"'
op|','
nl|'\n'
string|'"tgtadm --op new --lld=iscsi --mode=logicalunit --tid=%(tid)s "'
nl|'\n'
string|'"--lun=%(lun)d --backing-store=%(path)s"'
op|','
nl|'\n'
string|'"tgtadm --op delete --lld=iscsi --mode=logicalunit --tid=%(tid)s "'
nl|'\n'
string|'"--lun=%(lun)d"'
op|','
nl|'\n'
string|'"tgtadm --op delete --lld=iscsi --mode=target --tid=%(tid)s"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_script_params
dedent|''
name|'def'
name|'get_script_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'super'
op|'('
name|'TgtAdmTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'get_script_params'
op|'('
op|')'
newline|'\n'
name|'params'
op|'['
string|"'lun'"
op|']'
op|'+='
number|'1'
newline|'\n'
name|'return'
name|'params'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IetAdmTestCase
dedent|''
dedent|''
name|'class'
name|'IetAdmTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|','
name|'TargetAdminTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'IetAdmTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'TargetAdminTestCase'
op|'.'
name|'setUp'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'iscsi_helper'
op|'='
string|"'ietadm'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'script_template'
op|'='
string|'"\\n"'
op|'.'
name|'join'
op|'('
op|'['
nl|'\n'
string|'"ietadm --op new --tid=%(tid)s --params Name=%(target_name)s"'
op|','
nl|'\n'
string|'"ietadm --op show --tid=%(tid)s"'
op|','
nl|'\n'
string|'"ietadm --op new --tid=%(tid)s --lun=%(lun)d "'
nl|'\n'
string|'"--params Path=%(path)s,Type=fileio"'
op|','
nl|'\n'
string|'"ietadm --op delete --tid=%(tid)s --lun=%(lun)d"'
op|','
nl|'\n'
string|'"ietadm --op delete --tid=%(tid)s"'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
