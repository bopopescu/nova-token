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
name|'from'
name|'datetime'
name|'import'
name|'datetime'
newline|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
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
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'versions'
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
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|VERSIONS
name|'VERSIONS'
op|'='
op|'{'
nl|'\n'
string|'"v1.0"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v1.0"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"DEPRECATED"'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-01-21T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/pdf"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://docs.rackspacecloud.com/"'
nl|'\n'
string|'"servers/api/v1.0/cs-devguide-20110125.pdf"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.sun.wadl+xml"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://docs.rackspacecloud.com/"'
nl|'\n'
string|'"servers/api/v1.0/application.wadl"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/xml"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute-v1.0+xml"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute-v1.0+json"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|'"v1.1"'
op|':'
op|'{'
nl|'\n'
string|'"id"'
op|':'
string|'"v1.1"'
op|','
nl|'\n'
string|'"status"'
op|':'
string|'"CURRENT"'
op|','
nl|'\n'
string|'"updated"'
op|':'
string|'"2011-01-21T11:33:21Z"'
op|','
nl|'\n'
string|'"links"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/pdf"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://docs.rackspacecloud.com/"'
nl|'\n'
string|'"servers/api/v1.1/cs-devguide-20110125.pdf"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"rel"'
op|':'
string|'"describedby"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.sun.wadl+xml"'
op|','
nl|'\n'
string|'"href"'
op|':'
string|'"http://docs.rackspacecloud.com/"'
nl|'\n'
string|'"servers/api/v1.1/application.wadl"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|']'
op|','
nl|'\n'
string|'"media-types"'
op|':'
op|'['
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/xml"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute-v1.1+xml"'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'{'
nl|'\n'
string|'"base"'
op|':'
string|'"application/json"'
op|','
nl|'\n'
string|'"type"'
op|':'
string|'"application/vnd.openstack.compute-v1.1+json"'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|']'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Versions
name|'class'
name|'Versions'
op|'('
name|'wsgi'
op|'.'
name|'Resource'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'metadata'
op|'='
op|'{'
nl|'\n'
string|'"attributes"'
op|':'
op|'{'
nl|'\n'
string|'"version"'
op|':'
op|'['
string|'"status"'
op|','
string|'"id"'
op|']'
op|','
nl|'\n'
string|'"link"'
op|':'
op|'['
string|'"rel"'
op|','
string|'"href"'
op|']'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'headers_serializer'
op|'='
name|'VersionsHeadersSerializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'body_serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/atom+xml'"
op|':'
name|'VersionsAtomSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|')'
op|','
nl|'\n'
string|"'application/xml'"
op|':'
name|'VersionsXMLSerializer'
op|'('
name|'metadata'
op|'='
name|'metadata'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
nl|'\n'
name|'body_serializers'
op|'='
name|'body_serializers'
op|','
nl|'\n'
name|'headers_serializer'
op|'='
name|'headers_serializer'
op|')'
newline|'\n'
nl|'\n'
name|'supported_content_types'
op|'='
op|'('
string|"'application/json'"
op|','
nl|'\n'
string|"'application/xml'"
op|','
nl|'\n'
string|"'application/atom+xml'"
op|')'
newline|'\n'
name|'deserializer'
op|'='
name|'VersionsRequestDeserializer'
op|'('
nl|'\n'
name|'supported_content_types'
op|'='
name|'supported_content_types'
op|')'
newline|'\n'
nl|'\n'
name|'wsgi'
op|'.'
name|'Resource'
op|'.'
name|'__init__'
op|'('
name|'self'
op|','
name|'None'
op|','
name|'serializer'
op|'='
name|'serializer'
op|','
nl|'\n'
name|'deserializer'
op|'='
name|'deserializer'
op|')'
newline|'\n'
nl|'\n'
DECL|member|dispatch
dedent|''
name|'def'
name|'dispatch'
op|'('
name|'self'
op|','
name|'request'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Respond to a request for all OpenStack API versions."""'
newline|'\n'
name|'builder'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'versions'
op|'.'
name|'get_view_builder'
op|'('
name|'request'
op|')'
newline|'\n'
name|'if'
name|'request'
op|'.'
name|'path'
op|'=='
string|"'/'"
op|':'
newline|'\n'
comment|'# List Versions'
nl|'\n'
indent|'            '
name|'return'
name|'builder'
op|'.'
name|'build_versions'
op|'('
name|'VERSIONS'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# Versions Multiple Choice'
nl|'\n'
indent|'            '
name|'return'
name|'builder'
op|'.'
name|'build_choices'
op|'('
name|'VERSIONS'
op|','
name|'request'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionV10
dedent|''
dedent|''
dedent|''
name|'class'
name|'VersionV10'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|show
indent|'    '
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'builder'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'versions'
op|'.'
name|'get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'return'
name|'builder'
op|'.'
name|'build_version'
op|'('
name|'VERSIONS'
op|'['
string|"'v1.0'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionV11
dedent|''
dedent|''
name|'class'
name|'VersionV11'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|show
indent|'    '
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'builder'
op|'='
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'views'
op|'.'
name|'versions'
op|'.'
name|'get_view_builder'
op|'('
name|'req'
op|')'
newline|'\n'
name|'return'
name|'builder'
op|'.'
name|'build_version'
op|'('
name|'VERSIONS'
op|'['
string|"'v1.1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsRequestDeserializer
dedent|''
dedent|''
name|'class'
name|'VersionsRequestDeserializer'
op|'('
name|'wsgi'
op|'.'
name|'RequestDeserializer'
op|')'
op|':'
newline|'\n'
DECL|member|get_expected_content_type
indent|'    '
name|'def'
name|'get_expected_content_type'
op|'('
name|'self'
op|','
name|'request'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'supported_content_types'
op|'='
name|'list'
op|'('
name|'self'
op|'.'
name|'supported_content_types'
op|')'
newline|'\n'
name|'if'
name|'request'
op|'.'
name|'path'
op|'!='
string|"'/'"
op|':'
newline|'\n'
comment|'# Remove atom+xml accept type for 300 responses'
nl|'\n'
indent|'            '
name|'if'
string|"'application/atom+xml'"
name|'in'
name|'supported_content_types'
op|':'
newline|'\n'
indent|'                '
name|'supported_content_types'
op|'.'
name|'remove'
op|'('
string|"'application/atom+xml'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'request'
op|'.'
name|'best_match_content_type'
op|'('
name|'supported_content_types'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_action_args
dedent|''
name|'def'
name|'get_action_args'
op|'('
name|'self'
op|','
name|'request_environment'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Parse dictionary created by routes library."""'
newline|'\n'
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'request_environment'
op|'['
string|"'PATH_INFO'"
op|']'
op|'=='
string|"'/'"
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'action'"
op|']'
op|'='
string|"'index'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'['
string|"'action'"
op|']'
op|'='
string|"'multi'"
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'args'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsXMLSerializer
dedent|''
dedent|''
name|'class'
name|'VersionsXMLSerializer'
op|'('
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|_populate_version
indent|'    '
name|'def'
name|'_populate_version'
op|'('
name|'self'
op|','
name|'version_node'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'version_node'
op|'.'
name|'set'
op|'('
string|"'id'"
op|','
name|'version'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'version_node'
op|'.'
name|'set'
op|'('
string|"'status'"
op|','
name|'version'
op|'['
string|"'status'"
op|']'
op|')'
newline|'\n'
name|'if'
string|"'updated'"
name|'in'
name|'version'
op|':'
newline|'\n'
indent|'            '
name|'version_node'
op|'.'
name|'set'
op|'('
string|"'updated'"
op|','
name|'version'
op|'['
string|"'updated'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
string|"'media-types'"
name|'in'
name|'version'
op|':'
newline|'\n'
indent|'            '
name|'media_types'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'version_node'
op|','
string|"'media-types'"
op|')'
newline|'\n'
name|'for'
name|'mtype'
name|'in'
name|'version'
op|'['
string|"'media-types'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'elem'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'media_types'
op|','
string|"'media-type'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'base'"
op|','
name|'mtype'
op|'['
string|"'base'"
op|']'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'type'"
op|','
name|'mtype'
op|'['
string|"'type'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'for'
name|'link'
name|'in'
name|'version'
op|'.'
name|'get'
op|'('
string|"'links'"
op|','
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'elem'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'version_node'
op|','
nl|'\n'
string|"'{%s}link'"
op|'%'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'rel'"
op|','
name|'link'
op|'['
string|"'rel'"
op|']'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'href'"
op|','
name|'link'
op|'['
string|"'href'"
op|']'
op|')'
newline|'\n'
name|'if'
string|"'type'"
name|'in'
name|'link'
op|':'
newline|'\n'
indent|'                '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'type'"
op|','
name|'link'
op|'['
string|"'type'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|NSMAP
dedent|''
dedent|''
dedent|''
name|'NSMAP'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_V11'
op|','
string|"'atom'"
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'versions'"
op|','
name|'nsmap'
op|'='
name|'self'
op|'.'
name|'NSMAP'
op|')'
newline|'\n'
name|'for'
name|'version'
name|'in'
name|'data'
op|'['
string|"'versions'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'version_elem'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'root'
op|','
string|"'version'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_populate_version'
op|'('
name|'version_elem'
op|','
name|'version'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'root'
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
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'version'"
op|','
name|'nsmap'
op|'='
name|'self'
op|'.'
name|'NSMAP'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_populate_version'
op|'('
name|'root'
op|','
name|'data'
op|'['
string|"'version'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'root'
op|','
name|'encoding'
op|'='
string|"'UTF-8'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|multi
dedent|''
name|'def'
name|'multi'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'choices'"
op|','
name|'nsmap'
op|'='
name|'self'
op|'.'
name|'NSMAP'
op|')'
newline|'\n'
name|'for'
name|'version'
name|'in'
name|'data'
op|'['
string|"'choices'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'version_elem'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'root'
op|','
string|"'version'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_populate_version'
op|'('
name|'version_elem'
op|','
name|'version'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'root'
op|','
name|'encoding'
op|'='
string|"'UTF-8'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsAtomSerializer
dedent|''
dedent|''
name|'class'
name|'VersionsAtomSerializer'
op|'('
name|'wsgi'
op|'.'
name|'XMLDictSerializer'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|NSMAP
indent|'    '
name|'NSMAP'
op|'='
op|'{'
name|'None'
op|':'
name|'xmlutil'
op|'.'
name|'XMLNS_ATOM'
op|'}'
newline|'\n'
nl|'\n'
comment|'#TODO(wwolf): this is temporary until we get rid of toprettyxml'
nl|'\n'
comment|'# in the base class (XMLDictSerializer), which I plan to do in'
nl|'\n'
comment|'# another branch'
nl|'\n'
DECL|member|to_xml_string
name|'def'
name|'to_xml_string'
op|'('
name|'self'
op|','
name|'node'
op|','
name|'has_atom'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_add_xmlns'
op|'('
name|'node'
op|','
name|'has_atom'
op|')'
newline|'\n'
name|'return'
name|'node'
op|'.'
name|'toxml'
op|'('
name|'encoding'
op|'='
string|"'UTF-8'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'metadata'
op|'='
name|'None'
op|','
name|'xmlns'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'metadata'
op|'='
name|'metadata'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'if'
name|'not'
name|'xmlns'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'xmlns'
op|'='
name|'wsgi'
op|'.'
name|'XMLNS_ATOM'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'xmlns'
op|'='
name|'xmlns'
newline|'\n'
nl|'\n'
DECL|member|_create_text_elem
dedent|''
dedent|''
name|'def'
name|'_create_text_elem'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'text'
op|','
name|'type'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'elem'
op|'='
name|'self'
op|'.'
name|'_xml_doc'
op|'.'
name|'createElement'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'type'
op|':'
newline|'\n'
indent|'            '
name|'elem'
op|'.'
name|'setAttribute'
op|'('
string|"'type'"
op|','
name|'type'
op|')'
newline|'\n'
dedent|''
name|'elem_text'
op|'='
name|'self'
op|'.'
name|'_xml_doc'
op|'.'
name|'createTextNode'
op|'('
name|'text'
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'appendChild'
op|'('
name|'elem_text'
op|')'
newline|'\n'
name|'return'
name|'elem'
newline|'\n'
nl|'\n'
DECL|member|_get_most_recent_update
dedent|''
name|'def'
name|'_get_most_recent_update'
op|'('
name|'self'
op|','
name|'versions'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'recent'
op|'='
name|'None'
newline|'\n'
name|'for'
name|'version'
name|'in'
name|'versions'
op|':'
newline|'\n'
indent|'            '
name|'updated'
op|'='
name|'datetime'
op|'.'
name|'strptime'
op|'('
name|'version'
op|'['
string|"'updated'"
op|']'
op|','
nl|'\n'
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|')'
newline|'\n'
name|'if'
name|'not'
name|'recent'
op|':'
newline|'\n'
indent|'                '
name|'recent'
op|'='
name|'updated'
newline|'\n'
dedent|''
name|'elif'
name|'updated'
op|'>'
name|'recent'
op|':'
newline|'\n'
indent|'                '
name|'recent'
op|'='
name|'updated'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'recent'
op|'.'
name|'strftime'
op|'('
string|"'%Y-%m-%dT%H:%M:%SZ'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_base_url
dedent|''
name|'def'
name|'_get_base_url'
op|'('
name|'self'
op|','
name|'link_href'
op|')'
op|':'
newline|'\n'
comment|'# Make sure no trailing /'
nl|'\n'
indent|'        '
name|'link_href'
op|'='
name|'link_href'
op|'.'
name|'rstrip'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'return'
name|'link_href'
op|'.'
name|'rsplit'
op|'('
string|"'/'"
op|','
number|'1'
op|')'
op|'['
number|'0'
op|']'
op|'+'
string|"'/'"
newline|'\n'
nl|'\n'
DECL|member|_create_detail_meta
dedent|''
name|'def'
name|'_create_detail_meta'
op|'('
name|'self'
op|','
name|'root'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'title'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'title'"
op|','
string|'"About This Version"'
op|','
nl|'\n'
name|'type'
op|'='
string|"'text'"
op|')'
newline|'\n'
nl|'\n'
name|'updated'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'updated'"
op|','
name|'version'
op|'['
string|"'updated'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'uri'
op|'='
name|'version'
op|'['
string|"'links'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'href'"
op|']'
newline|'\n'
name|'id'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'id'"
op|','
name|'uri'
op|')'
newline|'\n'
nl|'\n'
name|'link'
op|'='
name|'self'
op|'.'
name|'_xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'link'"
op|')'
newline|'\n'
name|'link'
op|'.'
name|'setAttribute'
op|'('
string|"'rel'"
op|','
string|"'self'"
op|')'
newline|'\n'
name|'link'
op|'.'
name|'setAttribute'
op|'('
string|"'href'"
op|','
name|'uri'
op|')'
newline|'\n'
nl|'\n'
name|'author'
op|'='
name|'self'
op|'.'
name|'_xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'author'"
op|')'
newline|'\n'
name|'author_name'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'name'"
op|','
string|"'Rackspace'"
op|')'
newline|'\n'
name|'author_uri'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'uri'"
op|','
string|"'http://www.rackspace.com/'"
op|')'
newline|'\n'
name|'author'
op|'.'
name|'appendChild'
op|'('
name|'author_name'
op|')'
newline|'\n'
name|'author'
op|'.'
name|'appendChild'
op|'('
name|'author_uri'
op|')'
newline|'\n'
nl|'\n'
name|'root'
op|'.'
name|'appendChild'
op|'('
name|'title'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'appendChild'
op|'('
name|'updated'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'appendChild'
op|'('
name|'id'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'appendChild'
op|'('
name|'author'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'appendChild'
op|'('
name|'link'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_create_feed
dedent|''
name|'def'
name|'_create_feed'
op|'('
name|'self'
op|','
name|'versions'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'feed'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'feed'"
op|','
name|'nsmap'
op|'='
name|'self'
op|'.'
name|'NSMAP'
op|')'
newline|'\n'
name|'title'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'feed'
op|','
string|"'title'"
op|')'
newline|'\n'
name|'title'
op|'.'
name|'set'
op|'('
string|"'type'"
op|','
string|"'text'"
op|')'
newline|'\n'
name|'title'
op|'.'
name|'text'
op|'='
string|"'Available API Versions'"
newline|'\n'
nl|'\n'
comment|'# Set this updated to the most recently updated version'
nl|'\n'
name|'recent'
op|'='
name|'self'
op|'.'
name|'_get_most_recent_update'
op|'('
name|'versions'
op|')'
newline|'\n'
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'feed'
op|','
string|"'updated'"
op|')'
op|'.'
name|'text'
op|'='
name|'recent'
newline|'\n'
nl|'\n'
name|'base_url'
op|'='
name|'self'
op|'.'
name|'_get_base_url'
op|'('
name|'versions'
op|'['
number|'0'
op|']'
op|'['
string|"'links'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'href'"
op|']'
op|')'
newline|'\n'
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'feed'
op|','
string|"'id'"
op|')'
op|'.'
name|'text'
op|'='
name|'base_url'
newline|'\n'
nl|'\n'
name|'link'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'feed'
op|','
string|"'link'"
op|')'
newline|'\n'
name|'link'
op|'.'
name|'set'
op|'('
string|"'rel'"
op|','
string|"'self'"
op|')'
newline|'\n'
name|'link'
op|'.'
name|'set'
op|'('
string|"'href'"
op|','
name|'base_url'
op|')'
newline|'\n'
nl|'\n'
name|'author'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'feed'
op|','
string|"'author'"
op|')'
newline|'\n'
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'author'
op|','
string|"'name'"
op|')'
op|'.'
name|'text'
op|'='
string|"'Rackspace'"
newline|'\n'
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'author'
op|','
string|"'uri'"
op|')'
op|'.'
name|'text'
op|'='
string|"'http://www.rackspace.com/'"
newline|'\n'
nl|'\n'
name|'for'
name|'version'
name|'in'
name|'versions'
op|':'
newline|'\n'
indent|'            '
name|'feed'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_create_version_entry'
op|'('
name|'version'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'feed'
newline|'\n'
nl|'\n'
DECL|member|_create_version_entry
dedent|''
name|'def'
name|'_create_version_entry'
op|'('
name|'self'
op|','
name|'version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entry'
op|'='
name|'etree'
op|'.'
name|'Element'
op|'('
string|"'entry'"
op|')'
newline|'\n'
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'entry'
op|','
string|"'id'"
op|')'
op|'.'
name|'text'
op|'='
name|'version'
op|'['
string|"'links'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'href'"
op|']'
newline|'\n'
name|'title'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'entry'
op|','
string|"'title'"
op|')'
newline|'\n'
name|'title'
op|'.'
name|'set'
op|'('
string|"'type'"
op|','
string|"'text'"
op|')'
newline|'\n'
name|'title'
op|'.'
name|'text'
op|'='
string|"'Version %s'"
op|'%'
name|'version'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'entry'
op|','
string|"'updated'"
op|')'
op|'.'
name|'text'
op|'='
name|'version'
op|'['
string|"'updated'"
op|']'
newline|'\n'
nl|'\n'
name|'for'
name|'link'
name|'in'
name|'version'
op|'['
string|"'links'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'link_elem'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'entry'
op|','
string|"'link'"
op|')'
newline|'\n'
name|'link_elem'
op|'.'
name|'set'
op|'('
string|"'rel'"
op|','
name|'link'
op|'['
string|"'rel'"
op|']'
op|')'
newline|'\n'
name|'link_elem'
op|'.'
name|'set'
op|'('
string|"'href'"
op|','
name|'link'
op|'['
string|"'href'"
op|']'
op|')'
newline|'\n'
name|'if'
string|"'type'"
name|'in'
name|'link'
op|':'
newline|'\n'
indent|'                '
name|'link_elem'
op|'.'
name|'set'
op|'('
string|"'type'"
op|','
name|'link'
op|'['
string|"'type'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'content'
op|'='
name|'etree'
op|'.'
name|'SubElement'
op|'('
name|'entry'
op|','
string|"'content'"
op|')'
newline|'\n'
name|'content'
op|'.'
name|'set'
op|'('
string|"'type'"
op|','
string|"'text'"
op|')'
newline|'\n'
name|'content'
op|'.'
name|'text'
op|'='
string|"'Version %s %s (%s)'"
op|'%'
op|'('
name|'version'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'version'
op|'['
string|"'status'"
op|']'
op|','
nl|'\n'
name|'version'
op|'['
string|"'updated'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'entry'
newline|'\n'
nl|'\n'
DECL|member|_create_version_entries
dedent|''
name|'def'
name|'_create_version_entries'
op|'('
name|'self'
op|','
name|'root'
op|','
name|'versions'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'version'
name|'in'
name|'versions'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'self'
op|'.'
name|'_xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'entry'"
op|')'
newline|'\n'
nl|'\n'
name|'id'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'id'"
op|','
name|'version'
op|'['
string|"'links'"
op|']'
op|'['
number|'0'
op|']'
op|'['
string|"'href'"
op|']'
op|')'
newline|'\n'
name|'title'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'title'"
op|','
nl|'\n'
string|"'Version %s'"
op|'%'
name|'version'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'type'
op|'='
string|"'text'"
op|')'
newline|'\n'
name|'updated'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'updated'"
op|','
name|'version'
op|'['
string|"'updated'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'entry'
op|'.'
name|'appendChild'
op|'('
name|'id'
op|')'
newline|'\n'
name|'entry'
op|'.'
name|'appendChild'
op|'('
name|'title'
op|')'
newline|'\n'
name|'entry'
op|'.'
name|'appendChild'
op|'('
name|'updated'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'link'
name|'in'
name|'version'
op|'['
string|"'links'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'link_node'
op|'='
name|'self'
op|'.'
name|'_xml_doc'
op|'.'
name|'createElement'
op|'('
string|"'link'"
op|')'
newline|'\n'
name|'link_node'
op|'.'
name|'setAttribute'
op|'('
string|"'rel'"
op|','
name|'link'
op|'['
string|"'rel'"
op|']'
op|')'
newline|'\n'
name|'link_node'
op|'.'
name|'setAttribute'
op|'('
string|"'href'"
op|','
name|'link'
op|'['
string|"'href'"
op|']'
op|')'
newline|'\n'
name|'if'
string|"'type'"
name|'in'
name|'link'
op|':'
newline|'\n'
indent|'                    '
name|'link_node'
op|'.'
name|'setAttribute'
op|'('
string|"'type'"
op|','
name|'link'
op|'['
string|"'type'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'entry'
op|'.'
name|'appendChild'
op|'('
name|'link_node'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'content'
op|'='
name|'self'
op|'.'
name|'_create_text_elem'
op|'('
string|"'content'"
op|','
nl|'\n'
string|"'Version %s %s (%s)'"
op|'%'
nl|'\n'
op|'('
name|'version'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
name|'version'
op|'['
string|"'status'"
op|']'
op|','
nl|'\n'
name|'version'
op|'['
string|"'updated'"
op|']'
op|')'
op|','
nl|'\n'
name|'type'
op|'='
string|"'text'"
op|')'
newline|'\n'
nl|'\n'
name|'entry'
op|'.'
name|'appendChild'
op|'('
name|'content'
op|')'
newline|'\n'
name|'root'
op|'.'
name|'appendChild'
op|'('
name|'entry'
op|')'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
dedent|''
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'feed'
op|'='
name|'self'
op|'.'
name|'_create_feed'
op|'('
name|'data'
op|'['
string|"'versions'"
op|']'
op|')'
newline|'\n'
name|'return'
name|'etree'
op|'.'
name|'tostring'
op|'('
name|'feed'
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
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_xml_doc'
op|'='
name|'minidom'
op|'.'
name|'Document'
op|'('
op|')'
newline|'\n'
name|'node'
op|'='
name|'self'
op|'.'
name|'_xml_doc'
op|'.'
name|'createElementNS'
op|'('
name|'self'
op|'.'
name|'xmlns'
op|','
string|"'feed'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_detail_meta'
op|'('
name|'node'
op|','
name|'data'
op|'['
string|"'version'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_create_version_entries'
op|'('
name|'node'
op|','
op|'['
name|'data'
op|'['
string|"'version'"
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'to_xml_string'
op|'('
name|'node'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VersionsHeadersSerializer
dedent|''
dedent|''
name|'class'
name|'VersionsHeadersSerializer'
op|'('
name|'wsgi'
op|'.'
name|'ResponseHeadersSerializer'
op|')'
op|':'
newline|'\n'
DECL|member|multi
indent|'    '
name|'def'
name|'multi'
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
number|'300'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_resource
dedent|''
dedent|''
name|'def'
name|'create_resource'
op|'('
name|'version'
op|'='
string|"'1.0'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'controller'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
name|'VersionV10'
op|','
nl|'\n'
string|"'1.1'"
op|':'
name|'VersionV11'
op|','
nl|'\n'
op|'}'
op|'['
name|'version'
op|']'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'body_serializers'
op|'='
op|'{'
nl|'\n'
string|"'application/xml'"
op|':'
name|'VersionsXMLSerializer'
op|'('
op|')'
op|','
nl|'\n'
string|"'application/atom+xml'"
op|':'
name|'VersionsAtomSerializer'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'serializer'
op|'='
name|'wsgi'
op|'.'
name|'ResponseSerializer'
op|'('
name|'body_serializers'
op|')'
newline|'\n'
nl|'\n'
name|'supported_content_types'
op|'='
op|'('
string|"'application/json'"
op|','
nl|'\n'
string|"'application/xml'"
op|','
nl|'\n'
string|"'application/atom+xml'"
op|')'
newline|'\n'
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'RequestDeserializer'
op|'('
nl|'\n'
name|'supported_content_types'
op|'='
name|'supported_content_types'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'wsgi'
op|'.'
name|'Resource'
op|'('
name|'controller'
op|','
name|'serializer'
op|'='
name|'serializer'
op|','
nl|'\n'
name|'deserializer'
op|'='
name|'deserializer'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
