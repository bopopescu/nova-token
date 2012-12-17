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
name|'ConfigParser'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'logging'
op|'.'
name|'handlers'
newline|'\n'
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
string|'"/nonexistent/cat"'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'wrapper'
op|'.'
name|'NoFilterMatched'
op|','
nl|'\n'
name|'wrapper'
op|'.'
name|'match_filter'
op|','
name|'self'
op|'.'
name|'filters'
op|','
name|'usercmd'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'wrapper'
op|'.'
name|'FilterMatchNotExecutable'
op|','
nl|'\n'
name|'wrapper'
op|'.'
name|'match_filter'
op|','
name|'self'
op|'.'
name|'filters'
op|','
name|'valid_but_missing'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'wrapper'
op|'.'
name|'NoFilterMatched'
op|','
nl|'\n'
name|'wrapper'
op|'.'
name|'match_filter'
op|','
name|'self'
op|'.'
name|'filters'
op|','
name|'invalid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_DnsmasqFilter
dedent|''
name|'def'
name|'_test_DnsmasqFilter'
op|'('
name|'self'
op|','
name|'filter_class'
op|','
name|'config_file_arg'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'usercmd'
op|'='
op|'['
string|"'env'"
op|','
name|'config_file_arg'
op|'+'
string|"'=A'"
op|','
string|"'NETWORK_ID=foobar'"
op|','
nl|'\n'
string|"'dnsmasq'"
op|','
string|"'foo'"
op|']'
newline|'\n'
name|'f'
op|'='
name|'filter_class'
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
name|'config_file_arg'
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
name|'self'
op|'.'
name|'_test_DnsmasqFilter'
op|'('
name|'filters'
op|'.'
name|'DnsmasqFilter'
op|','
string|"'CONFIG_FILE'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_DeprecatedDnsmasqFilter
dedent|''
name|'def'
name|'test_DeprecatedDnsmasqFilter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_DnsmasqFilter'
op|'('
name|'filters'
op|'.'
name|'DeprecatedDnsmasqFilter'
op|','
string|"'FLAGFILE'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_KillFilter
dedent|''
name|'def'
name|'test_KillFilter'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
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
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'skipTest'
op|'('
string|'"Test requires /proc filesystem (procfs)"'
op|')'
newline|'\n'
dedent|''
name|'p'
op|'='
name|'subprocess'
op|'.'
name|'Popen'
op|'('
op|'['
string|'"cat"'
op|']'
op|','
name|'stdin'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
nl|'\n'
name|'stdout'
op|'='
name|'subprocess'
op|'.'
name|'PIPE'
op|','
nl|'\n'
name|'stderr'
op|'='
name|'subprocess'
op|'.'
name|'STDOUT'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'='
name|'filters'
op|'.'
name|'KillFilter'
op|'('
string|'"root"'
op|','
string|'"/bin/cat"'
op|','
string|'"-9"'
op|','
string|'"-HUP"'
op|')'
newline|'\n'
name|'f2'
op|'='
name|'filters'
op|'.'
name|'KillFilter'
op|'('
string|'"root"'
op|','
string|'"/usr/bin/cat"'
op|','
string|'"-9"'
op|','
string|'"-HUP"'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
string|"'-ALRM'"
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
name|'or'
name|'f2'
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
name|'or'
name|'f2'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
comment|'# Providing matching signal should be allowed'
nl|'\n'
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
name|'or'
name|'f2'
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
string|'"root"'
op|','
string|'"/bin/cat"'
op|')'
newline|'\n'
name|'f2'
op|'='
name|'filters'
op|'.'
name|'KillFilter'
op|'('
string|'"root"'
op|','
string|'"/usr/bin/cat"'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
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
name|'or'
name|'f2'
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
number|'999999'
op|']'
newline|'\n'
comment|'# Nonexistent PID should fail'
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
name|'or'
name|'f2'
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
name|'or'
name|'f2'
op|'.'
name|'match'
op|'('
name|'usercmd'
op|')'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# Terminate the "cat" process and wait for it to finish'
nl|'\n'
indent|'            '
name|'p'
op|'.'
name|'terminate'
op|'('
op|')'
newline|'\n'
name|'p'
op|'.'
name|'wait'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_KillFilter_no_raise
dedent|''
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
string|'"root"'
op|','
string|'""'
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
DECL|member|test_KillFilter_deleted_exe
dedent|''
name|'def'
name|'test_KillFilter_deleted_exe'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Makes sure deleted exe\'s are killed correctly"""'
newline|'\n'
comment|'# See bug #967931.'
nl|'\n'
DECL|function|fake_readlink
name|'def'
name|'fake_readlink'
op|'('
name|'blah'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'/bin/commandddddd (deleted)'"
newline|'\n'
nl|'\n'
dedent|''
name|'f'
op|'='
name|'filters'
op|'.'
name|'KillFilter'
op|'('
string|'"root"'
op|','
string|'"/bin/commandddddd"'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'kill'"
op|','
number|'1234'
op|']'
newline|'\n'
comment|'# Providing no signal should work'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'os'
op|','
string|"'readlink'"
op|','
name|'fake_readlink'
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
DECL|member|test_exec_dirs_search
dedent|''
name|'def'
name|'test_exec_dirs_search'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# This test supposes you have /bin/cat or /usr/bin/cat locally'
nl|'\n'
indent|'        '
name|'f'
op|'='
name|'filters'
op|'.'
name|'CommandFilter'
op|'('
string|'"cat"'
op|','
string|'"root"'
op|')'
newline|'\n'
name|'usercmd'
op|'='
op|'['
string|"'cat'"
op|','
string|"'/f'"
op|']'
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
name|'assertTrue'
op|'('
name|'f'
op|'.'
name|'get_command'
op|'('
name|'usercmd'
op|','
name|'exec_dirs'
op|'='
op|'['
string|"'/bin'"
op|','
nl|'\n'
string|"'/usr/bin'"
op|']'
op|')'
name|'in'
op|'('
op|'['
string|"'/bin/cat'"
op|','
string|"'/f'"
op|']'
op|','
op|'['
string|"'/usr/bin/cat'"
op|','
string|"'/f'"
op|']'
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
nl|'\n'
DECL|member|test_RootwrapConfig
dedent|''
name|'def'
name|'test_RootwrapConfig'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raw'
op|'='
name|'ConfigParser'
op|'.'
name|'RawConfigParser'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# Empty config should raise ConfigParser.Error'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ConfigParser'
op|'.'
name|'Error'
op|','
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|','
name|'raw'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check default values'
nl|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'filters_path'"
op|','
string|"'/a,/b'"
op|')'
newline|'\n'
name|'config'
op|'='
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|'('
name|'raw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'config'
op|'.'
name|'filters_path'
op|','
op|'['
string|"'/a'"
op|','
string|"'/b'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'config'
op|'.'
name|'exec_dirs'
op|','
name|'os'
op|'.'
name|'environ'
op|'['
string|'"PATH"'
op|']'
op|'.'
name|'split'
op|'('
string|"':'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'config'
op|'.'
name|'use_syslog'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'config'
op|'.'
name|'syslog_log_facility'
op|','
nl|'\n'
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'.'
name|'LOG_SYSLOG'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'config'
op|'.'
name|'syslog_log_level'
op|','
name|'logging'
op|'.'
name|'ERROR'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check general values'
nl|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'exec_dirs'"
op|','
string|"'/a,/x'"
op|')'
newline|'\n'
name|'config'
op|'='
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|'('
name|'raw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'config'
op|'.'
name|'exec_dirs'
op|','
op|'['
string|"'/a'"
op|','
string|"'/x'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'use_syslog'"
op|','
string|"'oui'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|','
name|'raw'
op|')'
newline|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'use_syslog'"
op|','
string|"'true'"
op|')'
newline|'\n'
name|'config'
op|'='
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|'('
name|'raw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'config'
op|'.'
name|'use_syslog'
op|')'
newline|'\n'
nl|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'syslog_log_facility'"
op|','
string|"'moo'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|','
name|'raw'
op|')'
newline|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'syslog_log_facility'"
op|','
string|"'local0'"
op|')'
newline|'\n'
name|'config'
op|'='
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|'('
name|'raw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'config'
op|'.'
name|'syslog_log_facility'
op|','
nl|'\n'
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'.'
name|'LOG_LOCAL0'
op|')'
newline|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'syslog_log_facility'"
op|','
string|"'LOG_AUTH'"
op|')'
newline|'\n'
name|'config'
op|'='
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|'('
name|'raw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'config'
op|'.'
name|'syslog_log_facility'
op|','
nl|'\n'
name|'logging'
op|'.'
name|'handlers'
op|'.'
name|'SysLogHandler'
op|'.'
name|'LOG_AUTH'
op|')'
newline|'\n'
nl|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'syslog_log_level'"
op|','
string|"'bar'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|','
name|'raw'
op|')'
newline|'\n'
name|'raw'
op|'.'
name|'set'
op|'('
string|"'DEFAULT'"
op|','
string|"'syslog_log_level'"
op|','
string|"'INFO'"
op|')'
newline|'\n'
name|'config'
op|'='
name|'wrapper'
op|'.'
name|'RootwrapConfig'
op|'('
name|'raw'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'config'
op|'.'
name|'syslog_log_level'
op|','
name|'logging'
op|'.'
name|'INFO'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
