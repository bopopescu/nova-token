begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 OpenStack LLC.'
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
name|'re'
newline|'\n'
name|'import'
name|'urlparse'
newline|'\n'
name|'from'
name|'xml'
op|'.'
name|'dom'
name|'import'
name|'minidom'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'wsgi'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.api.openstack.common'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|XML_NS_V10
name|'XML_NS_V10'
op|'='
string|"'http://docs.rackspacecloud.com/servers/api/v1.0'"
newline|'\n'
DECL|variable|XML_NS_V11
name|'XML_NS_V11'
op|'='
string|"'http://docs.openstack.org/compute/api/v1.1'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_pagination_params
name|'def'
name|'get_pagination_params'
op|'('
name|'request'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return marker, limit tuple from request.\n\n    :param request: `wsgi.Request` possibly containing \'marker\' and \'limit\'\n                    GET variables. \'marker\' is the id of the last element\n                    the client has seen, and \'limit\' is the maximum number\n                    of items to return. If \'limit\' is not specified, 0, or\n                    > max_limit, we default to max_limit. Negative values\n                    for either marker or limit will cause\n                    exc.HTTPBadRequest() exceptions to be raised.\n\n    """'
newline|'\n'
name|'params'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'param'
name|'in'
op|'['
string|"'marker'"
op|','
string|"'limit'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'param'
name|'in'
name|'request'
op|'.'
name|'GET'
op|':'
newline|'\n'
indent|'            '
name|'continue'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
name|'param'
op|']'
op|'='
name|'int'
op|'('
name|'request'
op|'.'
name|'GET'
op|'['
name|'param'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'%s param must be an integer'"
op|')'
op|'%'
name|'param'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'params'
op|'['
name|'param'
op|']'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'%s param must be positive'"
op|')'
op|'%'
name|'param'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'params'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|limited
dedent|''
name|'def'
name|'limited'
op|'('
name|'items'
op|','
name|'request'
op|','
name|'max_limit'
op|'='
name|'FLAGS'
op|'.'
name|'osapi_max_limit'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Return a slice of items according to requested offset and limit.\n\n    @param items: A sliceable entity\n    @param request: `wsgi.Request` possibly containing \'offset\' and \'limit\'\n                    GET variables. \'offset\' is where to start in the list,\n                    and \'limit\' is the maximum number of items to return. If\n                    \'limit\' is not specified, 0, or > max_limit, we default\n                    to max_limit. Negative values for either offset or limit\n                    will cause exc.HTTPBadRequest() exceptions to be raised.\n    @kwarg max_limit: The maximum number of items to return from \'items\'\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'offset'
op|'='
name|'int'
op|'('
name|'request'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'offset'"
op|','
number|'0'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'offset param must be an integer'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'limit'
op|'='
name|'int'
op|'('
name|'request'
op|'.'
name|'GET'
op|'.'
name|'get'
op|'('
string|"'limit'"
op|','
name|'max_limit'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'limit param must be an integer'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'limit'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'limit param must be positive'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'offset'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'offset param must be positive'"
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'limit'
op|'='
name|'min'
op|'('
name|'max_limit'
op|','
name|'limit'
name|'or'
name|'max_limit'
op|')'
newline|'\n'
name|'range_end'
op|'='
name|'offset'
op|'+'
name|'limit'
newline|'\n'
name|'return'
name|'items'
op|'['
name|'offset'
op|':'
name|'range_end'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|limited_by_marker
dedent|''
name|'def'
name|'limited_by_marker'
op|'('
name|'items'
op|','
name|'request'
op|','
name|'max_limit'
op|'='
name|'FLAGS'
op|'.'
name|'osapi_max_limit'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a slice of items according to the requested marker and limit."""'
newline|'\n'
name|'params'
op|'='
name|'get_pagination_params'
op|'('
name|'request'
op|')'
newline|'\n'
nl|'\n'
name|'limit'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'limit'"
op|','
name|'max_limit'
op|')'
newline|'\n'
name|'marker'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'marker'"
op|')'
newline|'\n'
nl|'\n'
name|'limit'
op|'='
name|'min'
op|'('
name|'max_limit'
op|','
name|'limit'
op|')'
newline|'\n'
name|'start_index'
op|'='
number|'0'
newline|'\n'
name|'if'
name|'marker'
op|':'
newline|'\n'
indent|'        '
name|'start_index'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'for'
name|'i'
op|','
name|'item'
name|'in'
name|'enumerate'
op|'('
name|'items'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|'['
string|"'id'"
op|']'
op|'=='
name|'marker'
op|':'
newline|'\n'
indent|'                '
name|'start_index'
op|'='
name|'i'
op|'+'
number|'1'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'start_index'
op|'<'
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|"'marker [%s] not found'"
op|')'
op|'%'
name|'marker'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPBadRequest'
op|'('
name|'explanation'
op|'='
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'range_end'
op|'='
name|'start_index'
op|'+'
name|'limit'
newline|'\n'
name|'return'
name|'items'
op|'['
name|'start_index'
op|':'
name|'range_end'
op|']'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_id_from_href
dedent|''
name|'def'
name|'get_id_from_href'
op|'('
name|'href'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return the id portion of a url as an int.\n\n    Given: \'http://www.foo.com/bar/123?q=4\'\n    Returns: 123\n\n    In order to support local hrefs, the href argument can be just an id:\n    Given: \'123\'\n    Returns: 123\n\n    """'
newline|'\n'
name|'if'
name|'re'
op|'.'
name|'match'
op|'('
string|"r'\\d+$'"
op|','
name|'str'
op|'('
name|'href'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'href'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'urlparse'
op|'.'
name|'urlsplit'
op|'('
name|'href'
op|')'
op|'.'
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|','
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Error extracting id from href: %s"'
op|')'
op|'%'
name|'href'
op|')'
newline|'\n'
name|'raise'
name|'ValueError'
op|'('
name|'_'
op|'('
string|"'could not parse id from href'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|remove_version_from_href
dedent|''
dedent|''
name|'def'
name|'remove_version_from_href'
op|'('
name|'href'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Removes the first api version from the href.\n\n    Given: \'http://www.nova.com/v1.1/123\'\n    Returns: \'http://www.nova.com/123\'\n\n    Given: \'http://www.nova.com/v1.1\'\n    Returns: \'http://www.nova.com\'\n\n    """'
newline|'\n'
name|'parsed_url'
op|'='
name|'urlparse'
op|'.'
name|'urlsplit'
op|'('
name|'href'
op|')'
newline|'\n'
name|'new_path'
op|'='
name|'re'
op|'.'
name|'sub'
op|'('
string|"r'^/v[0-9]+\\.[0-9]+(/|$)'"
op|','
string|"r'\\1'"
op|','
name|'parsed_url'
op|'.'
name|'path'
op|','
name|'count'
op|'='
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'new_path'
op|'=='
name|'parsed_url'
op|'.'
name|'path'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|"'href %s does not contain version'"
op|')'
op|'%'
name|'href'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'ValueError'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'parsed_url'
op|'='
name|'list'
op|'('
name|'parsed_url'
op|')'
newline|'\n'
name|'parsed_url'
op|'['
number|'2'
op|']'
op|'='
name|'new_path'
newline|'\n'
name|'return'
name|'urlparse'
op|'.'
name|'urlunsplit'
op|'('
name|'parsed_url'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_version_from_href
dedent|''
name|'def'
name|'get_version_from_href'
op|'('
name|'href'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns the api version in the href.\n\n    Returns the api version in the href.\n    If no version is found, 1.0 is returned\n\n    Given: \'http://www.nova.com/123\'\n    Returns: \'1.0\'\n\n    Given: \'http://www.nova.com/v1.1\'\n    Returns: \'1.1\'\n\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'#finds the first instance that matches /v#.#/'
nl|'\n'
indent|'        '
name|'version'
op|'='
name|'re'
op|'.'
name|'findall'
op|'('
string|"r'[/][v][0-9]+\\.[0-9]+[/]'"
op|','
name|'href'
op|')'
newline|'\n'
comment|'#if no version was found, try finding /v#.# at the end of the string'
nl|'\n'
name|'if'
name|'not'
name|'version'
op|':'
newline|'\n'
indent|'            '
name|'version'
op|'='
name|'re'
op|'.'
name|'findall'
op|'('
string|"r'[/][v][0-9]+\\.[0-9]+$'"
op|','
name|'href'
op|')'
newline|'\n'
dedent|''
name|'version'
op|'='
name|'re'
op|'.'
name|'findall'
op|'('
string|"r'[0-9]+\\.[0-9]'"
op|','
name|'version'
op|'['
number|'0'
op|']'
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'except'
name|'IndexError'
op|':'
newline|'\n'
indent|'        '
name|'version'
op|'='
string|"'1.0'"
newline|'\n'
dedent|''
name|'return'
name|'version'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataXMLDeserializer
dedent|''
name|'class'
name|'MetadataXMLDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'MetadataXMLDeserializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_extract_metadata_container
indent|'    '
name|'def'
name|'_extract_metadata_container'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'datastring'
op|')'
newline|'\n'
name|'metadata_node'
op|'='
name|'self'
op|'.'
name|'find_first_child_named'
op|'('
name|'dom'
op|','
string|'"metadata"'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'metadata_node'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'metadata'"
op|':'
name|'metadata'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_extract_metadata_container'
op|'('
name|'datastring'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_all
dedent|''
name|'def'
name|'update_all'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_extract_metadata_container'
op|'('
name|'datastring'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'datastring'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dom'
op|'='
name|'minidom'
op|'.'
name|'parseString'
op|'('
name|'datastring'
op|')'
newline|'\n'
name|'metadata_item'
op|'='
name|'self'
op|'.'
name|'extract_metadata'
op|'('
name|'dom'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'body'"
op|':'
op|'{'
string|"'meta'"
op|':'
name|'metadata_item'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataHeadersSerializer
dedent|''
dedent|''
name|'class'
name|'MetadataHeadersSerializer'
op|'('
name|'wsgi'
op|'.'
name|'ResponseHeadersSerializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|delete
indent|'    '
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'response'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'.'
name|'status_int'
op|'='
number|'204'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataXMLSerializer
dedent|''
dedent|''
name|'class'
name|'MetadataXMLSerializer'
op|'('
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
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
name|'xmlns'
op|'='
name|'wsgi'
op|'.'
name|'XMLNS_V11'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'MetadataXMLSerializer'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'xmlns'
op|'='
name|'xmlns'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_meta_item_to_xml
dedent|''
name|'def'
name|'_meta_item_to_xml'
op|'('
name|'self'
op|','
name|'doc'
op|','
name|'key'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'node'
op|'='
name|'doc'
op|'.'
name|'createElement'
op|'('
string|"'meta'"
op|')'
newline|'\n'
name|'doc'
op|'.'
name|'appendChild'
op|'('
name|'node'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'setAttribute'
op|'('
string|"'key'"
op|','
string|"'%s'"
op|'%'
name|'key'
op|')'
newline|'\n'
name|'text'
op|'='
name|'doc'
op|'.'
name|'createTextNode'
op|'('
string|"'%s'"
op|'%'
name|'value'
op|')'
newline|'\n'
name|'node'
op|'.'
name|'appendChild'
op|'('
name|'text'
op|')'
newline|'\n'
name|'return'
name|'node'
newline|'\n'
nl|'\n'
DECL|member|meta_list_to_xml
dedent|''
name|'def'
name|'meta_list_to_xml'
op|'('
name|'self'
op|','
name|'xml_doc'
op|','
name|'meta_items'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'container_node'
op|'='
name|'xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'metadata'"
op|')'
newline|'\n'
name|'for'
op|'('
name|'key'
op|','
name|'value'
op|')'
name|'in'
name|'meta_items'
op|':'
newline|'\n'
indent|'            '
name|'item_node'
op|'='
name|'self'
op|'.'
name|'_meta_item_to_xml'
op|'('
name|'xml_doc'
op|','
name|'key'
op|','
name|'value'
op|')'
newline|'\n'
name|'container_node'
op|'.'
name|'appendChild'
op|'('
name|'item_node'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'container_node'
newline|'\n'
nl|'\n'
DECL|member|_meta_list_to_xml_string
dedent|''
name|'def'
name|'_meta_list_to_xml_string'
op|'('
name|'self'
op|','
name|'metadata_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml_doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'items'
op|'='
name|'metadata_dict'
op|'['
string|"'metadata'"
op|']'
op|'.'
name|'items'
op|'('
op|')'
newline|'\n'
name|'container_node'
op|'='
name|'self'
op|'.'
name|'meta_list_to_xml'
op|'('
name|'xml_doc'
op|','
name|'items'
op|')'
newline|'\n'
name|'xml_doc'
op|'.'
name|'appendChild'
op|'('
name|'container_node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_xmlns'
op|'('
name|'container_node'
op|')'
newline|'\n'
name|'return'
name|'xml_doc'
op|'.'
name|'toprettyxml'
op|'('
name|'indent'
op|'='
string|"'    '"
op|','
name|'encoding'
op|'='
string|"'UTF-8'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'metadata_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_meta_list_to_xml_string'
op|'('
name|'metadata_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'metadata_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_meta_list_to_xml_string'
op|'('
name|'metadata_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_all
dedent|''
name|'def'
name|'update_all'
op|'('
name|'self'
op|','
name|'metadata_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_meta_list_to_xml_string'
op|'('
name|'metadata_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_meta_item_to_xml_string
dedent|''
name|'def'
name|'_meta_item_to_xml_string'
op|'('
name|'self'
op|','
name|'meta_item_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'xml_doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'item_key'
op|','
name|'item_value'
op|'='
name|'meta_item_dict'
op|'.'
name|'items'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'item_node'
op|'='
name|'self'
op|'.'
name|'_meta_item_to_xml'
op|'('
name|'xml_doc'
op|','
name|'item_key'
op|','
name|'item_value'
op|')'
newline|'\n'
name|'xml_doc'
op|'.'
name|'appendChild'
op|'('
name|'item_node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_add_xmlns'
op|'('
name|'item_node'
op|')'
newline|'\n'
name|'return'
name|'xml_doc'
op|'.'
name|'toprettyxml'
op|'('
name|'indent'
op|'='
string|"'    '"
op|','
name|'encoding'
op|'='
string|"'UTF-8'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|show
dedent|''
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'meta_item_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_meta_item_to_xml_string'
op|'('
name|'meta_item_dict'
op|'['
string|"'meta'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'meta_item_dict'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'_meta_item_to_xml_string'
op|'('
name|'meta_item_dict'
op|'['
string|"'meta'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|default
dedent|''
name|'def'
name|'default'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"''"
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
