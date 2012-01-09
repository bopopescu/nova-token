begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Andrew Bogott for the Wikimedia Foundation'
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
comment|'#    under the License'
nl|'\n'
nl|'\n'
name|'import'
name|'urllib'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
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
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'xmlutil'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
op|'.'
name|'v2'
name|'import'
name|'extensions'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'import'
name|'network'
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
string|"'nova.api.openstack.v2.contrib.floating_ip_dns'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_dns_entry
name|'def'
name|'make_dns_entry'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'ip'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'type'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'zone'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'name'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|make_zone_entry
dedent|''
name|'def'
name|'make_zone_entry'
op|'('
name|'elem'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'elem'
op|'.'
name|'set'
op|'('
string|"'zone'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPDNSTemplate
dedent|''
name|'class'
name|'FloatingIPDNSTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'dns_entry'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'dns_entry'"
op|')'
newline|'\n'
name|'make_dns_entry'
op|'('
name|'root'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPDNSsTemplate
dedent|''
dedent|''
name|'class'
name|'FloatingIPDNSsTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'dns_entries'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'dns_entry'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'dns_entries'"
op|')'
newline|'\n'
name|'make_dns_entry'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ZonesTemplate
dedent|''
dedent|''
name|'class'
name|'ZonesTemplate'
op|'('
name|'xmlutil'
op|'.'
name|'TemplateBuilder'
op|')'
op|':'
newline|'\n'
DECL|member|construct
indent|'    '
name|'def'
name|'construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root'
op|'='
name|'xmlutil'
op|'.'
name|'TemplateElement'
op|'('
string|"'zones'"
op|')'
newline|'\n'
name|'elem'
op|'='
name|'xmlutil'
op|'.'
name|'SubTemplateElement'
op|'('
name|'root'
op|','
string|"'zone'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'zones'"
op|')'
newline|'\n'
name|'make_zone_entry'
op|'('
name|'elem'
op|')'
newline|'\n'
name|'return'
name|'xmlutil'
op|'.'
name|'MasterTemplate'
op|'('
name|'root'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_dns_entry_view
dedent|''
dedent|''
name|'def'
name|'_translate_dns_entry_view'
op|'('
name|'dns_entry'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'result'
op|'['
string|"'ip'"
op|']'
op|'='
name|'dns_entry'
op|'.'
name|'get'
op|'('
string|"'ip'"
op|')'
newline|'\n'
name|'result'
op|'['
string|"'id'"
op|']'
op|'='
name|'dns_entry'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
newline|'\n'
name|'result'
op|'['
string|"'type'"
op|']'
op|'='
name|'dns_entry'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
newline|'\n'
name|'result'
op|'['
string|"'zone'"
op|']'
op|'='
name|'dns_entry'
op|'.'
name|'get'
op|'('
string|"'zone'"
op|')'
newline|'\n'
name|'result'
op|'['
string|"'name'"
op|']'
op|'='
name|'dns_entry'
op|'.'
name|'get'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'dns_entry'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_dns_entries_view
dedent|''
name|'def'
name|'_translate_dns_entries_view'
op|'('
name|'dns_entries'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'dns_entries'"
op|':'
op|'['
name|'_translate_dns_entry_view'
op|'('
name|'entry'
op|')'
op|'['
string|"'dns_entry'"
op|']'
nl|'\n'
name|'for'
name|'entry'
name|'in'
name|'dns_entries'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_zone_entries_view
dedent|''
name|'def'
name|'_translate_zone_entries_view'
op|'('
name|'zonelist'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'zones'"
op|':'
op|'['
op|'{'
string|"'zone'"
op|':'
name|'zone'
op|'}'
name|'for'
name|'zone'
name|'in'
name|'zonelist'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unquote_zone
dedent|''
name|'def'
name|'_unquote_zone'
op|'('
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unquoting function for receiving a zone name in a URL.\n\n    Zone names tend to have .\'s in them.  Urllib doesn\'t quote dots,\n    but Routes tends to choke on them, so we need an extra level of\n    by-hand quoting here.\n    """'
newline|'\n'
name|'return'
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'zone'
op|')'
op|'.'
name|'replace'
op|'('
string|"'%2E'"
op|','
string|"'.'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_dns_entry
dedent|''
name|'def'
name|'_create_dns_entry'
op|'('
name|'ip'
op|','
name|'name'
op|','
name|'zone'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'ip'"
op|':'
name|'ip'
op|','
string|"'name'"
op|':'
name|'name'
op|','
string|"'zone'"
op|':'
name|'zone'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPDNSController
dedent|''
name|'class'
name|'FloatingIPDNSController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""DNS Entry controller for OpenStack API"""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'FloatingIPDNSController'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'FloatingIPDNSsTemplate'
op|')'
newline|'\n'
DECL|member|show
name|'def'
name|'show'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of dns entries.  If ip is specified, query for\n           names.  if name is specified, query for ips.\n           Quoted domain (aka \'zone\') specified as id."""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'params'
op|'='
name|'req'
op|'.'
name|'str_GET'
newline|'\n'
name|'floating_ip'
op|'='
name|'params'
op|'['
string|"'ip'"
op|']'
name|'if'
string|"'ip'"
name|'in'
name|'params'
name|'else'
string|'""'
newline|'\n'
name|'name'
op|'='
name|'params'
op|'['
string|"'name'"
op|']'
name|'if'
string|"'name'"
name|'in'
name|'params'
name|'else'
string|'""'
newline|'\n'
name|'zone'
op|'='
name|'_unquote_zone'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'floating_ip'
op|':'
newline|'\n'
indent|'            '
name|'entries'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_dns_entries_by_address'
op|'('
name|'context'
op|','
nl|'\n'
name|'floating_ip'
op|','
nl|'\n'
name|'zone'
op|')'
newline|'\n'
name|'entrylist'
op|'='
op|'['
name|'_create_dns_entry'
op|'('
name|'floating_ip'
op|','
name|'entry'
op|','
name|'zone'
op|')'
nl|'\n'
name|'for'
name|'entry'
name|'in'
name|'entries'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'name'
op|':'
newline|'\n'
indent|'            '
name|'entries'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_dns_entries_by_name'
op|'('
name|'context'
op|','
nl|'\n'
name|'name'
op|','
name|'zone'
op|')'
newline|'\n'
name|'entrylist'
op|'='
op|'['
name|'_create_dns_entry'
op|'('
name|'entry'
op|','
name|'name'
op|','
name|'zone'
op|')'
nl|'\n'
name|'for'
name|'entry'
name|'in'
name|'entries'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'entrylist'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_translate_dns_entries_view'
op|'('
name|'entrylist'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'ZonesTemplate'
op|')'
newline|'\n'
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of available DNS zones."""'
newline|'\n'
nl|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'zones'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_dns_zones'
op|'('
name|'context'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'_translate_zone_entries_view'
op|'('
name|'zones'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'wsgi'
op|'.'
name|'serializers'
op|'('
name|'xml'
op|'='
name|'FloatingIPDNSTemplate'
op|')'
newline|'\n'
DECL|member|create
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add dns entry for name and address"""'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'body'
op|'['
string|"'dns_entry'"
op|']'
newline|'\n'
name|'address'
op|'='
name|'entry'
op|'['
string|"'ip'"
op|']'
newline|'\n'
name|'name'
op|'='
name|'entry'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'dns_type'
op|'='
name|'entry'
op|'['
string|"'dns_type'"
op|']'
newline|'\n'
name|'zone'
op|'='
name|'entry'
op|'['
string|"'zone'"
op|']'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'TypeError'
op|','
name|'KeyError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPUnprocessableEntity'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'add_dns_entry'
op|'('
name|'context'
op|','
name|'address'
op|','
name|'name'
op|','
nl|'\n'
name|'dns_type'
op|','
name|'zone'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'FloatingIpDNSExists'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'409'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'_translate_dns_entry_view'
op|'('
op|'{'
string|"'ip'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'name'
op|','
nl|'\n'
string|"'type'"
op|':'
name|'dns_type'
op|','
nl|'\n'
string|"'zone'"
op|':'
name|'zone'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the entry identified by req and id. """'
newline|'\n'
name|'context'
op|'='
name|'req'
op|'.'
name|'environ'
op|'['
string|"'nova.context'"
op|']'
newline|'\n'
name|'params'
op|'='
name|'req'
op|'.'
name|'str_GET'
newline|'\n'
name|'name'
op|'='
name|'params'
op|'['
string|"'name'"
op|']'
name|'if'
string|"'name'"
name|'in'
name|'params'
name|'else'
string|'""'
newline|'\n'
name|'zone'
op|'='
name|'_unquote_zone'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'delete_dns_entry'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'zone'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'404'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'webob'
op|'.'
name|'Response'
op|'('
name|'status_int'
op|'='
number|'200'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Floating_ip_dns
dedent|''
dedent|''
name|'class'
name|'Floating_ip_dns'
op|'('
name|'extensions'
op|'.'
name|'ExtensionDescriptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Floating IP DNS support"""'
newline|'\n'
nl|'\n'
DECL|variable|name
name|'name'
op|'='
string|'"Floating_ip_dns"'
newline|'\n'
DECL|variable|alias
name|'alias'
op|'='
string|'"os-floating-ip-dns"'
newline|'\n'
DECL|variable|namespace
name|'namespace'
op|'='
string|'"http://docs.openstack.org/ext/floating_ip_dns/api/v1.1"'
newline|'\n'
DECL|variable|updated
name|'updated'
op|'='
string|'"2011-12-23:00:00+00:00"'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ext_mgr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'Floating_ip_dns'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'ext_mgr'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_resources
dedent|''
name|'def'
name|'get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'resources'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'os-floating-ip-dns'"
op|','
nl|'\n'
name|'FloatingIPDNSController'
op|'('
op|')'
op|')'
newline|'\n'
name|'resources'
op|'.'
name|'append'
op|'('
name|'res'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'resources'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
