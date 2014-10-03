begin_unit
comment|'# Copyright 2013 Red Hat, Inc.'
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
string|'"""Provides Jinja Views\n\nThis module provides views that utilize the Jinja templating\nsystem for serialization.  For more information on Jinja, please\nsee http://jinja.pocoo.org/ .\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'import'
name|'jinja2'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|JinjaView
name|'class'
name|'JinjaView'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Jinja View\n\n    This view renders the given model using the provided Jinja\n    template.  The template can be given in various ways.\n    If the `VIEw_TEXT` property is defined, that is used as template.\n    Othewise, if a `path` parameter is passed to the constructor, that\n    is used to load a file containing the template.  If the `path`\n    parameter is None, the `text` parameter is used as the template.\n\n    The leading newline character and trailing newline character are stripped\n    from the template (provided they exist).  Baseline indentation is\n    also stripped from each line.  The baseline indentation is determined by\n    checking the indentation of the first line, after stripping off the leading\n    newline (if any).\n\n    :param str path: the path to the Jinja template\n    :param str text: the text of the Jinja template\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'path'
op|'='
name|'None'
op|','
name|'text'
op|'='
name|'None'
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
name|'_text'
op|'='
name|'self'
op|'.'
name|'VIEW_TEXT'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'path'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|"'r'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_text'
op|'='
name|'f'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'text'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_text'
op|'='
name|'text'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_text'
op|'='
string|'""'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'_text'
op|'['
number|'0'
op|']'
op|'=='
string|'"\\n"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_text'
op|'='
name|'self'
op|'.'
name|'_text'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'newtext'
op|'='
name|'self'
op|'.'
name|'_text'
op|'.'
name|'lstrip'
op|'('
op|')'
newline|'\n'
name|'amt'
op|'='
name|'len'
op|'('
name|'self'
op|'.'
name|'_text'
op|')'
op|'-'
name|'len'
op|'('
name|'newtext'
op|')'
newline|'\n'
name|'if'
op|'('
name|'amt'
op|'>'
number|'0'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'base_indent'
op|'='
name|'self'
op|'.'
name|'_text'
op|'['
number|'0'
op|':'
name|'amt'
op|']'
newline|'\n'
name|'lines'
op|'='
name|'self'
op|'.'
name|'_text'
op|'.'
name|'splitlines'
op|'('
op|')'
newline|'\n'
name|'newlines'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'lines'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'line'
op|'.'
name|'startswith'
op|'('
name|'base_indent'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'newlines'
op|'.'
name|'append'
op|'('
name|'line'
op|'['
name|'amt'
op|':'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'newlines'
op|'.'
name|'append'
op|'('
name|'line'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'_text'
op|'='
string|'"\\n"'
op|'.'
name|'join'
op|'('
name|'newlines'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_text'
op|'['
op|'-'
number|'1'
op|']'
op|'=='
string|'"\\n"'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_text'
op|'='
name|'self'
op|'.'
name|'_text'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_regentemplate'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'_templatecache'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'model'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'template'
op|'.'
name|'render'
op|'('
op|'**'
name|'model'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__deepcopy__
dedent|''
name|'def'
name|'__deepcopy__'
op|'('
name|'self'
op|','
name|'memodict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res'
op|'='
name|'object'
op|'.'
name|'__new__'
op|'('
name|'JinjaView'
op|')'
newline|'\n'
name|'res'
op|'.'
name|'_text'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'self'
op|'.'
name|'_text'
op|','
name|'memodict'
op|')'
newline|'\n'
nl|'\n'
comment|'# regenerate the template on a deepcopy'
nl|'\n'
name|'res'
op|'.'
name|'_regentemplate'
op|'='
name|'True'
newline|'\n'
name|'res'
op|'.'
name|'_templatecache'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'return'
name|'res'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|template
name|'def'
name|'template'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the Compiled Template\n\n        Gets the compiled template, using a cached copy if possible\n        (stored in attr:`_templatecache`) or otherwise recompiling\n        the template if the compiled template is not present or is\n        invalid (due to attr:`_regentemplate` being set to True).\n\n        :returns: the compiled Jinja template\n        :rtype: :class:`jinja2.Template`\n        """'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'_templatecache'
name|'is'
name|'None'
name|'or'
name|'self'
op|'.'
name|'_regentemplate'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_templatecache'
op|'='
name|'jinja2'
op|'.'
name|'Template'
op|'('
name|'self'
op|'.'
name|'_text'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_regentemplate'
op|'='
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_templatecache'
newline|'\n'
nl|'\n'
DECL|member|_gettext
dedent|''
name|'def'
name|'_gettext'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Get the Template Text\n\n        Gets the text of the current template\n\n        :returns: the text of the Jinja template\n        :rtype: str\n        """'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'_text'
newline|'\n'
nl|'\n'
DECL|member|_settext
dedent|''
name|'def'
name|'_settext'
op|'('
name|'self'
op|','
name|'textval'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Set the Template Text\n\n        Sets the text of the current template, marking it\n        for recompilation next time the compiled template\n        is retrived via attr:`template` .\n\n        :param str textval: the new text of the Jinja template\n        """'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_text'
op|'='
name|'textval'
newline|'\n'
name|'self'
op|'.'
name|'regentemplate'
op|'='
name|'True'
newline|'\n'
nl|'\n'
DECL|variable|text
dedent|''
name|'text'
op|'='
name|'property'
op|'('
name|'_gettext'
op|','
name|'_settext'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
