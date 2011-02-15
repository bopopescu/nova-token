begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
string|'"""\nPackage-level global flags are defined here, the rest are defined\nwhere they\'re used.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'getopt'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'socket'
newline|'\n'
name|'import'
name|'string'
newline|'\n'
name|'import'
name|'sys'
newline|'\n'
nl|'\n'
name|'import'
name|'gflags'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FlagValues
name|'class'
name|'FlagValues'
op|'('
name|'gflags'
op|'.'
name|'FlagValues'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extension of gflags.FlagValues that allows undefined and runtime flags.\n\n    Unknown flags will be ignored when parsing the command line, but the\n    command line will be kept so that it can be replayed if new flags are\n    defined after the initial parsing.\n\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'extra_context'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'gflags'
op|'.'
name|'FlagValues'
op|'.'
name|'__init__'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__dirty'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__was_already_parsed'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__stored_argv'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__extra_context'"
op|']'
op|'='
name|'extra_context'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'argv'
op|')'
op|':'
newline|'\n'
comment|"# We're doing some hacky stuff here so that we don't have to copy"
nl|'\n'
comment|'# out all the code of the original verbatim and then tweak a few lines.'
nl|'\n'
comment|"# We're hijacking the output of getopt so we can still return the"
nl|'\n'
comment|'# leftover args at the end'
nl|'\n'
indent|'        '
name|'sneaky_unparsed_args'
op|'='
op|'{'
string|'"value"'
op|':'
name|'None'
op|'}'
newline|'\n'
name|'original_argv'
op|'='
name|'list'
op|'('
name|'argv'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'IsGnuGetOpt'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'orig_getopt'
op|'='
name|'getattr'
op|'('
name|'getopt'
op|','
string|"'gnu_getopt'"
op|')'
newline|'\n'
name|'orig_name'
op|'='
string|"'gnu_getopt'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'orig_getopt'
op|'='
name|'getattr'
op|'('
name|'getopt'
op|','
string|"'getopt'"
op|')'
newline|'\n'
name|'orig_name'
op|'='
string|"'getopt'"
newline|'\n'
nl|'\n'
DECL|function|_sneaky
dedent|''
name|'def'
name|'_sneaky'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'optlist'
op|','
name|'unparsed_args'
op|'='
name|'orig_getopt'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
name|'sneaky_unparsed_args'
op|'['
string|"'value'"
op|']'
op|'='
name|'unparsed_args'
newline|'\n'
name|'return'
name|'optlist'
op|','
name|'unparsed_args'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'getopt'
op|','
name|'orig_name'
op|','
name|'_sneaky'
op|')'
newline|'\n'
name|'args'
op|'='
name|'gflags'
op|'.'
name|'FlagValues'
op|'.'
name|'__call__'
op|'('
name|'self'
op|','
name|'argv'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'gflags'
op|'.'
name|'UnrecognizedFlagError'
op|':'
newline|'\n'
comment|"# Undefined args were found, for now we don't care so just"
nl|'\n'
comment|'# act like everything went well'
nl|'\n'
comment|'# (these three lines are copied pretty much verbatim from the end'
nl|'\n'
comment|'# of the __call__ function we are wrapping)'
nl|'\n'
indent|'            '
name|'unparsed_args'
op|'='
name|'sneaky_unparsed_args'
op|'['
string|"'value'"
op|']'
newline|'\n'
name|'if'
name|'unparsed_args'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'self'
op|'.'
name|'IsGnuGetOpt'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'='
name|'argv'
op|'['
op|':'
number|'1'
op|']'
op|'+'
name|'unparsed_args'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'args'
op|'='
name|'argv'
op|'['
op|':'
number|'1'
op|']'
op|'+'
name|'original_argv'
op|'['
op|'-'
name|'len'
op|'('
name|'unparsed_args'
op|')'
op|':'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'args'
op|'='
name|'argv'
op|'['
op|':'
number|'1'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'getopt'
op|','
name|'orig_name'
op|','
name|'orig_getopt'
op|')'
newline|'\n'
nl|'\n'
comment|"# Store the arguments for later, we'll need them for new flags"
nl|'\n'
comment|'# added at runtime'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__stored_argv'"
op|']'
op|'='
name|'original_argv'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__was_already_parsed'"
op|']'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'ClearDirty'
op|'('
op|')'
newline|'\n'
name|'return'
name|'args'
newline|'\n'
nl|'\n'
DECL|member|Reset
dedent|''
name|'def'
name|'Reset'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'gflags'
op|'.'
name|'FlagValues'
op|'.'
name|'Reset'
op|'('
name|'self'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__dirty'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__was_already_parsed'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__stored_argv'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|SetDirty
dedent|''
name|'def'
name|'SetDirty'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Mark a flag as dirty so that accessing it will case a reparse."""'
newline|'\n'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__dirty'"
op|']'
op|'.'
name|'append'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|IsDirty
dedent|''
name|'def'
name|'IsDirty'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'name'
name|'in'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__dirty'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|ClearDirty
dedent|''
name|'def'
name|'ClearDirty'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__is_dirty'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|member|WasAlreadyParsed
dedent|''
name|'def'
name|'WasAlreadyParsed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__was_already_parsed'"
op|']'
newline|'\n'
nl|'\n'
DECL|member|ParseNewFlags
dedent|''
name|'def'
name|'ParseNewFlags'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'__stored_argv'"
name|'not'
name|'in'
name|'self'
op|'.'
name|'__dict__'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'new_flags'
op|'='
name|'FlagValues'
op|'('
name|'self'
op|')'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__dirty'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'new_flags'
op|'['
name|'k'
op|']'
op|'='
name|'gflags'
op|'.'
name|'FlagValues'
op|'.'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'k'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'new_flags'
op|'('
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__stored_argv'"
op|']'
op|')'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__dirty'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|','
name|'k'
op|','
name|'getattr'
op|'('
name|'new_flags'
op|','
name|'k'
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'ClearDirty'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|__setitem__
dedent|''
name|'def'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'flag'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'gflags'
op|'.'
name|'FlagValues'
op|'.'
name|'__setitem__'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'flag'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'WasAlreadyParsed'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'SetDirty'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'IsDirty'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ParseNewFlags'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'gflags'
op|'.'
name|'FlagValues'
op|'.'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'IsDirty'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'ParseNewFlags'
op|'('
op|')'
newline|'\n'
dedent|''
name|'val'
op|'='
name|'gflags'
op|'.'
name|'FlagValues'
op|'.'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'name'
op|')'
newline|'\n'
name|'if'
name|'type'
op|'('
name|'val'
op|')'
name|'is'
name|'str'
op|':'
newline|'\n'
indent|'            '
name|'tmpl'
op|'='
name|'string'
op|'.'
name|'Template'
op|'('
name|'val'
op|')'
newline|'\n'
name|'context'
op|'='
op|'['
name|'self'
op|','
name|'self'
op|'.'
name|'__dict__'
op|'['
string|"'__extra_context'"
op|']'
op|']'
newline|'\n'
name|'return'
name|'tmpl'
op|'.'
name|'substitute'
op|'('
name|'StrWrapper'
op|'('
name|'context'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'val'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StrWrapper
dedent|''
dedent|''
name|'class'
name|'StrWrapper'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wrapper around FlagValues objects\n\n    Wraps FlagValues objects for string.Template so that we\'re\n    sure to return strings."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'context_objs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'context_objs'
op|'='
name|'context_objs'
newline|'\n'
nl|'\n'
DECL|member|__getitem__
dedent|''
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'context'
name|'in'
name|'self'
op|'.'
name|'context_objs'
op|':'
newline|'\n'
indent|'            '
name|'val'
op|'='
name|'getattr'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'False'
op|')'
newline|'\n'
name|'if'
name|'val'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'str'
op|'('
name|'val'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'KeyError'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
dedent|''
dedent|''
name|'FLAGS'
op|'='
name|'FlagValues'
op|'('
op|')'
newline|'\n'
name|'gflags'
op|'.'
name|'FLAGS'
op|'='
name|'FLAGS'
newline|'\n'
name|'gflags'
op|'.'
name|'DEFINE_flag'
op|'('
name|'gflags'
op|'.'
name|'HelpFlag'
op|'('
op|')'
op|','
name|'FLAGS'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_wrapper
name|'def'
name|'_wrapper'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
DECL|function|_wrapped
indent|'    '
name|'def'
name|'_wrapped'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kw'
op|'.'
name|'setdefault'
op|'('
string|"'flag_values'"
op|','
name|'FLAGS'
op|')'
newline|'\n'
name|'func'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kw'
op|')'
newline|'\n'
dedent|''
name|'_wrapped'
op|'.'
name|'func_name'
op|'='
name|'func'
op|'.'
name|'func_name'
newline|'\n'
name|'return'
name|'_wrapped'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|DEFINE
dedent|''
name|'DEFINE'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE'
op|')'
newline|'\n'
DECL|variable|DEFINE_string
name|'DEFINE_string'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_string'
op|')'
newline|'\n'
DECL|variable|DEFINE_integer
name|'DEFINE_integer'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_integer'
op|')'
newline|'\n'
DECL|variable|DEFINE_bool
name|'DEFINE_bool'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_bool'
op|')'
newline|'\n'
DECL|variable|DEFINE_boolean
name|'DEFINE_boolean'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_boolean'
op|')'
newline|'\n'
DECL|variable|DEFINE_float
name|'DEFINE_float'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_float'
op|')'
newline|'\n'
DECL|variable|DEFINE_enum
name|'DEFINE_enum'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_enum'
op|')'
newline|'\n'
DECL|variable|DEFINE_list
name|'DEFINE_list'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_list'
op|')'
newline|'\n'
DECL|variable|DEFINE_spaceseplist
name|'DEFINE_spaceseplist'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_spaceseplist'
op|')'
newline|'\n'
DECL|variable|DEFINE_multistring
name|'DEFINE_multistring'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_multistring'
op|')'
newline|'\n'
DECL|variable|DEFINE_multi_int
name|'DEFINE_multi_int'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_multi_int'
op|')'
newline|'\n'
DECL|variable|DEFINE_flag
name|'DEFINE_flag'
op|'='
name|'_wrapper'
op|'('
name|'gflags'
op|'.'
name|'DEFINE_flag'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|HelpFlag
name|'HelpFlag'
op|'='
name|'gflags'
op|'.'
name|'HelpFlag'
newline|'\n'
DECL|variable|HelpshortFlag
name|'HelpshortFlag'
op|'='
name|'gflags'
op|'.'
name|'HelpshortFlag'
newline|'\n'
DECL|variable|HelpXMLFlag
name|'HelpXMLFlag'
op|'='
name|'gflags'
op|'.'
name|'HelpXMLFlag'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|DECLARE
name|'def'
name|'DECLARE'
op|'('
name|'name'
op|','
name|'module_string'
op|','
name|'flag_values'
op|'='
name|'FLAGS'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'module_string'
name|'not'
name|'in'
name|'sys'
op|'.'
name|'modules'
op|':'
newline|'\n'
indent|'        '
name|'__import__'
op|'('
name|'module_string'
op|','
name|'globals'
op|'('
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'name'
name|'not'
name|'in'
name|'flag_values'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'gflags'
op|'.'
name|'UnrecognizedFlag'
op|'('
nl|'\n'
string|'"%s not defined by %s"'
op|'%'
op|'('
name|'name'
op|','
name|'module_string'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_my_ip
dedent|''
dedent|''
name|'def'
name|'_get_my_ip'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the actual ip of the local machine."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'csock'
op|'='
name|'socket'
op|'.'
name|'socket'
op|'('
name|'socket'
op|'.'
name|'AF_INET'
op|','
name|'socket'
op|'.'
name|'SOCK_DGRAM'
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'connect'
op|'('
op|'('
string|"'8.8.8.8'"
op|','
number|'80'
op|')'
op|')'
newline|'\n'
op|'('
name|'addr'
op|','
name|'port'
op|')'
op|'='
name|'csock'
op|'.'
name|'getsockname'
op|'('
op|')'
newline|'\n'
name|'csock'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'return'
name|'addr'
newline|'\n'
dedent|''
name|'except'
name|'socket'
op|'.'
name|'error'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"127.0.0.1"'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# __GLOBAL FLAGS ONLY__'
nl|'\n'
comment|'# Define any app-specific flags in their own files, docs at:'
nl|'\n'
comment|'# http://code.google.com/p/python-gflags/source/browse/trunk/gflags.py#a9'
nl|'\n'
dedent|''
dedent|''
name|'DEFINE_string'
op|'('
string|"'my_ip'"
op|','
name|'_get_my_ip'
op|'('
op|')'
op|','
string|"'host ip address'"
op|')'
newline|'\n'
name|'DEFINE_list'
op|'('
string|"'region_list'"
op|','
nl|'\n'
op|'['
op|']'
op|','
nl|'\n'
string|"'list of region=fqdn pairs separated by commas'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'connection_type'"
op|','
string|"'libvirt'"
op|','
string|"'libvirt, xenapi or fake'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'aws_access_key_id'"
op|','
string|"'admin'"
op|','
string|"'AWS Access ID'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'aws_secret_access_key'"
op|','
string|"'admin'"
op|','
string|"'AWS Access Key'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'glance_port'"
op|','
number|'9292'
op|','
string|"'glance port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'glance_host'"
op|','
string|"'$my_ip'"
op|','
string|"'glance host'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'s3_port'"
op|','
number|'3333'
op|','
string|"'s3 port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'s3_host'"
op|','
string|"'$my_ip'"
op|','
string|"'s3 host (for infrastructure)'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'s3_dmz'"
op|','
string|"'$my_ip'"
op|','
string|"'s3 dmz ip (for instances)'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'compute_topic'"
op|','
string|"'compute'"
op|','
string|"'the topic compute nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'console_topic'"
op|','
string|"'console'"
op|','
nl|'\n'
string|"'the topic console proxy nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'scheduler_topic'"
op|','
string|"'scheduler'"
op|','
nl|'\n'
string|"'the topic scheduler nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'volume_topic'"
op|','
string|"'volume'"
op|','
string|"'the topic volume nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'network_topic'"
op|','
string|"'network'"
op|','
string|"'the topic network nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ajax_console_proxy_topic'"
op|','
string|"'ajax_proxy'"
op|','
nl|'\n'
string|"'the topic ajax proxy nodes listen on'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ajax_console_proxy_url'"
op|','
nl|'\n'
string|"'http://127.0.0.1:8000'"
op|','
nl|'\n'
string|'\'location of ajax console proxy, \\\n               in the form "http://127.0.0.1:8000"\''
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ajax_console_proxy_port'"
op|','
nl|'\n'
number|'8000'
op|','
string|"'port that ajax_console_proxy binds'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'verbose'"
op|','
name|'False'
op|','
string|"'show debug output'"
op|')'
newline|'\n'
name|'DEFINE_boolean'
op|'('
string|"'fake_rabbit'"
op|','
name|'False'
op|','
string|"'use a fake rabbit'"
op|')'
newline|'\n'
name|'DEFINE_bool'
op|'('
string|"'fake_network'"
op|','
name|'False'
op|','
nl|'\n'
string|"'should we use fake network devices and addresses'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_host'"
op|','
string|"'localhost'"
op|','
string|"'rabbit host'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'rabbit_port'"
op|','
number|'5672'
op|','
string|"'rabbit port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_userid'"
op|','
string|"'guest'"
op|','
string|"'rabbit userid'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_password'"
op|','
string|"'guest'"
op|','
string|"'rabbit password'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'rabbit_virtual_host'"
op|','
string|"'/'"
op|','
string|"'rabbit virtual host'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'rabbit_retry_interval'"
op|','
number|'10'
op|','
string|"'rabbit connection retry interval'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'rabbit_max_retries'"
op|','
number|'12'
op|','
string|"'rabbit connection attempts'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'control_exchange'"
op|','
string|"'nova'"
op|','
string|"'the main exchange to connect to'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_host'"
op|','
string|"'$my_ip'"
op|','
string|"'ip of api server'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_dmz_host'"
op|','
string|"'$my_ip'"
op|','
string|"'internal ip of api server'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'ec2_port'"
op|','
number|'8773'
op|','
string|"'cloud controller port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_scheme'"
op|','
string|"'http'"
op|','
string|"'prefix for ec2'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'ec2_path'"
op|','
string|"'/services/Cloud'"
op|','
string|"'suffix for ec2'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'osapi_host'"
op|','
string|"'$my_ip'"
op|','
string|"'ip of api server'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'osapi_scheme'"
op|','
string|"'http'"
op|','
string|"'prefix for openstack'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'osapi_port'"
op|','
number|'8774'
op|','
string|"'OpenStack API port'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'osapi_path'"
op|','
string|"'/v1.0/'"
op|','
string|"'suffix for openstack'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'default_project'"
op|','
string|"'openstack'"
op|','
string|"'default project for openstack'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'default_image'"
op|','
string|"'ami-11111'"
op|','
nl|'\n'
string|"'default image to use, testing only'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'default_instance_type'"
op|','
string|"'m1.small'"
op|','
nl|'\n'
string|"'default instance type to use, testing only'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'null_kernel'"
op|','
string|"'nokernel'"
op|','
nl|'\n'
string|"'kernel image that indicates not to use a kernel,'"
nl|'\n'
string|"' but to use a raw disk image instead'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'vpn_image_id'"
op|','
string|"'ami-cloudpipe'"
op|','
string|"'AMI for cloudpipe vpn server'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'vpn_key_suffix'"
op|','
nl|'\n'
string|"'-vpn'"
op|','
nl|'\n'
string|"'Suffix to add to project name for vpn key and secgroups'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_integer'
op|'('
string|"'auth_token_ttl'"
op|','
number|'3600'
op|','
string|"'Seconds for auth tokens to linger'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'state_path'"
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
string|"'../'"
op|')'
op|','
nl|'\n'
string|'"Top-level directory for maintaining nova\'s state"'
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'sql_connection'"
op|','
nl|'\n'
string|"'sqlite:///$state_path/nova.sqlite'"
op|','
nl|'\n'
string|"'connection string for sql database'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'sql_idle_timeout'"
op|','
nl|'\n'
number|'3600'
op|','
nl|'\n'
string|"'timeout for idle sql database connections'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'sql_max_retries'"
op|','
number|'12'
op|','
string|"'sql connection attempts'"
op|')'
newline|'\n'
name|'DEFINE_integer'
op|'('
string|"'sql_retry_interval'"
op|','
number|'10'
op|','
string|"'sql connection retry interval'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'compute_manager'"
op|','
string|"'nova.compute.manager.ComputeManager'"
op|','
nl|'\n'
string|"'Manager for compute'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'console_manager'"
op|','
string|"'nova.console.manager.ConsoleProxyManager'"
op|','
nl|'\n'
string|"'Manager for console proxy'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'network_manager'"
op|','
string|"'nova.network.manager.VlanManager'"
op|','
nl|'\n'
string|"'Manager for network'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'volume_manager'"
op|','
string|"'nova.volume.manager.VolumeManager'"
op|','
nl|'\n'
string|"'Manager for volume'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'scheduler_manager'"
op|','
string|"'nova.scheduler.manager.SchedulerManager'"
op|','
nl|'\n'
string|"'Manager for scheduler'"
op|')'
newline|'\n'
nl|'\n'
comment|'# The service to use for image search and retrieval'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'image_service'"
op|','
string|"'nova.image.s3.S3ImageService'"
op|','
nl|'\n'
string|"'The service to use for retrieving and searching for images.'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'host'"
op|','
name|'socket'
op|'.'
name|'gethostname'
op|'('
op|')'
op|','
nl|'\n'
string|"'name of this node'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'node_availability_zone'"
op|','
string|"'nova'"
op|','
nl|'\n'
string|"'availability zone of this node'"
op|')'
newline|'\n'
nl|'\n'
name|'DEFINE_string'
op|'('
string|"'zone_name'"
op|','
string|"'nova'"
op|','
string|"'name of this zone'"
op|')'
newline|'\n'
name|'DEFINE_string'
op|'('
string|"'zone_capabilities'"
op|','
string|"'xen, linux'"
op|','
nl|'\n'
string|"'comma-delimited list of tags which represent boolean'"
nl|'\n'
string|"' capabilities of this zone'"
op|')'
newline|'\n'
endmarker|''
end_unit
