begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#    Copyright 2010 OpenStack LLC'
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
name|'xml'
op|'.'
name|'dom'
op|'.'
name|'minidom'
name|'import'
name|'parseString'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'cloud'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'libvirt_conn'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtConnTestCase
name|'class'
name|'LibvirtConnTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|bitrot_test_get_uri_and_template
indent|'    '
name|'def'
name|'bitrot_test_get_uri_and_template'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
DECL|class|MockDataModel
indent|'        '
name|'class'
name|'MockDataModel'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
DECL|member|__getitem__
indent|'            '
name|'def'
name|'__getitem__'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'self'
op|'.'
name|'datamodel'
op|'['
name|'name'
op|']'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'datamodel'
op|'='
op|'{'
string|"'name'"
op|':'
string|"'i-cafebabe'"
op|','
nl|'\n'
string|"'memory_kb'"
op|':'
string|"'1024000'"
op|','
nl|'\n'
string|"'basepath'"
op|':'
string|"'/some/path'"
op|','
nl|'\n'
string|"'bridge_name'"
op|':'
string|"'br100'"
op|','
nl|'\n'
string|"'mac_address'"
op|':'
string|"'02:12:34:46:56:67'"
op|','
nl|'\n'
string|"'vcpus'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'None'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'type_uri_map'
op|'='
op|'{'
string|"'qemu'"
op|':'
op|'('
string|"'qemu:///system'"
op|','
nl|'\n'
op|'['
name|'lambda'
name|'s'
op|':'
string|"'<domain type=\\'qemu\\'>'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'type>hvm</type'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'emulator>/usr/bin/kvm'"
name|'not'
name|'in'
name|'s'
op|']'
op|')'
op|','
nl|'\n'
string|"'kvm'"
op|':'
op|'('
string|"'qemu:///system'"
op|','
nl|'\n'
op|'['
name|'lambda'
name|'s'
op|':'
string|"'<domain type=\\'kvm\\'>'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'type>hvm</type'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'emulator>/usr/bin/qemu<'"
name|'not'
name|'in'
name|'s'
op|']'
op|')'
op|','
nl|'\n'
string|"'uml'"
op|':'
op|'('
string|"'uml:///system'"
op|','
nl|'\n'
op|'['
name|'lambda'
name|'s'
op|':'
string|"'<domain type=\\'uml\\'>'"
name|'in'
name|'s'
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
string|"'type>uml</type'"
name|'in'
name|'s'
op|']'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'for'
op|'('
name|'libvirt_type'
op|','
op|'('
name|'expected_uri'
op|','
name|'checks'
op|')'
op|')'
name|'in'
name|'type_uri_map'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|'='
name|'libvirt_type'
newline|'\n'
DECL|variable|conn
name|'conn'
op|'='
name|'libvirt_conn'
op|'.'
name|'LibvirtConnection'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
name|'uri'
op|','
name|'template'
op|'='
name|'conn'
op|'.'
name|'get_uri_and_template'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'uri'
op|','
name|'expected_uri'
op|')'
newline|'\n'
nl|'\n'
name|'for'
name|'i'
op|','
name|'check'
name|'in'
name|'enumerate'
op|'('
name|'checks'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'xml'
op|'='
name|'conn'
op|'.'
name|'to_xml'
op|'('
name|'MockDataModel'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'check'
op|'('
name|'xml'
op|')'
op|','
string|"'%s failed check %d'"
op|'%'
op|'('
name|'xml'
op|','
name|'i'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Deliberately not just assigning this string to FLAGS.libvirt_uri and'
nl|'\n'
comment|'# checking against that later on. This way we make sure the'
nl|'\n'
comment|"# implementation doesn't fiddle around with the FLAGS."
nl|'\n'
dedent|''
dedent|''
name|'testuri'
op|'='
string|"'something completely different'"
newline|'\n'
name|'FLAGS'
op|'.'
name|'libvirt_uri'
op|'='
name|'testuri'
newline|'\n'
name|'for'
op|'('
name|'libvirt_type'
op|','
op|'('
name|'expected_uri'
op|','
name|'checks'
op|')'
op|')'
name|'in'
name|'type_uri_map'
op|'.'
name|'iteritems'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'FLAGS'
op|'.'
name|'libvirt_type'
op|'='
name|'libvirt_type'
newline|'\n'
DECL|variable|conn
name|'conn'
op|'='
name|'libvirt_conn'
op|'.'
name|'LibvirtConnection'
op|'('
name|'True'
op|')'
newline|'\n'
name|'uri'
op|','
name|'template'
op|'='
name|'conn'
op|'.'
name|'get_uri_and_template'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'uri'
op|','
name|'testuri'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NWFilterTestCase
dedent|''
dedent|''
dedent|''
name|'class'
name|'NWFilterTestCase'
op|'('
name|'test'
op|'.'
name|'TrialTestCase'
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
name|'NWFilterTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|class|Mock
name|'class'
name|'Mock'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'context'
op|'='
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'='
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'.'
name|'id'
op|'='
string|"'fake'"
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'user'
op|'.'
name|'is_superuser'
op|'='
name|'lambda'
op|':'
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project'
op|'='
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'.'
name|'project'
op|'.'
name|'id'
op|'='
string|"'fake'"
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'fake_libvirt_connection'
op|'='
name|'Mock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'fw'
op|'='
name|'libvirt_conn'
op|'.'
name|'NWFilterFirewall'
op|'('
name|'self'
op|'.'
name|'fake_libvirt_connection'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_cidr_rule_nwfilter_xml
dedent|''
name|'def'
name|'test_cidr_rule_nwfilter_xml'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cloud_controller'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'create_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'testgroup'"
op|','
nl|'\n'
string|"'test group description'"
op|')'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'authorize_security_group_ingress'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'testgroup'"
op|','
nl|'\n'
name|'from_port'
op|'='
string|"'80'"
op|','
nl|'\n'
name|'to_port'
op|'='
string|"'81'"
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'cidr_ip'
op|'='
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
name|'security_group'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
op|'{'
op|'}'
op|','
string|"'fake'"
op|','
string|"'testgroup'"
op|')'
newline|'\n'
nl|'\n'
name|'xml'
op|'='
name|'self'
op|'.'
name|'fw'
op|'.'
name|'security_group_to_nwfilter_xml'
op|'('
name|'security_group'
op|'.'
name|'id'
op|')'
newline|'\n'
nl|'\n'
name|'dom'
op|'='
name|'parseString'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'dom'
op|'.'
name|'firstChild'
op|'.'
name|'tagName'
op|','
string|"'filter'"
op|')'
newline|'\n'
nl|'\n'
name|'rules'
op|'='
name|'dom'
op|'.'
name|'getElementsByTagName'
op|'('
string|"'rule'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'rules'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
comment|"# It's supposed to allow inbound traffic."
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'action'"
op|')'
op|','
string|"'accept'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'direction'"
op|')'
op|','
string|"'in'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Must be lower priority than the base filter (which blocks everything)'
nl|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'int'
op|'('
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'priority'"
op|')'
op|')'
op|'<'
number|'1000'
op|')'
newline|'\n'
nl|'\n'
name|'ip_conditions'
op|'='
name|'rules'
op|'['
number|'0'
op|']'
op|'.'
name|'getElementsByTagName'
op|'('
string|"'tcp'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'len'
op|'('
name|'ip_conditions'
op|')'
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip_conditions'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'srcipaddr'"
op|')'
op|','
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip_conditions'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'dstportstart'"
op|')'
op|','
string|"'80'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'ip_conditions'
op|'['
number|'0'
op|']'
op|'.'
name|'getAttribute'
op|'('
string|"'dstportend'"
op|')'
op|','
string|"'81'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
name|'self'
op|'.'
name|'teardown_security_group'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|teardown_security_group
dedent|''
name|'def'
name|'teardown_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cloud_controller'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'delete_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
string|"'testgroup'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|member|setup_and_return_security_group
dedent|''
name|'def'
name|'setup_and_return_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'cloud_controller'
op|'='
name|'cloud'
op|'.'
name|'CloudController'
op|'('
op|')'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'create_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'testgroup'"
op|','
nl|'\n'
string|"'test group description'"
op|')'
newline|'\n'
name|'cloud_controller'
op|'.'
name|'authorize_security_group_ingress'
op|'('
name|'self'
op|'.'
name|'context'
op|','
nl|'\n'
string|"'testgroup'"
op|','
nl|'\n'
name|'from_port'
op|'='
string|"'80'"
op|','
nl|'\n'
name|'to_port'
op|'='
string|"'81'"
op|','
nl|'\n'
name|'ip_protocol'
op|'='
string|"'tcp'"
op|','
nl|'\n'
name|'cidr_ip'
op|'='
string|"'0.0.0.0/0'"
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'db'
op|'.'
name|'security_group_get_by_name'
op|'('
op|'{'
op|'}'
op|','
string|"'fake'"
op|','
string|"'testgroup'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_creates_base_rule_first
dedent|''
name|'def'
name|'test_creates_base_rule_first'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# These come pre-defined by libvirt'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'defined_filters'
op|'='
op|'['
string|"'no-mac-spoofing'"
op|','
nl|'\n'
string|"'no-ip-spoofing'"
op|','
nl|'\n'
string|"'no-arp-spoofing'"
op|','
nl|'\n'
string|"'allow-dhcp-server'"
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'recursive_depends'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'self'
op|'.'
name|'defined_filters'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'f'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
DECL|function|_filterDefineXMLMock
dedent|''
name|'def'
name|'_filterDefineXMLMock'
op|'('
name|'xml'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'dom'
op|'='
name|'parseString'
op|'('
name|'xml'
op|')'
newline|'\n'
name|'name'
op|'='
name|'dom'
op|'.'
name|'firstChild'
op|'.'
name|'getAttribute'
op|'('
string|"'name'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'name'
op|']'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'f'
name|'in'
name|'dom'
op|'.'
name|'getElementsByTagName'
op|'('
string|"'filterref'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ref'
op|'='
name|'f'
op|'.'
name|'getAttribute'
op|'('
string|"'filter'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ref'
name|'in'
name|'self'
op|'.'
name|'defined_filters'
op|','
nl|'\n'
op|'('
string|"'%s referenced filter that does '"
op|'+'
nl|'\n'
string|"'not yet exist: %s'"
op|')'
op|'%'
op|'('
name|'name'
op|','
name|'ref'
op|')'
op|')'
newline|'\n'
name|'dependencies'
op|'='
op|'['
name|'ref'
op|']'
op|'+'
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'ref'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'name'
op|']'
op|'+='
name|'dependencies'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'defined_filters'
op|'.'
name|'append'
op|'('
name|'name'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'fake_libvirt_connection'
op|'.'
name|'nwfilterDefineXML'
op|'='
name|'_filterDefineXMLMock'
newline|'\n'
nl|'\n'
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_create'
op|'('
op|'{'
op|'}'
op|','
op|'{'
string|"'user_id'"
op|':'
string|"'fake'"
op|','
nl|'\n'
string|"'project_id'"
op|':'
string|"'fake'"
op|'}'
op|')'
newline|'\n'
name|'inst_id'
op|'='
name|'instance_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
DECL|function|_ensure_all_called
name|'def'
name|'_ensure_all_called'
op|'('
name|'_'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'instance_filter'
op|'='
string|"'nova-instance-%s'"
op|'%'
name|'instance_ref'
op|'['
string|"'str_id'"
op|']'
newline|'\n'
name|'secgroup_filter'
op|'='
string|"'nova-secgroup-%s'"
op|'%'
name|'self'
op|'.'
name|'security_group'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'for'
name|'required'
name|'in'
op|'['
name|'secgroup_filter'
op|','
string|"'allow-dhcp-server'"
op|','
nl|'\n'
string|"'no-arp-spoofing'"
op|','
string|"'no-ip-spoofing'"
op|','
nl|'\n'
string|"'no-mac-spoofing'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'required'
name|'in'
name|'self'
op|'.'
name|'recursive_depends'
op|'['
name|'instance_filter'
op|']'
op|','
nl|'\n'
string|'"Instance\'s filter does not include %s"'
op|'%'
name|'required'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'security_group'
op|'='
name|'self'
op|'.'
name|'setup_and_return_security_group'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'db'
op|'.'
name|'instance_add_security_group'
op|'('
op|'{'
op|'}'
op|','
name|'inst_id'
op|','
name|'self'
op|'.'
name|'security_group'
op|'.'
name|'id'
op|')'
newline|'\n'
name|'instance'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
op|'{'
op|'}'
op|','
name|'inst_id'
op|')'
newline|'\n'
nl|'\n'
name|'d'
op|'='
name|'self'
op|'.'
name|'fw'
op|'.'
name|'setup_nwfilters_for_instance'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'_ensure_all_called'
op|')'
newline|'\n'
name|'d'
op|'.'
name|'addCallback'
op|'('
name|'lambda'
name|'_'
op|':'
name|'self'
op|'.'
name|'teardown_security_group'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'d'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
