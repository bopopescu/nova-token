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
string|'"""\nAPIRequest class\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'logging'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
comment|'# TODO(termie): replace minidom with etree'
nl|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
DECL|variable|_log
name|'_log'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"api"'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'setLevel'
op|'('
name|'logging'
op|'.'
name|'DEBUG'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_c2u
name|'_c2u'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_camelcase_to_underscore
name|'def'
name|'_camelcase_to_underscore'
op|'('
name|'str'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_c2u'
op|'.'
name|'sub'
op|'('
string|"r'_\\1'"
op|','
name|'str'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
string|"'_'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_underscore_to_camelcase
dedent|''
name|'def'
name|'_underscore_to_camelcase'
op|'('
name|'str'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
op|'['
name|'x'
op|'['
op|':'
number|'1'
op|']'
op|'.'
name|'upper'
op|'('
op|')'
op|'+'
name|'x'
op|'['
number|'1'
op|':'
op|']'
name|'for'
name|'x'
name|'in'
name|'str'
op|'.'
name|'split'
op|'('
string|"'_'"
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_underscore_to_xmlcase
dedent|''
name|'def'
name|'_underscore_to_xmlcase'
op|'('
name|'str'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'res'
op|'='
name|'_underscore_to_camelcase'
op|'('
name|'str'
op|')'
newline|'\n'
name|'return'
name|'res'
op|'['
op|':'
number|'1'
op|']'
op|'.'
name|'lower'
op|'('
op|')'
op|'+'
name|'res'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
nl|'\n'
DECL|function|_try_convert
dedent|''
name|'def'
name|'_try_convert'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a non-string if possible"""'
newline|'\n'
name|'if'
name|'value'
op|'=='
string|"'None'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'value'
op|'=='
string|"'True'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'value'
op|'=='
string|"'False'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'if'
name|'value'
op|'=='
string|"'0'"
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'valueneg'
op|'='
name|'value'
op|'['
number|'1'
op|':'
op|']'
name|'if'
name|'value'
op|'['
number|'0'
op|']'
op|'=='
string|"'-'"
name|'else'
name|'value'
newline|'\n'
name|'if'
name|'valueneg'
op|'['
number|'0'
op|']'
op|'=='
string|"'0'"
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'valueneg'
op|'['
number|'1'
op|']'
name|'in'
string|"'xX'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'value'
op|','
number|'16'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'valueneg'
op|'['
number|'1'
op|']'
name|'in'
string|"'bB'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'value'
op|','
number|'2'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'int'
op|'('
name|'value'
op|','
number|'8'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'float'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'complex'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
newline|'\n'
nl|'\n'
DECL|class|APIRequest
dedent|''
dedent|''
name|'class'
name|'APIRequest'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'controller'
op|','
name|'action'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'controller'
op|'='
name|'controller'
newline|'\n'
name|'self'
op|'.'
name|'action'
op|'='
name|'action'
newline|'\n'
nl|'\n'
DECL|member|send
dedent|''
name|'def'
name|'send'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'method'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
nl|'\n'
name|'_camelcase_to_underscore'
op|'('
name|'self'
op|'.'
name|'action'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'_error'
op|'='
op|'('
string|"'Unsupported API request: controller = %s,'"
nl|'\n'
string|"'action = %s'"
op|')'
op|'%'
op|'('
name|'self'
op|'.'
name|'controller'
op|','
name|'self'
op|'.'
name|'action'
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'warning'
op|'('
name|'_error'
op|')'
newline|'\n'
comment|'# TODO: Raise custom exception, trap in apiserver,'
nl|'\n'
comment|'#       and reraise as 400 error.'
nl|'\n'
name|'raise'
name|'Exception'
op|'('
name|'_error'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'kwargs'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'parts'
op|'='
name|'key'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
newline|'\n'
name|'key'
op|'='
name|'_camelcase_to_underscore'
op|'('
name|'parts'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'str'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'value'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): Automatically convert strings back'
nl|'\n'
comment|'#             into their respective values'
nl|'\n'
indent|'                '
name|'value'
op|'='
name|'_try_convert'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'='
name|'args'
op|'.'
name|'get'
op|'('
name|'key'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'d'
op|'['
name|'parts'
op|'['
number|'1'
op|']'
op|']'
op|'='
name|'value'
newline|'\n'
name|'value'
op|'='
name|'d'
newline|'\n'
dedent|''
name|'args'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'key'
name|'in'
name|'args'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): Turn numeric dict keys into lists'
nl|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'args'
op|'['
name|'key'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'args'
op|'['
name|'key'
op|']'
op|'!='
op|'{'
op|'}'
name|'and'
name|'args'
op|'['
name|'key'
op|']'
op|'.'
name|'keys'
op|'('
op|')'
op|'['
number|'0'
op|']'
op|'.'
name|'isdigit'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'s'
op|'='
name|'args'
op|'['
name|'key'
op|']'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
name|'s'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'args'
op|'['
name|'key'
op|']'
op|'='
op|'['
name|'v'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'s'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'result'
op|'='
name|'method'
op|'('
name|'context'
op|','
op|'**'
name|'args'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_render_response'
op|'('
name|'result'
op|','
name|'context'
op|'.'
name|'request_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_render_response
dedent|''
name|'def'
name|'_render_response'
op|'('
name|'self'
op|','
name|'response_data'
op|','
name|'request_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'response_el'
op|'='
name|'xml'
op|'.'
name|'createElement'
op|'('
name|'self'
op|'.'
name|'action'
op|'+'
string|"'Response'"
op|')'
newline|'\n'
name|'response_el'
op|'.'
name|'setAttribute'
op|'('
string|"'xmlns'"
op|','
nl|'\n'
string|"'http://ec2.amazonaws.com/doc/2009-11-30/'"
op|')'
newline|'\n'
name|'request_id_el'
op|'='
name|'xml'
op|'.'
name|'createElement'
op|'('
string|"'requestId'"
op|')'
newline|'\n'
name|'request_id_el'
op|'.'
name|'appendChild'
op|'('
name|'xml'
op|'.'
name|'createTextNode'
op|'('
name|'request_id'
op|')'
op|')'
newline|'\n'
name|'response_el'
op|'.'
name|'appendChild'
op|'('
name|'request_id_el'
op|')'
newline|'\n'
name|'if'
op|'('
name|'response_data'
op|'=='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_render_dict'
op|'('
name|'xml'
op|','
name|'response_el'
op|','
op|'{'
string|"'return'"
op|':'
string|"'true'"
op|'}'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_render_dict'
op|'('
name|'xml'
op|','
name|'response_el'
op|','
name|'response_data'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'xml'
op|'.'
name|'appendChild'
op|'('
name|'response_el'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'xml'
op|'.'
name|'toxml'
op|'('
op|')'
newline|'\n'
name|'xml'
op|'.'
name|'unlink'
op|'('
op|')'
newline|'\n'
name|'_log'
op|'.'
name|'debug'
op|'('
name|'response'
op|')'
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|_render_dict
dedent|''
name|'def'
name|'_render_dict'
op|'('
name|'self'
op|','
name|'xml'
op|','
name|'el'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'key'
name|'in'
name|'data'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'val'
op|'='
name|'data'
op|'['
name|'key'
op|']'
newline|'\n'
name|'el'
op|'.'
name|'appendChild'
op|'('
name|'self'
op|'.'
name|'_render_data'
op|'('
name|'xml'
op|','
name|'key'
op|','
name|'val'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
op|':'
newline|'\n'
indent|'            '
name|'_log'
op|'.'
name|'debug'
op|'('
name|'data'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|_render_data
dedent|''
dedent|''
name|'def'
name|'_render_data'
op|'('
name|'self'
op|','
name|'xml'
op|','
name|'el_name'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'el_name'
op|'='
name|'_underscore_to_xmlcase'
op|'('
name|'el_name'
op|')'
newline|'\n'
name|'data_el'
op|'='
name|'xml'
op|'.'
name|'createElement'
op|'('
name|'el_name'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'item'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'data_el'
op|'.'
name|'appendChild'
op|'('
name|'self'
op|'.'
name|'_render_data'
op|'('
name|'xml'
op|','
string|"'item'"
op|','
name|'item'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_render_dict'
op|'('
name|'xml'
op|','
name|'data_el'
op|','
name|'data'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'hasattr'
op|'('
name|'data'
op|','
string|"'__dict__'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_render_dict'
op|'('
name|'xml'
op|','
name|'data_el'
op|','
name|'data'
op|'.'
name|'__dict__'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'bool'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'data_el'
op|'.'
name|'appendChild'
op|'('
name|'xml'
op|'.'
name|'createTextNode'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'data'
op|'!='
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'data_el'
op|'.'
name|'appendChild'
op|'('
name|'xml'
op|'.'
name|'createTextNode'
op|'('
name|'str'
op|'('
name|'data'
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'data_el'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
