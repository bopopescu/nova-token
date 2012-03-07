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
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'subprocess'
newline|'\n'
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
name|'valid_but_missing'
op|'='
op|'['
string|'"foo_bar_not_exist"'
op|']'
newline|'\n'
name|'invalid'
op|'='
op|'['
string|'"foo_bar_not_exist_and_not_matched"'
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
name|'valid_but_missing'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'filtermatch'
name|'is'
name|'not'
name|'None'
op|')'
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
name|'invalid'
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
string|"'NETWORK_ID=foobar'"
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
op|'['
string|"'/usr/bin/dnsmasq'"
op|','
string|"'foo'"
op|']'
op|')'
newline|'\n'
name|'env'
op|'='
name|'f'
op|'.'
name|'get_environment'
op|'('
name|'usercmd'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'env'
op|'.'
name|'get'
op|'('
string|"'FLAGFILE'"
op|')'
op|','
string|"'A'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'env'
op|'.'
name|'get'
op|'('
string|"'NETWORK_ID'"
op|')'
op|','
string|"'foobar'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'test'
op|'.'
name|'skip_if'
op|'('
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
string|'"/proc/%d"'
op|'%'
name|'os'
op|'.'
name|'getpid'
op|'('
op|')'
op|')'
op|','
nl|'\n'
string|'"Test requires /proc filesystem (procfs)"'
op|')'
newline|'\n'
DECL|member|test_KillFilter
name|'def'
name|'test_KillFilter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'p'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
op|'['
string|'"/bin/sleep"'
op|','
string|'"5"'
op|']'
op|')'
newline|'\n'
name|'f'
op|'='
name|'filters'
op|'.'
name|'KillFilter'
op|'('
string|'"/bin/kill"'
op|','
string|'"root"'
op|','
nl|'\n'
op|'['
string|'"-ALRM"'
op|']'
op|','
nl|'\n'
op|'['
string|'"/bin/sleep"'
op|']'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
string|"'-9'"
op|','
name|'p'
op|'.'
name|'pid'
op|']'
newline|'\n'
comment|'# Incorrect signal should fail'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'f'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
name|'p'
op|'.'
name|'pid'
op|']'
newline|'\n'
comment|'# Providing no signal should fail'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'f'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'f'
op|'='
name|'filters'
op|'.'
name|'KillFilter'
op|'('
string|'"/bin/kill"'
op|','
string|'"root"'
op|','
nl|'\n'
op|'['
string|'"-9"'
op|','
string|'""'
op|']'
op|','
nl|'\n'
op|'['
string|'"/bin/sleep"'
op|']'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
string|"'-9'"
op|','
name|'os'
op|'.'
name|'getpid'
op|'('
op|')'
op|']'
newline|'\n'
comment|'# Our own PID does not match /bin/sleep, so it should fail'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'f'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
string|"'-9'"
op|','
number|'999999'
op|']'
newline|'\n'
comment|'# Nonexistant PID should fail'
nl|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'f'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
name|'p'
op|'.'
name|'pid'
op|']'
newline|'\n'
comment|'# Providing no signal should work'
nl|'\n'
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
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
string|"'-9'"
op|','
name|'p'
op|'.'
name|'pid'
op|']'
newline|'\n'
comment|'# Providing -9 signal should work'
nl|'\n'
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
nl|'\n'
DECL|member|test_KillFilter_no_raise
dedent|''
name|'def'
name|'test_KillFilter_no_raise'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure ValueError from bug 926412 is gone"""'
newline|'\n'
name|'f'
op|'='
name|'filters'
op|'.'
name|'KillFilter'
op|'('
string|'"/bin/kill"'
op|','
string|'"root"'
op|','
op|'['
string|'""'
op|']'
op|')'
newline|'\n'
comment|'# Providing anything other than kill should be False'
nl|'\n'
name|'usercmd'
op|'='
op|'['
string|"'notkill'"
op|','
number|'999999'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'f'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
comment|'# Providing something that is not a pid should be False'
nl|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
string|"'notapid'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'f'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ReadFileFilter
dedent|''
name|'def'
name|'test_ReadFileFilter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'goodfn'
op|'='
string|"'/good/file.name'"
newline|'\n'
name|'f'
op|'='
name|'filters'
op|'.'
name|'ReadFileFilter'
op|'('
name|'goodfn'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'cat'"
op|','
string|"'/bad/file'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'f'
op|'.'
name|'match'
op|'('
op|'['
string|"'cat'"
op|','
string|"'/bad/file'"
op|']'
op|')'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'cat'"
op|','
name|'goodfn'
op|']'
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
op|'['
string|"'/bin/cat'"
op|','
name|'goodfn'
op|']'
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
