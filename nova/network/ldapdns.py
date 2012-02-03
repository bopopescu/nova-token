begin_unit
comment|'# Copyright 2012 Andrew Bogott for the Wikimedia Foundation'
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
name|'ldap'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'auth'
name|'import'
name|'fakeldap'
newline|'\n'
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
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
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
string|'"nova.network.manager"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|ldap_dns_opts
name|'ldap_dns_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_url'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'ldap://ldap.example.com:389'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'URL for ldap server which will store dns entries'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_user'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'uid=admin,ou=people,dc=example,dc=org'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'user for ldap DNS'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'password'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'password for ldap DNS'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_hostmaster'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'hostmaster@example.org'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Hostmaster for ldap dns driver Statement of Authority'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'ldap_dns_servers'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'[dns.example.org]'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'DNS Servers for ldap dns driver'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_base_dn'"
op|','
nl|'\n'
name|'default'
op|'='
string|"'ou=hosts,dc=example,dc=org'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Base DN for DNS entries in ldap'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_refresh'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'1800'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Refresh interval (in seconds) for ldap dns driver '"
nl|'\n'
string|"'Statement of Authority'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_retry'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'3600'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Retry interval (in seconds) for ldap dns driver '"
nl|'\n'
string|"'Statement of Authority'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_expiry'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'86400'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Expiry interval (in seconds) for ldap dns driver '"
nl|'\n'
string|"'Statement of Authority'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'ldap_dns_soa_minimum'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'7200'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Minimum interval (in seconds) for ldap dns driver '"
nl|'\n'
string|"'Statement of Authority'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'add_options'
op|'('
name|'ldap_dns_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|utf8
name|'def'
name|'utf8'
op|'('
name|'instring'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'type'
op|'('
name|'instring'
op|')'
op|'=='
name|'unicode'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'instring'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'UnicodeError'
op|','
name|'AttributeError'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Unable to encode %s as utf8. Discarding.'"
op|')'
op|'%'
name|'val'
op|')'
newline|'\n'
name|'return'
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'instring'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Importing ldap.modlist breaks the tests for some reason,'
nl|'\n'
comment|'#  so this is an abbreviated version of a function from'
nl|'\n'
comment|'#  there.'
nl|'\n'
DECL|function|create_modlist
dedent|''
dedent|''
name|'def'
name|'create_modlist'
op|'('
name|'newattrs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'modlist'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'attrtype'
name|'in'
name|'newattrs'
op|'.'
name|'keys'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utf8_vals'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'val'
name|'in'
name|'newattrs'
op|'['
name|'attrtype'
op|']'
op|':'
newline|'\n'
indent|'            '
name|'utf8_vals'
op|'.'
name|'append'
op|'('
name|'utf8'
op|'('
name|'val'
op|')'
op|')'
newline|'\n'
dedent|''
name|'newattrs'
op|'['
name|'attrtype'
op|']'
op|'='
name|'utf8_vals'
newline|'\n'
name|'modlist'
op|'.'
name|'append'
op|'('
op|'('
name|'attrtype'
op|','
name|'newattrs'
op|'['
name|'attrtype'
op|']'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'modlist'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DNSEntry
dedent|''
name|'class'
name|'DNSEntry'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'ldap_object'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""ldap_object is an instance of ldap.LDAPObject.\n           It should already be initialized and bound before\n           getting passed in here."""'
newline|'\n'
name|'self'
op|'.'
name|'lobj'
op|'='
name|'ldap_object'
newline|'\n'
name|'self'
op|'.'
name|'ldap_tuple'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'qualified_domain'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_tuple_for_domain
name|'def'
name|'_get_tuple_for_domain'
op|'('
name|'cls'
op|','
name|'lobj'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entry'
op|'='
name|'lobj'
op|'.'
name|'search_s'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_base_dn'
op|','
name|'ldap'
op|'.'
name|'SCOPE_SUBTREE'
op|','
nl|'\n'
string|'"(associatedDomain=%s)"'
op|'%'
name|'utf8'
op|'('
name|'domain'
op|')'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'entry'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'entry'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
string|'"Found multiple matches for domain %s.\\n%s"'
op|'%'
nl|'\n'
op|'('
name|'domain'
op|','
name|'entry'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'entry'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_get_all_domains
name|'def'
name|'_get_all_domains'
op|'('
name|'cls'
op|','
name|'lobj'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entries'
op|'='
name|'lobj'
op|'.'
name|'search_s'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_base_dn'
op|','
nl|'\n'
name|'ldap'
op|'.'
name|'SCOPE_SUBTREE'
op|','
string|'"(sOARecord=*)"'
op|')'
newline|'\n'
name|'domains'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'entry'
name|'in'
name|'entries'
op|':'
newline|'\n'
indent|'            '
name|'domain'
op|'='
name|'entry'
op|'['
number|'1'
op|']'
op|'.'
name|'get'
op|'('
string|"'associatedDomain'"
op|')'
newline|'\n'
name|'if'
name|'domain'
op|':'
newline|'\n'
indent|'                '
name|'domains'
op|'.'
name|'append'
op|'('
name|'domain'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'domains'
newline|'\n'
nl|'\n'
DECL|member|_set_tuple
dedent|''
name|'def'
name|'_set_tuple'
op|'('
name|'self'
op|','
name|'tuple'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'ldap_tuple'
op|'='
name|'tuple'
newline|'\n'
nl|'\n'
DECL|member|_qualify
dedent|''
name|'def'
name|'_qualify'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"%s.%s"'
op|'%'
op|'('
name|'name'
op|','
name|'self'
op|'.'
name|'qualified_domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_dequalify
dedent|''
name|'def'
name|'_dequalify'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'z'
op|'='
string|'".%s"'
op|'%'
name|'self'
op|'.'
name|'qualified_domain'
newline|'\n'
name|'if'
name|'name'
op|'.'
name|'endswith'
op|'('
name|'z'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'dequalified'
op|'='
name|'name'
op|'['
number|'0'
op|':'
name|'name'
op|'.'
name|'rfind'
op|'('
name|'z'
op|')'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
string|'"Unable to dequalify.  %s is not in %s.\\n"'
op|'%'
op|'('
name|'name'
op|','
nl|'\n'
name|'self'
op|'.'
name|'qualified_domain'
op|')'
op|')'
newline|'\n'
name|'dequalified'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'dequalified'
newline|'\n'
nl|'\n'
DECL|member|_dn
dedent|''
name|'def'
name|'_dn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'ldap_tuple'
op|'['
number|'0'
op|']'
newline|'\n'
DECL|variable|dn
dedent|''
name|'dn'
op|'='
name|'property'
op|'('
name|'_dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_rdn
name|'def'
name|'_rdn'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'dn'
op|'.'
name|'partition'
op|'('
string|"','"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
DECL|variable|rdn
dedent|''
name|'rdn'
op|'='
name|'property'
op|'('
name|'_rdn'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DomainEntry
dedent|''
name|'class'
name|'DomainEntry'
op|'('
name|'DNSEntry'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|_soa
name|'def'
name|'_soa'
op|'('
name|'cls'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'date'
op|'='
name|'time'
op|'.'
name|'strftime'
op|'('
string|'"%Y%m%d%H%M%S"'
op|')'
newline|'\n'
name|'soa'
op|'='
string|'"%s %s %s %s %s %s %s"'
op|'%'
op|'('
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_servers'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_soa_hostmaster'
op|','
nl|'\n'
name|'date'
op|','
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_soa_refresh'
op|','
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_soa_retry'
op|','
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_soa_expiry'
op|','
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_soa_minimum'
op|')'
newline|'\n'
name|'return'
name|'utf8'
op|'('
name|'soa'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|create_domain
name|'def'
name|'create_domain'
op|'('
name|'cls'
op|','
name|'lobj'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a new domain entry, and return an object that wraps it."""'
newline|'\n'
name|'entry'
op|'='
name|'cls'
op|'.'
name|'_get_tuple_for_domain'
op|'('
name|'lobj'
op|','
name|'domain'
op|')'
newline|'\n'
name|'if'
name|'entry'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FloatingIpDNSExists'
op|'('
name|'name'
op|'='
name|'domain'
op|','
name|'domain'
op|'='
string|'""'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'newdn'
op|'='
string|'"dc=%s,%s"'
op|'%'
op|'('
name|'domain'
op|','
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_base_dn'
op|')'
newline|'\n'
name|'attrs'
op|'='
op|'{'
string|"'objectClass'"
op|':'
op|'['
string|"'domainrelatedobject'"
op|','
string|"'dnsdomain'"
op|','
nl|'\n'
string|"'domain'"
op|','
string|"'dcobject'"
op|','
string|"'top'"
op|']'
op|','
nl|'\n'
string|"'sOARecord'"
op|':'
op|'['
name|'cls'
op|'.'
name|'_soa'
op|'('
op|')'
op|']'
op|','
nl|'\n'
string|"'associatedDomain'"
op|':'
op|'['
name|'domain'
op|']'
op|','
nl|'\n'
string|"'dc'"
op|':'
op|'['
name|'domain'
op|']'
op|'}'
newline|'\n'
name|'lobj'
op|'.'
name|'add_s'
op|'('
name|'newdn'
op|','
name|'create_modlist'
op|'('
name|'attrs'
op|')'
op|')'
newline|'\n'
name|'return'
name|'DomainEntry'
op|'('
name|'lobj'
op|','
name|'domain'
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
name|'ldap_object'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'DomainEntry'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'ldap_object'
op|')'
newline|'\n'
name|'entry'
op|'='
name|'self'
op|'.'
name|'_get_tuple_for_domain'
op|'('
name|'self'
op|'.'
name|'lobj'
op|','
name|'domain'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'entry'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_set_tuple'
op|'('
name|'entry'
op|')'
newline|'\n'
name|'assert'
op|'('
name|'entry'
op|'['
number|'1'
op|']'
op|'['
string|"'associatedDomain'"
op|']'
op|'['
number|'0'
op|']'
op|'=='
name|'domain'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'qualified_domain'
op|'='
name|'domain'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
name|'def'
name|'delete'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete the domain that this entry refers to."""'
newline|'\n'
name|'entries'
op|'='
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'search_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|','
nl|'\n'
name|'ldap'
op|'.'
name|'SCOPE_SUBTREE'
op|','
nl|'\n'
string|"'(aRecord=*)'"
op|')'
newline|'\n'
name|'for'
name|'entry'
name|'in'
name|'entries'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'delete_s'
op|'('
name|'entry'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'delete_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_soa
dedent|''
name|'def'
name|'update_soa'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mlist'
op|'='
op|'['
op|'('
name|'ldap'
op|'.'
name|'MOD_REPLACE'
op|','
string|"'sOARecord'"
op|','
name|'self'
op|'.'
name|'_soa'
op|'('
op|')'
op|')'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'modify_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|','
name|'mlist'
op|')'
newline|'\n'
nl|'\n'
DECL|member|subentry_with_name
dedent|''
name|'def'
name|'subentry_with_name'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entry'
op|'='
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'search_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|','
name|'ldap'
op|'.'
name|'SCOPE_SUBTREE'
op|','
nl|'\n'
string|'"(associatedDomain=%s.%s)"'
op|'%'
nl|'\n'
op|'('
name|'utf8'
op|'('
name|'name'
op|')'
op|','
name|'utf8'
op|'('
name|'self'
op|'.'
name|'qualified_domain'
op|')'
op|')'
op|')'
newline|'\n'
name|'if'
name|'entry'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'HostEntry'
op|'('
name|'self'
op|','
name|'entry'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
DECL|member|subentries_with_ip
dedent|''
dedent|''
name|'def'
name|'subentries_with_ip'
op|'('
name|'self'
op|','
name|'ip'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entries'
op|'='
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'search_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|','
name|'ldap'
op|'.'
name|'SCOPE_SUBTREE'
op|','
nl|'\n'
string|'"(aRecord=%s)"'
op|'%'
name|'utf8'
op|'('
name|'ip'
op|')'
op|')'
newline|'\n'
name|'objs'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'entry'
name|'in'
name|'entries'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'associatedDomain'"
name|'in'
name|'entry'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'objs'
op|'.'
name|'append'
op|'('
name|'HostEntry'
op|'('
name|'self'
op|','
name|'entry'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'objs'
newline|'\n'
nl|'\n'
DECL|member|add_entry
dedent|''
name|'def'
name|'add_entry'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'self'
op|'.'
name|'subentry_with_name'
op|'('
name|'name'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'FloatingIpDNSExists'
op|'('
name|'name'
op|'='
name|'name'
op|','
nl|'\n'
name|'domain'
op|'='
name|'self'
op|'.'
name|'qualified_domain'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'entries'
op|'='
name|'self'
op|'.'
name|'subentries_with_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'if'
name|'entries'
op|':'
newline|'\n'
comment|'# We already have an ldap entry for this IP, so we just'
nl|'\n'
comment|'# need to add the new name.'
nl|'\n'
indent|'            '
name|'existingdn'
op|'='
name|'entries'
op|'['
number|'0'
op|']'
op|'.'
name|'dn'
newline|'\n'
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'modify_s'
op|'('
name|'existingdn'
op|','
op|'['
op|'('
name|'ldap'
op|'.'
name|'MOD_ADD'
op|','
nl|'\n'
string|"'associatedDomain'"
op|','
nl|'\n'
name|'utf8'
op|'('
name|'self'
op|'.'
name|'_qualify'
op|'('
name|'name'
op|')'
op|')'
op|')'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'self'
op|'.'
name|'subentry_with_name'
op|'('
name|'name'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# We need to create an entirely new entry.'
nl|'\n'
indent|'            '
name|'newdn'
op|'='
string|'"dc=%s,%s"'
op|'%'
op|'('
name|'name'
op|','
name|'self'
op|'.'
name|'dn'
op|')'
newline|'\n'
name|'attrs'
op|'='
op|'{'
string|"'objectClass'"
op|':'
op|'['
string|"'domainrelatedobject'"
op|','
string|"'dnsdomain'"
op|','
nl|'\n'
string|"'domain'"
op|','
string|"'dcobject'"
op|','
string|"'top'"
op|']'
op|','
nl|'\n'
string|"'aRecord'"
op|':'
op|'['
name|'address'
op|']'
op|','
nl|'\n'
string|"'associatedDomain'"
op|':'
op|'['
name|'self'
op|'.'
name|'_qualify'
op|'('
name|'name'
op|')'
op|']'
op|','
nl|'\n'
string|"'dc'"
op|':'
op|'['
name|'name'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'add_s'
op|'('
name|'newdn'
op|','
name|'create_modlist'
op|'('
name|'attrs'
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'subentry_with_name'
op|'('
name|'name'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'update_soa'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_entry
dedent|''
name|'def'
name|'remove_entry'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'entry'
op|'='
name|'self'
op|'.'
name|'subentry_with_name'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'entry'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'entry'
op|'.'
name|'remove_name'
op|'('
name|'name'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'update_soa'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|HostEntry
dedent|''
dedent|''
name|'class'
name|'HostEntry'
op|'('
name|'DNSEntry'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'parent'
op|','
name|'tuple'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'HostEntry'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'parent'
op|'.'
name|'lobj'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'parent_entry'
op|'='
name|'parent'
newline|'\n'
name|'self'
op|'.'
name|'_set_tuple'
op|'('
name|'tuple'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'qualified_domain'
op|'='
name|'parent'
op|'.'
name|'qualified_domain'
newline|'\n'
nl|'\n'
DECL|member|remove_name
dedent|''
name|'def'
name|'remove_name'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'names'
op|'='
name|'self'
op|'.'
name|'ldap_tuple'
op|'['
number|'1'
op|']'
op|'['
string|"'associatedDomain'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'names'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'names'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
comment|'# We just have to remove the requested domain.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'modify_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|','
op|'['
op|'('
name|'ldap'
op|'.'
name|'MOD_DELETE'
op|','
string|"'associatedDomain'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'_qualify'
op|'('
name|'utf8'
op|'('
name|'name'
op|')'
op|')'
op|')'
op|']'
op|')'
newline|'\n'
name|'if'
op|'('
name|'self'
op|'.'
name|'rdn'
op|'['
number|'1'
op|']'
op|'=='
name|'name'
op|')'
op|':'
newline|'\n'
comment|'# We just removed the rdn, so we need to move this entry.'
nl|'\n'
indent|'                '
name|'names'
op|'.'
name|'remove'
op|'('
name|'self'
op|'.'
name|'_qualify'
op|'('
name|'name'
op|')'
op|')'
newline|'\n'
name|'newrdn'
op|'='
string|'"dc=%s"'
op|'%'
name|'self'
op|'.'
name|'_dequalify'
op|'('
name|'names'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'modrdn_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|','
op|'['
name|'newrdn'
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# We should delete the entire record.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'delete_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|')'
newline|'\n'
nl|'\n'
DECL|member|modify_address
dedent|''
dedent|''
name|'def'
name|'modify_address'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'names'
op|'='
name|'self'
op|'.'
name|'ldap_tuple'
op|'['
number|'1'
op|']'
op|'['
string|"'associatedDomain'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'names'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'names'
op|')'
op|'=='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'modify_s'
op|'('
name|'self'
op|'.'
name|'dn'
op|','
op|'['
op|'('
name|'ldap'
op|'.'
name|'MOD_REPLACE'
op|','
string|"'aRecord'"
op|','
nl|'\n'
op|'['
name|'utf8'
op|'('
name|'address'
op|')'
op|']'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'remove_name'
op|'('
name|'name'
op|')'
newline|'\n'
name|'parent'
op|'.'
name|'add_entry'
op|'('
name|'name'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_names
dedent|''
dedent|''
name|'def'
name|'_names'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'names'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'domain'
name|'in'
name|'self'
op|'.'
name|'ldap_tuple'
op|'['
number|'1'
op|']'
op|'['
string|"'associatedDomain'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'names'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'_dequalify'
op|'('
name|'domain'
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'names'
newline|'\n'
DECL|variable|names
dedent|''
name|'names'
op|'='
name|'property'
op|'('
name|'_names'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_ip
name|'def'
name|'_ip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ip'
op|'='
name|'self'
op|'.'
name|'ldap_tuple'
op|'['
number|'1'
op|']'
op|'['
string|"'aRecord'"
op|']'
op|'['
number|'0'
op|']'
newline|'\n'
name|'return'
name|'ip'
newline|'\n'
DECL|variable|ip
dedent|''
name|'ip'
op|'='
name|'property'
op|'('
name|'_ip'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_parent
name|'def'
name|'_parent'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
op|'.'
name|'parent_entry'
newline|'\n'
DECL|variable|parent
dedent|''
name|'parent'
op|'='
name|'property'
op|'('
name|'_parent'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LdapDNS
dedent|''
name|'class'
name|'LdapDNS'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Driver for PowerDNS using ldap as a back end.\n\n       This driver assumes ldap-method=strict, with all domains\n       in the top-level, aRecords only."""'
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
name|'lobj'
op|'='
name|'ldap'
op|'.'
name|'initialize'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_url'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'simple_bind_s'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_user'
op|','
nl|'\n'
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_password'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_domains
dedent|''
name|'def'
name|'get_domains'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'DomainEntry'
op|'.'
name|'_get_all_domains'
op|'('
name|'self'
op|'.'
name|'lobj'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_entry
dedent|''
name|'def'
name|'create_entry'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'address'
op|','
name|'type'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'type'
op|'.'
name|'lower'
op|'('
op|')'
op|'!='
string|"'a'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'InvalidInput'
op|'('
name|'_'
op|'('
string|'"This driver only supports "'
nl|'\n'
string|'"type \'a\' entries."'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'dEntry'
op|'='
name|'DomainEntry'
op|'('
name|'self'
op|'.'
name|'lobj'
op|','
name|'domain'
op|')'
newline|'\n'
name|'dEntry'
op|'.'
name|'add_entry'
op|'('
name|'name'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_entry
dedent|''
name|'def'
name|'delete_entry'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dEntry'
op|'='
name|'DomainEntry'
op|'('
name|'self'
op|'.'
name|'lobj'
op|','
name|'domain'
op|')'
newline|'\n'
name|'dEntry'
op|'.'
name|'remove_entry'
op|'('
name|'name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_entries_by_address
dedent|''
name|'def'
name|'get_entries_by_address'
op|'('
name|'self'
op|','
name|'address'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'dEntry'
op|'='
name|'DomainEntry'
op|'('
name|'self'
op|'.'
name|'lobj'
op|','
name|'domain'
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
op|'['
op|']'
newline|'\n'
dedent|''
name|'entries'
op|'='
name|'dEntry'
op|'.'
name|'subentries_with_ip'
op|'('
name|'address'
op|')'
newline|'\n'
name|'names'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'entry'
name|'in'
name|'entries'
op|':'
newline|'\n'
indent|'            '
name|'names'
op|'.'
name|'extend'
op|'('
name|'entry'
op|'.'
name|'names'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'names'
newline|'\n'
nl|'\n'
DECL|member|get_entries_by_name
dedent|''
name|'def'
name|'get_entries_by_name'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'dEntry'
op|'='
name|'DomainEntry'
op|'('
name|'self'
op|'.'
name|'lobj'
op|','
name|'domain'
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
op|'['
op|']'
newline|'\n'
dedent|''
name|'nEntry'
op|'='
name|'dEntry'
op|'.'
name|'subentry_with_name'
op|'('
name|'name'
op|')'
newline|'\n'
name|'if'
name|'nEntry'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'['
name|'nEntry'
op|'.'
name|'ip'
op|']'
newline|'\n'
nl|'\n'
DECL|member|modify_address
dedent|''
dedent|''
name|'def'
name|'modify_address'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'address'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dEntry'
op|'='
name|'DomainEntry'
op|'('
name|'self'
op|'.'
name|'lobj'
op|','
name|'domain'
op|')'
newline|'\n'
name|'nEntry'
op|'='
name|'dEntry'
op|'.'
name|'subentry_with_name'
op|'('
name|'name'
op|')'
newline|'\n'
name|'nEntry'
op|'.'
name|'modify_address'
op|'('
name|'name'
op|','
name|'address'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_domain
dedent|''
name|'def'
name|'create_domain'
op|'('
name|'self'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'DomainEntry'
op|'.'
name|'create_domain'
op|'('
name|'self'
op|'.'
name|'lobj'
op|','
name|'domain'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_domain
dedent|''
name|'def'
name|'delete_domain'
op|'('
name|'self'
op|','
name|'domain'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dEntry'
op|'='
name|'DomainEntry'
op|'('
name|'self'
op|'.'
name|'lobj'
op|','
name|'domain'
op|')'
newline|'\n'
name|'dEntry'
op|'.'
name|'delete'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_dns_file
dedent|''
name|'def'
name|'delete_dns_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'warn'
op|'('
string|'"This shouldn\'t be getting called except during testing."'
op|')'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeLdapDNS
dedent|''
dedent|''
name|'class'
name|'FakeLdapDNS'
op|'('
name|'LdapDNS'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""For testing purposes, a DNS driver backed with a fake ldap driver."""'
newline|'\n'
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
name|'lobj'
op|'='
name|'fakeldap'
op|'.'
name|'FakeLDAP'
op|'('
op|')'
newline|'\n'
name|'attrs'
op|'='
op|'{'
string|"'objectClass'"
op|':'
op|'['
string|"'domainrelatedobject'"
op|','
string|"'dnsdomain'"
op|','
nl|'\n'
string|"'domain'"
op|','
string|"'dcobject'"
op|','
string|"'top'"
op|']'
op|','
nl|'\n'
string|"'associateddomain'"
op|':'
op|'['
string|"'root'"
op|']'
op|','
nl|'\n'
string|"'dc'"
op|':'
op|'['
string|"'root'"
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'lobj'
op|'.'
name|'add_s'
op|'('
name|'flags'
op|'.'
name|'FLAGS'
op|'.'
name|'ldap_dns_base_dn'
op|','
name|'create_modlist'
op|'('
name|'attrs'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
