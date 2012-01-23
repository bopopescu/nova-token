begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2011 OpenStack LLC'
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
name|'nova'
op|'.'
name|'rootwrap'
name|'import'
name|'filters'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'rootwrap'
name|'import'
name|'wrapper'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RootwrapTestCase
name|'class'
name|'RootwrapTestCase'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'RootwrapTestCase'
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
name|'filters'
op|'='
op|'['
nl|'\n'
name|'filters'
op|'.'
name|'RegExpFilter'
op|'('
string|'"/bin/ls"'
op|','
string|'"root"'
op|','
string|"'ls'"
op|','
string|"'/[a-z]+'"
op|')'
op|','
nl|'\n'
name|'filters'
op|'.'
name|'CommandFilter'
op|'('
string|'"/usr/bin/foo_bar_not_exist"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
name|'filters'
op|'.'
name|'RegExpFilter'
op|'('
string|'"/bin/cat"'
op|','
string|'"root"'
op|','
string|"'cat'"
op|','
string|"'/[a-z]+'"
op|')'
op|','
nl|'\n'
name|'filters'
op|'.'
name|'CommandFilter'
op|'('
string|'"/nonexistant/cat"'
op|','
string|'"root"'
op|')'
op|','
nl|'\n'
name|'filters'
op|'.'
name|'CommandFilter'
op|'('
string|'"/bin/cat"'
op|','
string|'"root"'
op|')'
comment|'# Keep this one last'
nl|'\n'
op|']'
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
name|'super'
op|'('
name|'RootwrapTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'tearDown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_RegExpFilter_match
dedent|''
name|'def'
name|'test_RegExpFilter_match'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usercmd'
op|'='
op|'['
string|'"ls"'
op|','
string|'"/root"'
op|']'
newline|'\n'
name|'filtermatch'
op|'='
name|'wrapper'
op|'.'
name|'match_filter'
op|'('
name|'self'
op|'.'
name|'filters'
op|','
name|'usercmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'filtermatch'
name|'is'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'filtermatch'
op|'.'
name|'get_command'
op|'('
name|'usercmd'
op|')'
op|','
nl|'\n'
op|'['
string|'"/bin/ls"'
op|','
string|'"/root"'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_RegExpFilter_reject
dedent|''
name|'def'
name|'test_RegExpFilter_reject'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usercmd'
op|'='
op|'['
string|'"ls"'
op|','
string|'"root"'
op|']'
newline|'\n'
name|'filtermatch'
op|'='
name|'wrapper'
op|'.'
name|'match_filter'
op|'('
name|'self'
op|'.'
name|'filters'
op|','
name|'usercmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filtermatch'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_missing_command
dedent|''
name|'def'
name|'test_missing_command'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usercmd'
op|'='
op|'['
string|'"foo_bar_not_exist"'
op|']'
newline|'\n'
name|'filtermatch'
op|'='
name|'wrapper'
op|'.'
name|'match_filter'
op|'('
name|'self'
op|'.'
name|'filters'
op|','
name|'usercmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filtermatch'
name|'is'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_DnsmasqFilter
dedent|''
name|'def'
name|'test_DnsmasqFilter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usercmd'
op|'='
op|'['
string|"'FLAGFILE=A'"
op|','
string|'\'NETWORK_ID="foo bar"\''
op|','
string|"'dnsmasq'"
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'f'
op|'='
name|'filters'
op|'.'
name|'DnsmasqFilter'
op|'('
string|'"/usr/bin/dnsmasq"'
op|','
string|'"root"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'f'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'f'
op|'.'
name|'get_command'
op|'('
name|'usercmd'
op|')'
op|','
nl|'\n'
op|'['
string|"'FLAGFILE=A'"
op|','
string|'\'NETWORK_ID="foo bar"\''
op|','
string|"'/usr/bin/dnsmasq'"
op|','
string|"'foo'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_skips
dedent|''
name|'def'
name|'test_skips'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Check that all filters are skipped and that the last matches'
nl|'\n'
indent|'        '
name|'usercmd'
op|'='
op|'['
string|'"cat"'
op|','
string|'"/"'
op|']'
newline|'\n'
name|'filtermatch'
op|'='
name|'wrapper'
op|'.'
name|'match_filter'
op|'('
name|'self'
op|'.'
name|'filters'
op|','
name|'usercmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filtermatch'
name|'is'
name|'self'
op|'.'
name|'filters'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
