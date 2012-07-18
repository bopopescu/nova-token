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
name|'extensions'
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
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
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
DECL|variable|authorize
name|'authorize'
op|'='
name|'extensions'
op|'.'
name|'extension_authorizer'
op|'('
string|"'compute'"
op|','
string|"'floating_ip_dns'"
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
string|"'domain'"
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
DECL|function|make_domain_entry
dedent|''
name|'def'
name|'make_domain_entry'
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
string|"'domain'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'scope'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'project'"
op|')'
newline|'\n'
name|'elem'
op|'.'
name|'set'
op|'('
string|"'availability_zone'"
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
DECL|class|DomainTemplate
dedent|''
dedent|''
name|'class'
name|'DomainTemplate'
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
string|"'domain_entry'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'domain_entry'"
op|')'
newline|'\n'
name|'make_domain_entry'
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
DECL|class|DomainsTemplate
dedent|''
dedent|''
name|'class'
name|'DomainsTemplate'
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
string|"'domain_entries'"
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
string|"'domain_entry'"
op|','
nl|'\n'
name|'selector'
op|'='
string|"'domain_entries'"
op|')'
newline|'\n'
name|'make_domain_entry'
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
string|"'domain'"
op|']'
op|'='
name|'dns_entry'
op|'.'
name|'get'
op|'('
string|"'domain'"
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
DECL|function|_translate_domain_entry_view
dedent|''
name|'def'
name|'_translate_domain_entry_view'
op|'('
name|'domain_entry'
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
string|"'domain'"
op|']'
op|'='
name|'domain_entry'
op|'.'
name|'get'
op|'('
string|"'domain'"
op|')'
newline|'\n'
name|'result'
op|'['
string|"'scope'"
op|']'
op|'='
name|'domain_entry'
op|'.'
name|'get'
op|'('
string|"'scope'"
op|')'
newline|'\n'
name|'result'
op|'['
string|"'project'"
op|']'
op|'='
name|'domain_entry'
op|'.'
name|'get'
op|'('
string|"'project'"
op|')'
newline|'\n'
name|'result'
op|'['
string|"'availability_zone'"
op|']'
op|'='
name|'domain_entry'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'domain_entry'"
op|':'
name|'result'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_translate_domain_entries_view
dedent|''
name|'def'
name|'_translate_domain_entries_view'
op|'('
name|'domain_entries'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'domain_entries'"
op|':'
nl|'\n'
op|'['
name|'_translate_domain_entry_view'
op|'('
name|'entry'
op|')'
op|'['
string|"'domain_entry'"
op|']'
nl|'\n'
name|'for'
name|'entry'
name|'in'
name|'domain_entries'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unquote_domain
dedent|''
name|'def'
name|'_unquote_domain'
op|'('
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unquoting function for receiving a domain name in a URL.\n\n    Domain names tend to have .\'s in them.  Urllib doesn\'t quote dots,\n    but Routes tends to choke on them, so we need an extra level of\n    by-hand quoting here.\n    """'
newline|'\n'
name|'return'
name|'urllib'
op|'.'
name|'unquote'
op|'('
name|'domain'
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
name|'domain'
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
string|"'domain'"
op|':'
name|'domain'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_domain_entry
dedent|''
name|'def'
name|'_create_domain_entry'
op|'('
name|'domain'
op|','
name|'scope'
op|'='
name|'None'
op|','
name|'project'
op|'='
name|'None'
op|','
name|'av_zone'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'domain'"
op|':'
name|'domain'
op|','
string|"'scope'"
op|':'
name|'scope'
op|','
string|"'project'"
op|':'
name|'project'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'av_zone'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPDNSDomainController
dedent|''
name|'class'
name|'FloatingIPDNSDomainController'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""DNS domain controller for OpenStack API"""'
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
name|'FloatingIPDNSDomainController'
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
name|'DomainsTemplate'
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
string|'"""Return a list of available DNS domains."""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'domains'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'get_dns_domains'
op|'('
name|'context'
op|')'
newline|'\n'
name|'domainlist'
op|'='
op|'['
name|'_create_domain_entry'
op|'('
name|'domain'
op|'['
string|"'domain'"
op|']'
op|','
nl|'\n'
name|'domain'
op|'.'
name|'get'
op|'('
string|"'scope'"
op|')'
op|','
nl|'\n'
name|'domain'
op|'.'
name|'get'
op|'('
string|"'project'"
op|')'
op|','
nl|'\n'
name|'domain'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|')'
op|')'
nl|'\n'
name|'for'
name|'domain'
name|'in'
name|'domains'
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'_translate_domain_entries_view'
op|'('
name|'domainlist'
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
name|'DomainTemplate'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add or modify domain entry"""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'fqdomain'
op|'='
name|'_unquote_domain'
op|'('
name|'id'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'entry'
op|'='
name|'body'
op|'['
string|"'domain_entry'"
op|']'
newline|'\n'
name|'scope'
op|'='
name|'entry'
op|'['
string|"'scope'"
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
dedent|''
name|'project'
op|'='
name|'entry'
op|'.'
name|'get'
op|'('
string|"'project'"
op|','
name|'None'
op|')'
newline|'\n'
name|'av_zone'
op|'='
name|'entry'
op|'.'
name|'get'
op|'('
string|"'availability_zone'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
op|'('
name|'scope'
name|'not'
name|'in'
op|'('
string|"'private'"
op|','
string|"'public'"
op|')'
name|'or'
nl|'\n'
name|'project'
name|'and'
name|'av_zone'
name|'or'
nl|'\n'
name|'scope'
op|'=='
string|"'private'"
name|'and'
name|'project'
name|'or'
nl|'\n'
name|'scope'
op|'=='
string|"'public'"
name|'and'
name|'av_zone'
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
dedent|''
name|'if'
name|'scope'
op|'=='
string|"'private'"
op|':'
newline|'\n'
indent|'            '
name|'create_dns_domain'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'create_private_dns_domain'
newline|'\n'
name|'area_name'
op|','
name|'area'
op|'='
string|"'availability_zone'"
op|','
name|'av_zone'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'create_dns_domain'
op|'='
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'create_public_dns_domain'
newline|'\n'
name|'area_name'
op|','
name|'area'
op|'='
string|"'project'"
op|','
name|'project'
newline|'\n'
dedent|''
name|'create_dns_domain'
op|'('
name|'context'
op|','
name|'fqdomain'
op|','
name|'area'
op|')'
newline|'\n'
name|'return'
name|'_translate_domain_entry_view'
op|'('
op|'{'
string|"'domain'"
op|':'
name|'fqdomain'
op|','
nl|'\n'
string|"'scope'"
op|':'
name|'scope'
op|','
nl|'\n'
name|'area_name'
op|':'
name|'area'
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
string|'"""Delete the domain identified by id. """'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'domain'
op|'='
name|'_unquote_domain'
op|'('
name|'id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete the whole domain'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'delete_dns_domain'
op|'('
name|'context'
op|','
name|'domain'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'e'
op|')'
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
number|'202'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FloatingIPDNSEntryController
dedent|''
dedent|''
name|'class'
name|'FloatingIPDNSEntryController'
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
name|'FloatingIPDNSEntryController'
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
name|'FloatingIPDNSTemplate'
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
name|'domain_id'
op|','
name|'id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the DNS entry that corresponds to domain_id and id."""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'domain'
op|'='
name|'_unquote_domain'
op|'('
name|'domain_id'
op|')'
newline|'\n'
name|'name'
op|'='
name|'id'
newline|'\n'
nl|'\n'
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
name|'domain'
op|')'
newline|'\n'
name|'entry'
op|'='
name|'_create_dns_entry'
op|'('
name|'entries'
op|'['
number|'0'
op|']'
op|','
name|'name'
op|','
name|'domain'
op|')'
newline|'\n'
name|'return'
name|'_translate_dns_entry_view'
op|'('
name|'entry'
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
DECL|member|index
name|'def'
name|'index'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'domain_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return a list of dns entries for the specified domain and ip."""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'params'
op|'='
name|'req'
op|'.'
name|'GET'
newline|'\n'
name|'floating_ip'
op|'='
name|'params'
op|'.'
name|'get'
op|'('
string|"'ip'"
op|')'
newline|'\n'
name|'domain'
op|'='
name|'_unquote_domain'
op|'('
name|'domain_id'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'floating_ip'
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
name|'domain'
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
name|'domain'
op|')'
nl|'\n'
name|'for'
name|'entry'
name|'in'
name|'entries'
op|']'
newline|'\n'
nl|'\n'
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
name|'FloatingIPDNSTemplate'
op|')'
newline|'\n'
DECL|member|update
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'req'
op|','
name|'domain_id'
op|','
name|'id'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Add or modify dns entry"""'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'domain'
op|'='
name|'_unquote_domain'
op|'('
name|'domain_id'
op|')'
newline|'\n'
name|'name'
op|'='
name|'id'
newline|'\n'
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
name|'dns_type'
op|'='
name|'entry'
op|'['
string|"'dns_type'"
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
name|'domain'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'entries'
op|':'
newline|'\n'
comment|'# create!'
nl|'\n'
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
name|'domain'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# modify!'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'network_api'
op|'.'
name|'modify_dns_entry'
op|'('
name|'context'
op|','
name|'name'
op|','
name|'address'
op|','
name|'domain'
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
string|"'domain'"
op|':'
name|'domain'
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
name|'domain_id'
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
name|'authorize'
op|'('
name|'context'
op|')'
newline|'\n'
name|'domain'
op|'='
name|'_unquote_domain'
op|'('
name|'domain_id'
op|')'
newline|'\n'
name|'name'
op|'='
name|'id'
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
name|'domain'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'e'
op|')'
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
number|'202'
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
string|'"2011-12-23T00:00:00+00:00"'
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
name|'FloatingIPDNSDomainController'
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
name|'res'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'entries'"
op|','
nl|'\n'
name|'FloatingIPDNSEntryController'
op|'('
op|')'
op|','
nl|'\n'
name|'parent'
op|'='
op|'{'
string|"'member_name'"
op|':'
string|"'domain'"
op|','
nl|'\n'
string|"'collection_name'"
op|':'
string|"'os-floating-ip-dns'"
op|'}'
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
