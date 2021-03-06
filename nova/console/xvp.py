begin_unit
comment|'# Copyright (c) 2010 OpenStack Foundation'
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
string|'"""XVP (Xenserver VNC Proxy) driver."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'signal'
newline|'\n'
nl|'\n'
name|'import'
name|'jinja2'
newline|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'excutils'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'conf'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
op|','
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'nova'
op|'.'
name|'conf'
op|'.'
name|'CONF'
newline|'\n'
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
DECL|class|XVPConsoleProxy
name|'class'
name|'XVPConsoleProxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Sets up XVP config, and manages XVP daemon."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'xvpconf_template'
op|'='
name|'open'
op|'('
name|'CONF'
op|'.'
name|'console_xvp_conf_template'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'host'
op|'='
name|'CONF'
op|'.'
name|'host'
comment|'# default, set by manager.'
newline|'\n'
name|'super'
op|'('
name|'XVPConsoleProxy'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|console_type
name|'def'
name|'console_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'vnc+xvp'"
newline|'\n'
nl|'\n'
DECL|member|get_port
dedent|''
name|'def'
name|'get_port'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get available port for consoles that need one."""'
newline|'\n'
comment|'# TODO(mdragon): implement port selection for non multiplex ports,'
nl|'\n'
comment|'#               we are not using that, but someone else may want'
nl|'\n'
comment|'#               it.'
nl|'\n'
name|'return'
name|'CONF'
op|'.'
name|'console_xvp_multiplex_port'
newline|'\n'
nl|'\n'
DECL|member|setup_console
dedent|''
name|'def'
name|'setup_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'console'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Sets up actual proxies."""'
newline|'\n'
name|'self'
op|'.'
name|'_rebuild_xvp_conf'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|teardown_console
dedent|''
name|'def'
name|'teardown_console'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'console'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Tears down actual proxies."""'
newline|'\n'
name|'self'
op|'.'
name|'_rebuild_xvp_conf'
op|'('
name|'context'
op|'.'
name|'elevated'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start up any config\'ed consoles on start."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_rebuild_xvp_conf'
op|'('
name|'ctxt'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fix_pool_password
dedent|''
name|'def'
name|'fix_pool_password'
op|'('
name|'self'
op|','
name|'password'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Trim password to length, and encode."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_xvp_encrypt'
op|'('
name|'password'
op|','
name|'is_pool_password'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|fix_console_password
dedent|''
name|'def'
name|'fix_console_password'
op|'('
name|'self'
op|','
name|'password'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Trim password to length, and encode."""'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_xvp_encrypt'
op|'('
name|'password'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_rebuild_xvp_conf
dedent|''
name|'def'
name|'_rebuild_xvp_conf'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Rebuilding xvp conf'"
op|')'
newline|'\n'
name|'pools'
op|'='
op|'['
name|'pool'
name|'for'
name|'pool'
name|'in'
nl|'\n'
name|'db'
op|'.'
name|'console_pool_get_all_by_host_type'
op|'('
name|'context'
op|','
name|'self'
op|'.'
name|'host'
op|','
nl|'\n'
name|'self'
op|'.'
name|'console_type'
op|')'
nl|'\n'
name|'if'
name|'pool'
op|'['
string|"'consoles'"
op|']'
op|']'
newline|'\n'
name|'if'
name|'not'
name|'pools'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'No console pools!'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_xvp_stop'
op|'('
op|')'
newline|'\n'
name|'return'
newline|'\n'
dedent|''
name|'conf_data'
op|'='
op|'{'
string|"'multiplex_port'"
op|':'
name|'CONF'
op|'.'
name|'console_xvp_multiplex_port'
op|','
nl|'\n'
string|"'pools'"
op|':'
name|'pools'
op|'}'
newline|'\n'
name|'tmpl_path'
op|','
name|'tmpl_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
name|'CONF'
op|'.'
name|'injected_network_template'
op|')'
newline|'\n'
name|'env'
op|'='
name|'jinja2'
op|'.'
name|'Environment'
op|'('
name|'loader'
op|'='
name|'jinja2'
op|'.'
name|'FileSystemLoader'
op|'('
name|'tmpl_path'
op|')'
op|')'
newline|'\n'
name|'env'
op|'.'
name|'filters'
op|'['
string|"'pass_encode'"
op|']'
op|'='
name|'self'
op|'.'
name|'fix_console_password'
newline|'\n'
name|'template'
op|'='
name|'env'
op|'.'
name|'get_template'
op|'('
name|'tmpl_file'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_write_conf'
op|'('
name|'template'
op|'.'
name|'render'
op|'('
name|'conf_data'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_xvp_restart'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_write_conf
dedent|''
name|'def'
name|'_write_conf'
op|'('
name|'self'
op|','
name|'config'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Re-wrote %s'"
op|','
name|'CONF'
op|'.'
name|'console_xvp_conf'
op|')'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'CONF'
op|'.'
name|'console_xvp_conf'
op|','
string|"'w'"
op|')'
name|'as'
name|'cfile'
op|':'
newline|'\n'
indent|'                '
name|'cfile'
op|'.'
name|'write'
op|'('
name|'config'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Failed to write configuration file"'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_xvp_stop
dedent|''
dedent|''
dedent|''
name|'def'
name|'_xvp_stop'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Stopping xvp'"
op|')'
newline|'\n'
name|'pid'
op|'='
name|'self'
op|'.'
name|'_xvp_pid'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pid'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGTERM'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|':'
newline|'\n'
comment|"# if it's already not running, no problem."
nl|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_xvp_start
dedent|''
dedent|''
name|'def'
name|'_xvp_start'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'_xvp_check_running'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Starting xvp'"
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'xvp'"
op|','
nl|'\n'
string|"'-p'"
op|','
name|'CONF'
op|'.'
name|'console_xvp_pid'
op|','
nl|'\n'
string|"'-c'"
op|','
name|'CONF'
op|'.'
name|'console_xvp_conf'
op|','
nl|'\n'
string|"'-l'"
op|','
name|'CONF'
op|'.'
name|'console_xvp_log'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'Error starting xvp: %s'"
op|')'
op|','
name|'err'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_xvp_restart
dedent|''
dedent|''
name|'def'
name|'_xvp_restart'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Restarting xvp'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_xvp_check_running'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'xvp not running...'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_xvp_start'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'pid'
op|'='
name|'self'
op|'.'
name|'_xvp_pid'
op|'('
op|')'
newline|'\n'
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
name|'signal'
op|'.'
name|'SIGUSR1'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_xvp_pid
dedent|''
dedent|''
name|'def'
name|'_xvp_pid'
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
name|'with'
name|'open'
op|'('
name|'CONF'
op|'.'
name|'console_xvp_pid'
op|','
string|"'r'"
op|')'
name|'as'
name|'pidfile'
op|':'
newline|'\n'
indent|'                '
name|'pid'
op|'='
name|'int'
op|'('
name|'pidfile'
op|'.'
name|'read'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'IOError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'pid'
newline|'\n'
nl|'\n'
DECL|member|_xvp_check_running
dedent|''
name|'def'
name|'_xvp_check_running'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pid'
op|'='
name|'self'
op|'.'
name|'_xvp_pid'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pid'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'kill'
op|'('
name|'pid'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'OSError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_xvp_encrypt
dedent|''
name|'def'
name|'_xvp_encrypt'
op|'('
name|'self'
op|','
name|'password'
op|','
name|'is_pool_password'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call xvp to obfuscate passwords for config file.\n\n        Args:\n            - password: the password to encode, max 8 char for vm passwords,\n                        and 16 chars for pool passwords. passwords will\n                        be trimmed to max len before encoding.\n            - is_pool_password: True if this is the XenServer api password\n                                False if it\'s a VM console password\n              (xvp uses different keys and max lengths for pool passwords)\n\n        Note that xvp\'s obfuscation should not be considered \'real\' encryption.\n        It simply DES encrypts the passwords with static keys plainly viewable\n        in the xvp source code.\n\n        """'
newline|'\n'
name|'maxlen'
op|'='
number|'8'
newline|'\n'
name|'flag'
op|'='
string|"'-e'"
newline|'\n'
name|'if'
name|'is_pool_password'
op|':'
newline|'\n'
indent|'            '
name|'maxlen'
op|'='
number|'16'
newline|'\n'
name|'flag'
op|'='
string|"'-x'"
newline|'\n'
comment|'# xvp will blow up on passwords that are too long (mdragon)'
nl|'\n'
dedent|''
name|'password'
op|'='
name|'password'
op|'['
op|':'
name|'maxlen'
op|']'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'xvp'"
op|','
name|'flag'
op|','
name|'process_input'
op|'='
name|'password'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
op|'('
name|'_'
op|'('
string|'"Failed to run xvp."'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
