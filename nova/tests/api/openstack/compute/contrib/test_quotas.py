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
name|'webob'
newline|'\n'
name|'from'
name|'lxml'
name|'import'
name|'etree'
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
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'quotas'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'fakes'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|quota_set
name|'def'
name|'quota_set'
op|'('
name|'id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'quota_set'"
op|':'
op|'{'
string|"'id'"
op|':'
name|'id'
op|','
string|"'metadata_items'"
op|':'
number|'128'
op|','
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
string|"'ram'"
op|':'
number|'51200'
op|','
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'instances'"
op|':'
number|'10'
op|','
string|"'injected_files'"
op|':'
number|'5'
op|','
string|"'cores'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|quota_set_list
dedent|''
name|'def'
name|'quota_set_list'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'quota_set_list'"
op|':'
op|'['
name|'quota_set'
op|'('
string|"'1234'"
op|')'
op|','
name|'quota_set'
op|'('
string|"'5678'"
op|')'
op|','
nl|'\n'
name|'quota_set'
op|'('
string|"'update_me'"
op|')'
op|']'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaSetsTest
dedent|''
name|'class'
name|'QuotaSetsTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'QuotaSetsTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'quotas'
op|'.'
name|'QuotaSetsController'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_format_quota_set
dedent|''
name|'def'
name|'test_format_quota_set'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raw_quota_set'
op|'='
op|'{'
nl|'\n'
string|"'instances'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'cores'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
nl|'\n'
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
number|'128'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|'}'
newline|'\n'
nl|'\n'
name|'quota_set'
op|'='
name|'quotas'
op|'.'
name|'QuotaSetsController'
op|'('
op|')'
op|'.'
name|'_format_quota_set'
op|'('
string|"'1234'"
op|','
nl|'\n'
name|'raw_quota_set'
op|')'
newline|'\n'
name|'qs'
op|'='
name|'quota_set'
op|'['
string|"'quota_set'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'id'"
op|']'
op|','
string|"'1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'instances'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'cores'"
op|']'
op|','
number|'20'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'ram'"
op|']'
op|','
number|'51200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'volumes'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'gigabytes'"
op|']'
op|','
number|'1000'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'floating_ips'"
op|']'
op|','
number|'10'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'metadata_items'"
op|']'
op|','
number|'128'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'injected_files'"
op|']'
op|','
number|'5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'qs'
op|'['
string|"'injected_file_content_bytes'"
op|']'
op|','
number|'10240'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_defaults
dedent|''
name|'def'
name|'test_quotas_defaults'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'uri'
op|'='
string|"'/v2/fake_tenant/os-quota-sets/fake_tenant/defaults'"
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
name|'uri'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'defaults'
op|'('
name|'req'
op|','
string|"'fake_tenant'"
op|')'
newline|'\n'
nl|'\n'
name|'expected'
op|'='
op|'{'
string|"'quota_set'"
op|':'
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'fake_tenant'"
op|','
nl|'\n'
string|"'instances'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'cores'"
op|':'
number|'20'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
nl|'\n'
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
nl|'\n'
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
number|'128'
op|','
nl|'\n'
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'expected'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_show_as_admin
dedent|''
name|'def'
name|'test_quotas_show_as_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake4/os-quota-sets/1234'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|'('
name|'req'
op|','
number|'1234'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'quota_set'
op|'('
string|"'1234'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_show_as_unauthorized_user
dedent|''
name|'def'
name|'test_quotas_show_as_unauthorized_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake4/os-quota-sets/1234'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'show'
op|','
nl|'\n'
name|'req'
op|','
number|'1234'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_as_admin
dedent|''
name|'def'
name|'test_quotas_update_as_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'quota_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
number|'50'
op|','
string|"'cores'"
op|':'
number|'50'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
number|'128'
op|','
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake4/os-quota-sets/update_me'"
op|','
nl|'\n'
name|'use_admin_context'
op|'='
name|'True'
op|')'
newline|'\n'
name|'res_dict'
op|'='
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|'('
name|'req'
op|','
string|"'update_me'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res_dict'
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_quotas_update_as_user
dedent|''
name|'def'
name|'test_quotas_update_as_user'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'quota_set'"
op|':'
op|'{'
string|"'instances'"
op|':'
number|'50'
op|','
string|"'cores'"
op|':'
number|'50'
op|','
nl|'\n'
string|"'ram'"
op|':'
number|'51200'
op|','
string|"'volumes'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'gigabytes'"
op|':'
number|'1000'
op|','
string|"'floating_ips'"
op|':'
number|'10'
op|','
nl|'\n'
string|"'metadata_items'"
op|':'
number|'128'
op|','
string|"'injected_files'"
op|':'
number|'5'
op|','
nl|'\n'
string|"'injected_file_content_bytes'"
op|':'
number|'10240'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
name|'req'
op|'='
name|'fakes'
op|'.'
name|'HTTPRequest'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake4/os-quota-sets/update_me'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPForbidden'
op|','
name|'self'
op|'.'
name|'controller'
op|'.'
name|'update'
op|','
nl|'\n'
name|'req'
op|','
string|"'update_me'"
op|','
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|QuotaXMLSerializerTest
dedent|''
dedent|''
name|'class'
name|'QuotaXMLSerializerTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|setUp
indent|'    '
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'QuotaXMLSerializerTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'serializer'
op|'='
name|'quotas'
op|'.'
name|'QuotaTemplate'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'deserializer'
op|'='
name|'wsgi'
op|'.'
name|'XMLDeserializer'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_serializer
dedent|''
name|'def'
name|'test_serializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'quota_set'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'id'
op|'='
string|"'project_id'"
op|','
nl|'\n'
name|'metadata_items'
op|'='
number|'10'
op|','
nl|'\n'
name|'injected_file_content_bytes'
op|'='
number|'20'
op|','
nl|'\n'
name|'volumes'
op|'='
number|'30'
op|','
nl|'\n'
name|'gigabytes'
op|'='
number|'40'
op|','
nl|'\n'
name|'ram'
op|'='
number|'50'
op|','
nl|'\n'
name|'floating_ips'
op|'='
number|'60'
op|','
nl|'\n'
name|'instances'
op|'='
number|'70'
op|','
nl|'\n'
name|'injected_files'
op|'='
number|'80'
op|','
nl|'\n'
name|'cores'
op|'='
number|'90'
op|')'
op|')'
newline|'\n'
name|'text'
op|'='
name|'self'
op|'.'
name|'serializer'
op|'.'
name|'serialize'
op|'('
name|'exemplar'
op|')'
newline|'\n'
nl|'\n'
name|'print'
name|'text'
newline|'\n'
name|'tree'
op|'='
name|'etree'
op|'.'
name|'fromstring'
op|'('
name|'text'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'quota_set'"
op|','
name|'tree'
op|'.'
name|'tag'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|"'project_id'"
op|','
name|'tree'
op|'.'
name|'get'
op|'('
string|"'id'"
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'exemplar'
op|'['
string|"'quota_set'"
op|']'
op|')'
op|'-'
number|'1'
op|','
name|'len'
op|'('
name|'tree'
op|')'
op|')'
newline|'\n'
name|'for'
name|'child'
name|'in'
name|'tree'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'child'
op|'.'
name|'tag'
name|'in'
name|'exemplar'
op|'['
string|"'quota_set'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'int'
op|'('
name|'child'
op|'.'
name|'text'
op|')'
op|','
name|'exemplar'
op|'['
string|"'quota_set'"
op|']'
op|'['
name|'child'
op|'.'
name|'tag'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_deserializer
dedent|''
dedent|''
name|'def'
name|'test_deserializer'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'exemplar'
op|'='
name|'dict'
op|'('
name|'quota_set'
op|'='
name|'dict'
op|'('
nl|'\n'
name|'metadata_items'
op|'='
string|"'10'"
op|','
nl|'\n'
name|'injected_file_content_bytes'
op|'='
string|"'20'"
op|','
nl|'\n'
name|'volumes'
op|'='
string|"'30'"
op|','
nl|'\n'
name|'gigabytes'
op|'='
string|"'40'"
op|','
nl|'\n'
name|'ram'
op|'='
string|"'50'"
op|','
nl|'\n'
name|'floating_ips'
op|'='
string|"'60'"
op|','
nl|'\n'
name|'instances'
op|'='
string|"'70'"
op|','
nl|'\n'
name|'injected_files'
op|'='
string|"'80'"
op|','
nl|'\n'
name|'cores'
op|'='
string|"'90'"
op|')'
op|')'
newline|'\n'
name|'intext'
op|'='
op|'('
string|'"<?xml version=\'1.0\' encoding=\'UTF-8\'?>\\n"'
nl|'\n'
string|"'<quota_set>'"
nl|'\n'
string|"'<metadata_items>10</metadata_items>'"
nl|'\n'
string|"'<injected_file_content_bytes>20'"
nl|'\n'
string|"'</injected_file_content_bytes>'"
nl|'\n'
string|"'<volumes>30</volumes>'"
nl|'\n'
string|"'<gigabytes>40</gigabytes>'"
nl|'\n'
string|"'<ram>50</ram>'"
nl|'\n'
string|"'<floating_ips>60</floating_ips>'"
nl|'\n'
string|"'<instances>70</instances>'"
nl|'\n'
string|"'<injected_files>80</injected_files>'"
nl|'\n'
string|"'<cores>90</cores>'"
nl|'\n'
string|"'</quota_set>'"
op|')'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'self'
op|'.'
name|'deserializer'
op|'.'
name|'deserialize'
op|'('
name|'intext'
op|')'
op|'['
string|"'body'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'result'
op|','
name|'exemplar'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
