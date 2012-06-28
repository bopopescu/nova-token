begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 OpenStack LLC.'
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
name|'import'
name|'paste'
op|'.'
name|'urlmap'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
name|'import'
name|'urllib2'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_quoted_string_re
name|'_quoted_string_re'
op|'='
string|'r\'"[^"\\\\]*(?:\\\\.[^"\\\\]*)*"\''
newline|'\n'
DECL|variable|_option_header_piece_re
name|'_option_header_piece_re'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"r';\\s*([^\\s;=]+|%s)\\s*'"
nl|'\n'
string|"r'(?:=\\s*([^;]+|%s))?\\s*'"
op|'%'
nl|'\n'
op|'('
name|'_quoted_string_re'
op|','
name|'_quoted_string_re'
op|')'
op|')'
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
DECL|function|unquote_header_value
name|'def'
name|'unquote_header_value'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unquotes a header value.\n    This does not use the real unquoting but what browsers are actually\n    using for quoting.\n\n    :param value: the header value to unquote.\n    """'
newline|'\n'
name|'if'
name|'value'
name|'and'
name|'value'
op|'['
number|'0'
op|']'
op|'=='
name|'value'
op|'['
op|'-'
number|'1'
op|']'
op|'=='
string|'\'"\''
op|':'
newline|'\n'
comment|'# this is not the real unquoting, but fixing this so that the'
nl|'\n'
comment|'# RFC is met will result in bugs with internet explorer and'
nl|'\n'
comment|'# probably some other browsers as well.  IE for example is'
nl|'\n'
comment|'# uploading files with "C:\\foo\\bar.txt" as filename'
nl|'\n'
indent|'        '
name|'value'
op|'='
name|'value'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_list_header
dedent|''
name|'def'
name|'parse_list_header'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse lists as described by RFC 2068 Section 2.\n\n    In particular, parse comma-separated lists where the elements of\n    the list may include quoted-strings.  A quoted-string could\n    contain a comma.  A non-quoted string could have quotes in the\n    middle.  Quotes are removed automatically after parsing.\n\n    The return value is a standard :class:`list`:\n\n    >>> parse_list_header(\'token, "quoted value"\')\n    [\'token\', \'quoted value\']\n\n    :param value: a string with a list header.\n    :return: :class:`list`\n    """'
newline|'\n'
name|'result'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'urllib2'
op|'.'
name|'parse_http_list'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'item'
op|'['
op|':'
number|'1'
op|']'
op|'=='
name|'item'
op|'['
op|'-'
number|'1'
op|':'
op|']'
op|'=='
string|'\'"\''
op|':'
newline|'\n'
indent|'            '
name|'item'
op|'='
name|'unquote_header_value'
op|'('
name|'item'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'result'
op|'.'
name|'append'
op|'('
name|'item'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|parse_options_header
dedent|''
name|'def'
name|'parse_options_header'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Parse a ``Content-Type`` like header into a tuple with the content\n    type and the options:\n\n    >>> parse_options_header(\'Content-Type: text/html; mimetype=text/html\')\n    (\'Content-Type:\', {\'mimetype\': \'text/html\'})\n\n    :param value: the header to parse.\n    :return: (str, options)\n    """'
newline|'\n'
DECL|function|_tokenize
name|'def'
name|'_tokenize'
op|'('
name|'string'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'match'
name|'in'
name|'_option_header_piece_re'
op|'.'
name|'finditer'
op|'('
name|'string'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'key'
op|','
name|'value'
op|'='
name|'match'
op|'.'
name|'groups'
op|'('
op|')'
newline|'\n'
name|'key'
op|'='
name|'unquote_header_value'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'value'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'value'
op|'='
name|'unquote_header_value'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'yield'
name|'key'
op|','
name|'value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'value'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"''"
op|','
op|'{'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'parts'
op|'='
name|'_tokenize'
op|'('
string|"';'"
op|'+'
name|'value'
op|')'
newline|'\n'
name|'name'
op|'='
name|'parts'
op|'.'
name|'next'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'extra'
op|'='
name|'dict'
op|'('
name|'parts'
op|')'
newline|'\n'
name|'return'
name|'name'
op|','
name|'extra'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Accept
dedent|''
name|'class'
name|'Accept'
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
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_content_types'
op|'='
op|'['
name|'parse_options_header'
op|'('
name|'v'
op|')'
name|'for'
name|'v'
name|'in'
nl|'\n'
name|'parse_list_header'
op|'('
name|'value'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|member|best_match
dedent|''
name|'def'
name|'best_match'
op|'('
name|'self'
op|','
name|'supported_content_types'
op|')'
op|':'
newline|'\n'
comment|'# FIXME: Should we have a more sophisticated matching algorithm that'
nl|'\n'
comment|'# takes into account the version as well?'
nl|'\n'
indent|'        '
name|'best_quality'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'best_content_type'
op|'='
name|'None'
newline|'\n'
name|'best_params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'best_match'
op|'='
string|"'*/*'"
newline|'\n'
nl|'\n'
name|'for'
name|'content_type'
name|'in'
name|'supported_content_types'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'content_mask'
op|','
name|'params'
name|'in'
name|'self'
op|'.'
name|'_content_types'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'quality'
op|'='
name|'float'
op|'('
name|'params'
op|'.'
name|'get'
op|'('
string|"'q'"
op|','
number|'1'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'quality'
op|'<'
name|'best_quality'
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'elif'
name|'best_quality'
op|'=='
name|'quality'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'best_match'
op|'.'
name|'count'
op|'('
string|"'*'"
op|')'
op|'<='
name|'content_mask'
op|'.'
name|'count'
op|'('
string|"'*'"
op|')'
op|':'
newline|'\n'
indent|'                        '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'self'
op|'.'
name|'_match_mask'
op|'('
name|'content_mask'
op|','
name|'content_type'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'best_quality'
op|'='
name|'quality'
newline|'\n'
name|'best_content_type'
op|'='
name|'content_type'
newline|'\n'
name|'best_params'
op|'='
name|'params'
newline|'\n'
name|'best_match'
op|'='
name|'content_mask'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'best_content_type'
op|','
name|'best_params'
newline|'\n'
nl|'\n'
DECL|member|content_type_params
dedent|''
name|'def'
name|'content_type_params'
op|'('
name|'self'
op|','
name|'best_content_type'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find parameters in Accept header for given content type."""'
newline|'\n'
name|'for'
name|'content_type'
op|','
name|'params'
name|'in'
name|'self'
op|'.'
name|'_content_types'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'best_content_type'
op|'=='
name|'content_type'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'params'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_match_mask
dedent|''
name|'def'
name|'_match_mask'
op|'('
name|'self'
op|','
name|'mask'
op|','
name|'content_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'*'"
name|'not'
name|'in'
name|'mask'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'content_type'
op|'=='
name|'mask'
newline|'\n'
dedent|''
name|'if'
name|'mask'
op|'=='
string|"'*/*'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'mask_major'
op|'='
name|'mask'
op|'['
op|':'
op|'-'
number|'2'
op|']'
newline|'\n'
name|'content_type_major'
op|'='
name|'content_type'
op|'.'
name|'split'
op|'('
string|"'/'"
op|','
number|'1'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'content_type_major'
op|'=='
name|'mask_major'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|urlmap_factory
dedent|''
dedent|''
name|'def'
name|'urlmap_factory'
op|'('
name|'loader'
op|','
name|'global_conf'
op|','
op|'**'
name|'local_conf'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
string|"'not_found_app'"
name|'in'
name|'local_conf'
op|':'
newline|'\n'
indent|'        '
name|'not_found_app'
op|'='
name|'local_conf'
op|'.'
name|'pop'
op|'('
string|"'not_found_app'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'not_found_app'
op|'='
name|'global_conf'
op|'.'
name|'get'
op|'('
string|"'not_found_app'"
op|')'
newline|'\n'
dedent|''
name|'if'
name|'not_found_app'
op|':'
newline|'\n'
indent|'        '
name|'not_found_app'
op|'='
name|'loader'
op|'.'
name|'get_app'
op|'('
name|'not_found_app'
op|','
name|'global_conf'
op|'='
name|'global_conf'
op|')'
newline|'\n'
dedent|''
name|'urlmap'
op|'='
name|'URLMap'
op|'('
name|'not_found_app'
op|'='
name|'not_found_app'
op|')'
newline|'\n'
name|'for'
name|'path'
op|','
name|'app_name'
name|'in'
name|'local_conf'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'path'
op|'='
name|'paste'
op|'.'
name|'urlmap'
op|'.'
name|'parse_path_expression'
op|'('
name|'path'
op|')'
newline|'\n'
name|'app'
op|'='
name|'loader'
op|'.'
name|'get_app'
op|'('
name|'app_name'
op|','
name|'global_conf'
op|'='
name|'global_conf'
op|')'
newline|'\n'
name|'urlmap'
op|'['
name|'path'
op|']'
op|'='
name|'app'
newline|'\n'
dedent|''
name|'return'
name|'urlmap'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|URLMap
dedent|''
name|'class'
name|'URLMap'
op|'('
name|'paste'
op|'.'
name|'urlmap'
op|'.'
name|'URLMap'
op|')'
op|':'
newline|'\n'
DECL|member|_match
indent|'    '
name|'def'
name|'_match'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|','
name|'path_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Find longest match for a given URL path."""'
newline|'\n'
name|'for'
op|'('
name|'domain'
op|','
name|'app_url'
op|')'
op|','
name|'app'
name|'in'
name|'self'
op|'.'
name|'applications'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'domain'
name|'and'
name|'domain'
op|'!='
name|'host'
name|'and'
name|'domain'
op|'!='
name|'host'
op|'+'
string|"':'"
op|'+'
name|'port'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
dedent|''
name|'if'
op|'('
name|'path_info'
op|'=='
name|'app_url'
nl|'\n'
name|'or'
name|'path_info'
op|'.'
name|'startswith'
op|'('
name|'app_url'
op|'+'
string|"'/'"
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'app'
op|','
name|'app_url'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
op|','
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_set_script_name
dedent|''
name|'def'
name|'_set_script_name'
op|'('
name|'self'
op|','
name|'app'
op|','
name|'app_url'
op|')'
op|':'
newline|'\n'
DECL|function|wrap
indent|'        '
name|'def'
name|'wrap'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'environ'
op|'['
string|"'SCRIPT_NAME'"
op|']'
op|'+='
name|'app_url'
newline|'\n'
name|'return'
name|'app'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'wrap'
newline|'\n'
nl|'\n'
DECL|member|_munge_path
dedent|''
name|'def'
name|'_munge_path'
op|'('
name|'self'
op|','
name|'app'
op|','
name|'path_info'
op|','
name|'app_url'
op|')'
op|':'
newline|'\n'
DECL|function|wrap
indent|'        '
name|'def'
name|'wrap'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'environ'
op|'['
string|"'SCRIPT_NAME'"
op|']'
op|'+='
name|'app_url'
newline|'\n'
name|'environ'
op|'['
string|"'PATH_INFO'"
op|']'
op|'='
name|'path_info'
op|'['
name|'len'
op|'('
name|'app_url'
op|')'
op|':'
op|']'
newline|'\n'
name|'return'
name|'app'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'wrap'
newline|'\n'
nl|'\n'
DECL|member|_path_strategy
dedent|''
name|'def'
name|'_path_strategy'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|','
name|'path_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check path suffix for MIME type and path prefix for API version."""'
newline|'\n'
name|'mime_type'
op|'='
name|'app'
op|'='
name|'app_url'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'parts'
op|'='
name|'path_info'
op|'.'
name|'rsplit'
op|'('
string|"'.'"
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'possible_type'
op|'='
string|"'application/'"
op|'+'
name|'parts'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
name|'possible_type'
name|'in'
name|'wsgi'
op|'.'
name|'SUPPORTED_CONTENT_TYPES'
op|':'
newline|'\n'
indent|'                '
name|'mime_type'
op|'='
name|'possible_type'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'parts'
op|'='
name|'path_info'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'possible_app'
op|','
name|'possible_app_url'
op|'='
name|'self'
op|'.'
name|'_match'
op|'('
name|'host'
op|','
name|'port'
op|','
name|'path_info'
op|')'
newline|'\n'
comment|"# Don't use prefix if it ends up matching default"
nl|'\n'
name|'if'
name|'possible_app'
name|'and'
name|'possible_app_url'
op|':'
newline|'\n'
indent|'                '
name|'app_url'
op|'='
name|'possible_app_url'
newline|'\n'
name|'app'
op|'='
name|'self'
op|'.'
name|'_munge_path'
op|'('
name|'possible_app'
op|','
name|'path_info'
op|','
name|'app_url'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'mime_type'
op|','
name|'app'
op|','
name|'app_url'
newline|'\n'
nl|'\n'
DECL|member|_content_type_strategy
dedent|''
name|'def'
name|'_content_type_strategy'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|','
name|'environ'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check Content-Type header for API version."""'
newline|'\n'
name|'app'
op|'='
name|'None'
newline|'\n'
name|'params'
op|'='
name|'parse_options_header'
op|'('
name|'environ'
op|'.'
name|'get'
op|'('
string|"'CONTENT_TYPE'"
op|','
string|"''"
op|')'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
name|'if'
string|"'version'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'app'
op|','
name|'app_url'
op|'='
name|'self'
op|'.'
name|'_match'
op|'('
name|'host'
op|','
name|'port'
op|','
string|"'/v'"
op|'+'
name|'params'
op|'['
string|"'version'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'app'
op|':'
newline|'\n'
indent|'                '
name|'app'
op|'='
name|'self'
op|'.'
name|'_set_script_name'
op|'('
name|'app'
op|','
name|'app_url'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'app'
newline|'\n'
nl|'\n'
DECL|member|_accept_strategy
dedent|''
name|'def'
name|'_accept_strategy'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'port'
op|','
name|'environ'
op|','
name|'supported_content_types'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check Accept header for best matching MIME type and API version."""'
newline|'\n'
name|'accept'
op|'='
name|'Accept'
op|'('
name|'environ'
op|'.'
name|'get'
op|'('
string|"'HTTP_ACCEPT'"
op|','
string|"''"
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'app'
op|'='
name|'None'
newline|'\n'
nl|'\n'
comment|'# Find the best match in the Accept header'
nl|'\n'
name|'mime_type'
op|','
name|'params'
op|'='
name|'accept'
op|'.'
name|'best_match'
op|'('
name|'supported_content_types'
op|')'
newline|'\n'
name|'if'
string|"'version'"
name|'in'
name|'params'
op|':'
newline|'\n'
indent|'            '
name|'app'
op|','
name|'app_url'
op|'='
name|'self'
op|'.'
name|'_match'
op|'('
name|'host'
op|','
name|'port'
op|','
string|"'/v'"
op|'+'
name|'params'
op|'['
string|"'version'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'app'
op|':'
newline|'\n'
indent|'                '
name|'app'
op|'='
name|'self'
op|'.'
name|'_set_script_name'
op|'('
name|'app'
op|','
name|'app_url'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'mime_type'
op|','
name|'app'
newline|'\n'
nl|'\n'
DECL|member|__call__
dedent|''
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'environ'
op|','
name|'start_response'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'host'
op|'='
name|'environ'
op|'.'
name|'get'
op|'('
string|"'HTTP_HOST'"
op|','
name|'environ'
op|'.'
name|'get'
op|'('
string|"'SERVER_NAME'"
op|')'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'if'
string|"':'"
name|'in'
name|'host'
op|':'
newline|'\n'
indent|'            '
name|'host'
op|','
name|'port'
op|'='
name|'host'
op|'.'
name|'split'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'environ'
op|'['
string|"'wsgi.url_scheme'"
op|']'
op|'=='
string|"'http'"
op|':'
newline|'\n'
indent|'                '
name|'port'
op|'='
string|"'80'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'port'
op|'='
string|"'443'"
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'path_info'
op|'='
name|'environ'
op|'['
string|"'PATH_INFO'"
op|']'
newline|'\n'
name|'path_info'
op|'='
name|'self'
op|'.'
name|'normalize_url'
op|'('
name|'path_info'
op|','
name|'False'
op|')'
op|'['
number|'1'
op|']'
newline|'\n'
nl|'\n'
comment|'# The MIME type for the response is determined in one of two ways:'
nl|'\n'
comment|'# 1) URL path suffix (eg /servers/detail.json)'
nl|'\n'
comment|'# 2) Accept header (eg application/json;q=0.8, application/xml;q=0.2)'
nl|'\n'
nl|'\n'
comment|'# The API version is determined in one of three ways:'
nl|'\n'
comment|'# 1) URL path prefix (eg /v1.1/tenant/servers/detail)'
nl|'\n'
comment|'# 2) Content-Type header (eg application/json;version=1.1)'
nl|'\n'
comment|'# 3) Accept header (eg application/json;q=0.8;version=1.1)'
nl|'\n'
nl|'\n'
name|'supported_content_types'
op|'='
name|'list'
op|'('
name|'wsgi'
op|'.'
name|'SUPPORTED_CONTENT_TYPES'
op|')'
newline|'\n'
nl|'\n'
name|'mime_type'
op|','
name|'app'
op|','
name|'app_url'
op|'='
name|'self'
op|'.'
name|'_path_strategy'
op|'('
name|'host'
op|','
name|'port'
op|','
name|'path_info'
op|')'
newline|'\n'
nl|'\n'
comment|'# Accept application/atom+xml for the index query of each API'
nl|'\n'
comment|'# version mount point as well as the root index'
nl|'\n'
name|'if'
op|'('
name|'app_url'
name|'and'
name|'app_url'
op|'+'
string|"'/'"
op|'=='
name|'path_info'
op|')'
name|'or'
name|'path_info'
op|'=='
string|"'/'"
op|':'
newline|'\n'
indent|'            '
name|'supported_content_types'
op|'.'
name|'append'
op|'('
string|"'application/atom+xml'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'app'
op|':'
newline|'\n'
indent|'            '
name|'app'
op|'='
name|'self'
op|'.'
name|'_content_type_strategy'
op|'('
name|'host'
op|','
name|'port'
op|','
name|'environ'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'mime_type'
name|'or'
name|'not'
name|'app'
op|':'
newline|'\n'
indent|'            '
name|'possible_mime_type'
op|','
name|'possible_app'
op|'='
name|'self'
op|'.'
name|'_accept_strategy'
op|'('
nl|'\n'
name|'host'
op|','
name|'port'
op|','
name|'environ'
op|','
name|'supported_content_types'
op|')'
newline|'\n'
name|'if'
name|'possible_mime_type'
name|'and'
name|'not'
name|'mime_type'
op|':'
newline|'\n'
indent|'                '
name|'mime_type'
op|'='
name|'possible_mime_type'
newline|'\n'
dedent|''
name|'if'
name|'possible_app'
name|'and'
name|'not'
name|'app'
op|':'
newline|'\n'
indent|'                '
name|'app'
op|'='
name|'possible_app'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'mime_type'
op|':'
newline|'\n'
indent|'            '
name|'mime_type'
op|'='
string|"'application/json'"
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'app'
op|':'
newline|'\n'
comment|"# Didn't match a particular version, probably matches default"
nl|'\n'
indent|'            '
name|'app'
op|','
name|'app_url'
op|'='
name|'self'
op|'.'
name|'_match'
op|'('
name|'host'
op|','
name|'port'
op|','
name|'path_info'
op|')'
newline|'\n'
name|'if'
name|'app'
op|':'
newline|'\n'
indent|'                '
name|'app'
op|'='
name|'self'
op|'.'
name|'_munge_path'
op|'('
name|'app'
op|','
name|'path_info'
op|','
name|'app_url'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'app'
op|':'
newline|'\n'
indent|'            '
name|'environ'
op|'['
string|"'nova.best_content_type'"
op|']'
op|'='
name|'mime_type'
newline|'\n'
name|'return'
name|'app'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'environ'
op|'['
string|"'paste.urlmap_object'"
op|']'
op|'='
name|'self'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'not_found_application'
op|'('
name|'environ'
op|','
name|'start_response'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
