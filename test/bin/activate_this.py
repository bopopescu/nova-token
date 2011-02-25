begin_unit
string|'"""By using execfile(this_file, dict(__file__=this_file)) you will\nactivate this virtualenv environment.\n\nThis can be used when you must use an existing Python interpreter, not\nthe virtualenv bin/python\n"""'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'__file__'
newline|'\n'
dedent|''
name|'except'
name|'NameError'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'AssertionError'
op|'('
nl|'\n'
string|'"You must run this like execfile(\'path/to/activate_this.py\', dict(__file__=\'path/to/activate_this.py\'))"'
op|')'
newline|'\n'
dedent|''
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
DECL|variable|base
name|'base'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'abspath'
op|'('
name|'__file__'
op|')'
op|')'
op|')'
newline|'\n'
name|'if'
name|'sys'
op|'.'
name|'platform'
op|'=='
string|"'win32'"
op|':'
newline|'\n'
DECL|variable|site_packages
indent|'    '
name|'site_packages'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base'
op|','
string|"'Lib'"
op|','
string|"'site-packages'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|variable|site_packages
indent|'    '
name|'site_packages'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'base'
op|','
string|"'lib'"
op|','
string|"'python%s'"
op|'%'
name|'sys'
op|'.'
name|'version'
op|'['
op|':'
number|'3'
op|']'
op|','
string|"'site-packages'"
op|')'
newline|'\n'
DECL|variable|prev_sys_path
dedent|''
name|'prev_sys_path'
op|'='
name|'list'
op|'('
name|'sys'
op|'.'
name|'path'
op|')'
newline|'\n'
name|'import'
name|'site'
newline|'\n'
name|'site'
op|'.'
name|'addsitedir'
op|'('
name|'site_packages'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'real_prefix'
op|'='
name|'sys'
op|'.'
name|'prefix'
newline|'\n'
name|'sys'
op|'.'
name|'prefix'
op|'='
name|'base'
newline|'\n'
comment|'# Move the added items to the front of the path:'
nl|'\n'
DECL|variable|new_sys_path
name|'new_sys_path'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'list'
op|'('
name|'sys'
op|'.'
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'item'
name|'not'
name|'in'
name|'prev_sys_path'
op|':'
newline|'\n'
indent|'        '
name|'new_sys_path'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
name|'sys'
op|'.'
name|'path'
op|'.'
name|'remove'
op|'('
name|'item'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'sys'
op|'.'
name|'path'
op|'['
op|':'
number|'0'
op|']'
op|'='
name|'new_sys_path'
newline|'\n'
endmarker|''
end_unit
