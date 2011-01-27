begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
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
name|'glob'
newline|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LocalizationTestCase
name|'class'
name|'LocalizationTestCase'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_multiple_positional_format_placeholders
indent|'    '
name|'def'
name|'test_multiple_positional_format_placeholders'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pat'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"\\W_\\("'
op|')'
newline|'\n'
name|'single_pat'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|'"\\W%\\W"'
op|')'
newline|'\n'
name|'root_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'nova'
op|'.'
name|'__file__'
op|')'
newline|'\n'
name|'problems'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'root'
op|','
name|'dirs'
op|','
name|'files'
name|'in'
name|'os'
op|'.'
name|'walk'
op|'('
name|'root_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'fname'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'fname'
op|'.'
name|'endswith'
op|'('
string|'".py"'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'pth'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'root'
op|','
name|'fname'
op|')'
newline|'\n'
name|'txt'
op|'='
name|'fulltext'
op|'='
name|'file'
op|'('
name|'pth'
op|')'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
name|'txt_lines'
op|'='
name|'fulltext'
op|'.'
name|'splitlines'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'pat'
op|'.'
name|'search'
op|'('
name|'txt'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'problems'
op|'['
name|'pth'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'pos'
op|'='
name|'txt'
op|'.'
name|'find'
op|'('
string|'"_("'
op|')'
newline|'\n'
name|'while'
name|'pos'
op|'>'
op|'-'
number|'1'
op|':'
newline|'\n'
comment|"# Make sure that this isn't part of a dunder;"
nl|'\n'
comment|'# e.g., __init__(...'
nl|'\n'
comment|"# or something like 'self.assert_(...'"
nl|'\n'
indent|'                    '
name|'test_txt'
op|'='
name|'txt'
op|'['
name|'pos'
op|'-'
number|'1'
op|':'
name|'pos'
op|'+'
number|'10'
op|']'
newline|'\n'
name|'if'
name|'not'
op|'('
name|'pat'
op|'.'
name|'search'
op|'('
name|'test_txt'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'txt'
op|'='
name|'txt'
op|'['
name|'pos'
op|'+'
number|'2'
op|':'
op|']'
newline|'\n'
name|'pos'
op|'='
name|'txt'
op|'.'
name|'find'
op|'('
string|'"_("'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
dedent|''
name|'pos'
op|'+='
number|'2'
newline|'\n'
name|'txt'
op|'='
name|'txt'
op|'['
name|'pos'
op|':'
op|']'
newline|'\n'
name|'innerChars'
op|'='
op|'['
op|']'
newline|'\n'
comment|'# Count pairs of open/close parens until _() closing'
nl|'\n'
comment|'# paren is found.'
nl|'\n'
name|'parenCount'
op|'='
number|'1'
newline|'\n'
name|'pos'
op|'='
number|'0'
newline|'\n'
name|'while'
name|'parenCount'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                        '
name|'char'
op|'='
name|'txt'
op|'['
name|'pos'
op|']'
newline|'\n'
name|'if'
name|'char'
op|'=='
string|'"("'
op|':'
newline|'\n'
indent|'                            '
name|'parenCount'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'elif'
name|'char'
op|'=='
string|'")"'
op|':'
newline|'\n'
indent|'                            '
name|'parenCount'
op|'-='
number|'1'
newline|'\n'
dedent|''
name|'innerChars'
op|'.'
name|'append'
op|'('
name|'char'
op|')'
newline|'\n'
name|'pos'
op|'+='
number|'1'
newline|'\n'
dedent|''
name|'inner_all'
op|'='
string|'""'
op|'.'
name|'join'
op|'('
name|'innerChars'
op|')'
newline|'\n'
comment|"# Filter out '%%' and '%('"
nl|'\n'
name|'inner'
op|'='
name|'inner_all'
op|'.'
name|'replace'
op|'('
string|'"%%"'
op|','
string|'""'
op|')'
op|'.'
name|'replace'
op|'('
string|'"%("'
op|','
string|'""'
op|')'
newline|'\n'
comment|"# Filter out the single '%' operators"
nl|'\n'
name|'inner'
op|'='
name|'single_pat'
op|'.'
name|'sub'
op|'('
string|'""'
op|','
name|'inner'
op|')'
newline|'\n'
comment|'# Within the remaining content, count %'
nl|'\n'
name|'fmtCount'
op|'='
name|'inner'
op|'.'
name|'count'
op|'('
string|'"%"'
op|')'
newline|'\n'
name|'if'
name|'fmtCount'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                        '
name|'inner_first'
op|'='
name|'inner_all'
op|'.'
name|'splitlines'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'lns'
op|'='
op|'['
string|'"%s"'
op|'%'
op|'('
name|'p'
op|'+'
number|'1'
op|')'
nl|'\n'
name|'for'
name|'p'
op|','
name|'t'
name|'in'
name|'enumerate'
op|'('
name|'txt_lines'
op|')'
nl|'\n'
name|'if'
name|'inner_first'
name|'in'
name|'t'
op|']'
newline|'\n'
name|'lnums'
op|'='
string|'", "'
op|'.'
name|'join'
op|'('
name|'lns'
op|')'
newline|'\n'
comment|'# Using ugly string concatenation to avoid having'
nl|'\n'
comment|'# this test fail itself.'
nl|'\n'
name|'inner_all'
op|'='
string|'"_"'
op|'+'
string|'"("'
op|'+'
string|'"%s"'
op|'%'
name|'inner_all'
newline|'\n'
name|'problems'
op|'['
name|'pth'
op|']'
op|'.'
name|'append'
op|'('
string|'"Line: %s Text: %s"'
op|'%'
nl|'\n'
op|'('
name|'lnums'
op|','
name|'inner_all'
op|')'
op|')'
newline|'\n'
comment|'# Look for more'
nl|'\n'
dedent|''
name|'pos'
op|'='
name|'txt'
op|'.'
name|'find'
op|'('
string|'"_("'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'problems'
op|'['
name|'pth'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'del'
name|'problems'
op|'['
name|'pth'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'problems'
op|':'
newline|'\n'
indent|'            '
name|'out'
op|'='
op|'['
string|'"Problem(s) found in localized string formatting"'
op|','
nl|'\n'
string|'"(see http://www.gnu.org/software/hello/manual/"'
nl|'\n'
string|'"gettext/Python.html for more information)"'
op|','
nl|'\n'
string|'""'
op|','
nl|'\n'
string|'"    ------------ Files to fix ------------"'
op|']'
newline|'\n'
name|'for'
name|'pth'
name|'in'
name|'problems'
op|':'
newline|'\n'
indent|'                '
name|'out'
op|'.'
name|'append'
op|'('
string|'"    %s:"'
op|'%'
name|'pth'
op|')'
newline|'\n'
name|'for'
name|'val'
name|'in'
name|'set'
op|'('
name|'problems'
op|'['
name|'pth'
op|']'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'out'
op|'.'
name|'append'
op|'('
string|'"        %s"'
op|'%'
name|'val'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'AssertionError'
op|'('
string|'"\\n"'
op|'.'
name|'join'
op|'('
name|'out'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
