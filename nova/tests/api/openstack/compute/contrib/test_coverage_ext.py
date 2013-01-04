begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2012 IBM'
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
name|'telnetlib'
newline|'\n'
nl|'\n'
name|'from'
name|'coverage'
name|'import'
name|'coverage'
newline|'\n'
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
op|'.'
name|'compute'
op|'.'
name|'contrib'
name|'import'
name|'coverage_ext'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'jsonutils'
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
DECL|function|fake_telnet
name|'def'
name|'fake_telnet'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_check_coverage
dedent|''
name|'def'
name|'fake_check_coverage'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_xml_report
dedent|''
name|'def'
name|'fake_xml_report'
op|'('
name|'self'
op|','
name|'outfile'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_report
dedent|''
name|'def'
name|'fake_report'
op|'('
name|'self'
op|','
name|'file'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CoverageExtensionTest
dedent|''
name|'class'
name|'CoverageExtensionTest'
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
name|'CoverageExtensionTest'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'telnetlib'
op|'.'
name|'Telnet'
op|','
string|"'write'"
op|','
name|'fake_telnet'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'telnetlib'
op|'.'
name|'Telnet'
op|','
string|"'expect'"
op|','
name|'fake_telnet'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'coverage'
op|','
string|"'report'"
op|','
name|'fake_report'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'coverage'
op|','
string|"'xml_report'"
op|','
name|'fake_xml_report'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'admin_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fakeadmin_0'"
op|','
nl|'\n'
string|"'fake'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'user_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fakeadmin_0'"
op|','
nl|'\n'
string|"'fake'"
op|','
nl|'\n'
name|'is_admin'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_not_admin
dedent|''
name|'def'
name|'test_not_admin'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'start'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'user_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'403'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_start_coverage_action
dedent|''
name|'def'
name|'test_start_coverage_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'start'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_coverage_action
dedent|''
name|'def'
name|'test_stop_coverage_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'coverage_ext'
op|'.'
name|'CoverageController'
op|','
nl|'\n'
string|"'_check_coverage'"
op|','
name|'fake_check_coverage'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'stop'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'path'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_coverage_action_file
dedent|''
name|'def'
name|'test_report_coverage_action_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'coverage_ext'
op|'.'
name|'CoverageController'
op|','
nl|'\n'
string|"'_check_coverage'"
op|','
name|'fake_check_coverage'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'test_start_coverage_action'
op|'('
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'report'"
op|':'
op|'{'
nl|'\n'
string|"'file'"
op|':'
string|"'coverage-unit-test.report'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'path'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'coverage-unit-test.report'"
name|'in'
name|'resp_dict'
op|'['
string|"'path'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_coverage_action_xml_file
dedent|''
name|'def'
name|'test_report_coverage_action_xml_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'coverage_ext'
op|'.'
name|'CoverageController'
op|','
nl|'\n'
string|"'_check_coverage'"
op|','
name|'fake_check_coverage'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'report'"
op|':'
op|'{'
nl|'\n'
string|"'file'"
op|':'
string|"'coverage-xml-unit-test.report'"
op|','
nl|'\n'
string|"'xml'"
op|':'
string|"'True'"
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'resp_dict'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'path'"
name|'in'
name|'resp_dict'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
string|"'coverage-xml-unit-test.report'"
name|'in'
name|'resp_dict'
op|'['
string|"'path'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_coverage_action_nofile
dedent|''
name|'def'
name|'test_report_coverage_action_nofile'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'coverage_ext'
op|'.'
name|'CoverageController'
op|','
nl|'\n'
string|"'_check_coverage'"
op|','
name|'fake_check_coverage'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'report'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_coverage_bad_body
dedent|''
name|'def'
name|'test_coverage_bad_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_coverage_report_bad_path
dedent|''
name|'def'
name|'test_coverage_report_bad_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'coverage_ext'
op|'.'
name|'CoverageController'
op|','
nl|'\n'
string|"'_check_coverage'"
op|','
name|'fake_check_coverage'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
nl|'\n'
string|"'report'"
op|':'
op|'{'
nl|'\n'
string|"'file'"
op|':'
string|"'/tmp/coverage-xml-unit-test.report'"
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'400'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_stop_coverage_action_nostart
dedent|''
name|'def'
name|'test_stop_coverage_action_nostart'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'stop'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_report_coverage_action_nostart
dedent|''
name|'def'
name|'test_report_coverage_action_nostart'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'report'"
op|':'
op|'{'
op|'}'
op|'}'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/os-coverage/action'"
op|')'
newline|'\n'
name|'req'
op|'.'
name|'method'
op|'='
string|'"POST"'
newline|'\n'
name|'req'
op|'.'
name|'body'
op|'='
name|'jsonutils'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'req'
op|'.'
name|'headers'
op|'['
string|'"content-type"'
op|']'
op|'='
string|'"application/json"'
newline|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
nl|'\n'
name|'fake_auth_context'
op|'='
name|'self'
op|'.'
name|'admin_context'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'404'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
