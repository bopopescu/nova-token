begin_unit
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
name|'datetime'
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
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
name|'encodeutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
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
DECL|function|_underscore_to_camelcase
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
nl|'\n'
DECL|function|_database_to_isoformat
dedent|''
name|'def'
name|'_database_to_isoformat'
op|'('
name|'datetimeobj'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a xs:dateTime parsable string from datatime."""'
newline|'\n'
name|'return'
name|'datetimeobj'
op|'.'
name|'strftime'
op|'('
string|'"%Y-%m-%dT%H:%M:%S.%f"'
op|')'
op|'['
op|':'
op|'-'
number|'3'
op|']'
op|'+'
string|"'Z'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|APIRequest
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
op|','
name|'version'
op|','
name|'args'
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
name|'self'
op|'.'
name|'version'
op|'='
name|'version'
newline|'\n'
name|'self'
op|'.'
name|'args'
op|'='
name|'args'
newline|'\n'
nl|'\n'
DECL|member|invoke
dedent|''
name|'def'
name|'invoke'
op|'('
name|'self'
op|','
name|'context'
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
name|'ec2utils'
op|'.'
name|'camelcase_to_underscore'
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
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Unsupported API request: controller = '"
nl|'\n'
string|"'%(controller)s, action = %(action)s'"
op|','
nl|'\n'
op|'{'
string|"'controller'"
op|':'
name|'self'
op|'.'
name|'controller'
op|','
nl|'\n'
string|"'action'"
op|':'
name|'self'
op|'.'
name|'action'
op|'}'
op|')'
newline|'\n'
comment|'# TODO(gundlach): Raise custom exception, trap in apiserver,'
nl|'\n'
comment|'#       and reraise as 400 error.'
nl|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidRequest'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'args'
op|'='
name|'ec2utils'
op|'.'
name|'dict_from_dotted_str'
op|'('
name|'self'
op|'.'
name|'args'
op|'.'
name|'items'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
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
string|"'http://ec2.amazonaws.com/doc/%s/'"
op|'%'
name|'self'
op|'.'
name|'version'
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
name|'response_data'
name|'is'
name|'True'
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
name|'root'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'response'
op|')'
newline|'\n'
name|'response'
op|'='
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'root'
op|','
name|'pretty_print'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'.'
name|'unlink'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|"# Don't write private key to log"
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'action'
op|'!='
string|'"CreateKeyPair"'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'response'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"CreateKeyPair: Return Private Key"'
op|')'
newline|'\n'
nl|'\n'
dedent|''
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
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
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
name|'isinstance'
op|'('
name|'data'
op|','
name|'datetime'
op|'.'
name|'datetime'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'data_el'
op|'.'
name|'appendChild'
op|'('
nl|'\n'
name|'xml'
op|'.'
name|'createTextNode'
op|'('
name|'_database_to_isoformat'
op|'('
name|'data'
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'data'
name|'is'
name|'not'
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
nl|'\n'
name|'encodeutils'
op|'.'
name|'safe_encode'
op|'('
name|'six'
op|'.'
name|'text_type'
op|'('
name|'data'
op|')'
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
