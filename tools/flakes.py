begin_unit
string|'"""\n wrapper for pyflakes to ignore gettext based warning:\n     "undefined name \'_\'"\n\n From https://bugs.launchpad.net/pyflakes/+bug/844592\n"""'
newline|'\n'
name|'import'
name|'__builtin__'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'from'
name|'pyflakes'
op|'.'
name|'scripts'
op|'.'
name|'pyflakes'
name|'import'
name|'main'
newline|'\n'
nl|'\n'
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
DECL|variable|names
indent|'    '
name|'names'
op|'='
name|'os'
op|'.'
name|'environ'
op|'.'
name|'get'
op|'('
string|"'PYFLAKES_BUILTINS'"
op|','
string|"'_'"
op|')'
newline|'\n'
DECL|variable|names
name|'names'
op|'='
op|'['
name|'x'
op|'.'
name|'strip'
op|'('
op|')'
name|'for'
name|'x'
name|'in'
name|'names'
op|'.'
name|'split'
op|'('
string|"','"
op|')'
op|']'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'names'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'__builtin__'
op|','
name|'x'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'__builtin__'
op|','
name|'x'
op|','
name|'True'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'del'
name|'names'
op|','
name|'os'
op|','
name|'__builtin__'
newline|'\n'
nl|'\n'
name|'sys'
op|'.'
name|'exit'
op|'('
name|'main'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
