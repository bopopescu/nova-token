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
string|'"""Text Views With Headers\n\nThis package defines several text views with headers\n"""'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HeaderView
name|'class'
name|'HeaderView'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Text View With a Header\n\n    This view simply serializes the model and places the given\n    header on top.\n\n    :param header: the header (can be anything on which str() can be called)\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'header'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'header'
op|'='
name|'header'
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
name|'str'
op|'('
name|'self'
op|'.'
name|'header'
op|')'
op|'+'
string|'"\\n"'
op|'+'
name|'str'
op|'('
name|'model'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TitledView
dedent|''
dedent|''
name|'class'
name|'TitledView'
op|'('
name|'HeaderView'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A Text View With a Title\n\n    This view simply serializes the model, and places\n    a preformatted header containing the given title\n    text on top.  The title text can be up to 64 characters\n    long.\n\n    :param str title:  the title of the view\n    """'
newline|'\n'
nl|'\n'
DECL|variable|FORMAT_STR
name|'FORMAT_STR'
op|'='
op|'('
string|"'='"
op|'*'
number|'72'
op|')'
op|'+'
string|'"\\n===={0: ^64}====\\n"'
op|'+'
op|'('
string|"'='"
op|'*'
number|'72'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'title'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'TitledView'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'self'
op|'.'
name|'FORMAT_STR'
op|'.'
name|'format'
op|'('
name|'title'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit