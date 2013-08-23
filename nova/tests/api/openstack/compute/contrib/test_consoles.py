begin_unit
comment|'# Copyright 2012 OpenStack Foundation'
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
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'api'
name|'as'
name|'compute_api'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
DECL|function|fake_get_vnc_console
name|'def'
name|'fake_get_vnc_console'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'_instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'url'"
op|':'
string|"'http://fake'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_spice_console
dedent|''
name|'def'
name|'fake_get_spice_console'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'_instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'url'"
op|':'
string|"'http://fake'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_rdp_console
dedent|''
name|'def'
name|'fake_get_rdp_console'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'_instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'url'"
op|':'
string|"'http://fake'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_vnc_console_invalid_type
dedent|''
name|'def'
name|'fake_get_vnc_console_invalid_type'
op|'('
name|'self'
op|','
name|'_context'
op|','
nl|'\n'
name|'_instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'ConsoleTypeInvalid'
op|'('
name|'console_type'
op|'='
name|'_console_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_spice_console_invalid_type
dedent|''
name|'def'
name|'fake_get_spice_console_invalid_type'
op|'('
name|'self'
op|','
name|'_context'
op|','
nl|'\n'
name|'_instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'ConsoleTypeInvalid'
op|'('
name|'console_type'
op|'='
name|'_console_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_rdp_console_invalid_type
dedent|''
name|'def'
name|'fake_get_rdp_console_invalid_type'
op|'('
name|'self'
op|','
name|'_context'
op|','
nl|'\n'
name|'_instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'ConsoleTypeInvalid'
op|'('
name|'console_type'
op|'='
name|'_console_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_vnc_console_not_ready
dedent|''
name|'def'
name|'fake_get_vnc_console_not_ready'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotReady'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_spice_console_not_ready
dedent|''
name|'def'
name|'fake_get_spice_console_not_ready'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotReady'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_rdp_console_not_ready
dedent|''
name|'def'
name|'fake_get_rdp_console_not_ready'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotReady'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_vnc_console_not_found
dedent|''
name|'def'
name|'fake_get_vnc_console_not_found'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_spice_console_not_found
dedent|''
name|'def'
name|'fake_get_spice_console_not_found'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_rdp_console_not_found
dedent|''
name|'def'
name|'fake_get_rdp_console_not_found'
op|'('
name|'self'
op|','
name|'_context'
op|','
name|'instance'
op|','
name|'_console_type'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance'
op|'['
string|'"uuid"'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get
dedent|''
name|'def'
name|'fake_get'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'want_objects'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'instance_uuid'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fake_get_not_found
dedent|''
name|'def'
name|'fake_get_not_found'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'instance_uuid'
op|','
name|'want_objects'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'raise'
name|'exception'
op|'.'
name|'InstanceNotFound'
op|'('
name|'instance_id'
op|'='
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsolesExtensionTest
dedent|''
name|'class'
name|'ConsolesExtensionTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'ConsolesExtensionTest'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_vnc_console'"
op|','
nl|'\n'
name|'fake_get_vnc_console'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_spice_console'"
op|','
nl|'\n'
name|'fake_get_spice_console'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_rdp_console'"
op|','
nl|'\n'
name|'fake_get_rdp_console'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
nl|'\n'
name|'osapi_compute_extension'
op|'='
op|'['
nl|'\n'
string|"'nova.api.openstack.compute.contrib.select_extensions'"
op|']'
op|','
nl|'\n'
name|'osapi_compute_ext_list'
op|'='
op|'['
string|"'Consoles'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
name|'init_only'
op|'='
op|'('
string|"'servers'"
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vnc_console
dedent|''
name|'def'
name|'test_get_vnc_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'os-getVNCConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'novnc'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
nl|'\n'
op|'{'
string|"u'console'"
op|':'
op|'{'
string|"u'url'"
op|':'
string|"u'http://fake'"
op|','
string|"u'type'"
op|':'
string|"u'novnc'"
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vnc_console_not_ready
dedent|''
name|'def'
name|'test_get_vnc_console_not_ready'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_vnc_console'"
op|','
nl|'\n'
name|'fake_get_vnc_console_not_ready'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getVNCConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'novnc'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'409'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_vnc_console_no_type
dedent|''
name|'def'
name|'test_get_vnc_console_no_type'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_vnc_console'"
op|','
nl|'\n'
name|'fake_get_vnc_console_invalid_type'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getVNCConsole'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_vnc_console_no_instance
dedent|''
name|'def'
name|'test_get_vnc_console_no_instance'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get_not_found'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getVNCConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'novnc'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_vnc_console_no_instance_on_console_get
dedent|''
name|'def'
name|'test_get_vnc_console_no_instance_on_console_get'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_vnc_console'"
op|','
nl|'\n'
name|'fake_get_vnc_console_not_found'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getVNCConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'novnc'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_vnc_console_invalid_type
dedent|''
name|'def'
name|'test_get_vnc_console_invalid_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'os-getVNCConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'invalid'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_vnc_console'"
op|','
nl|'\n'
name|'fake_get_vnc_console_invalid_type'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_vnc_console_not_implemented
dedent|''
name|'def'
name|'test_get_vnc_console_not_implemented'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_vnc_console'"
op|','
nl|'\n'
name|'fakes'
op|'.'
name|'fake_not_implemented'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getVNCConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'novnc'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
number|'501'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_spice_console
dedent|''
name|'def'
name|'test_get_spice_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'os-getSPICEConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'spice-html5'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
nl|'\n'
op|'{'
string|"u'console'"
op|':'
op|'{'
string|"u'url'"
op|':'
string|"u'http://fake'"
op|','
string|"u'type'"
op|':'
string|"u'spice-html5'"
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_spice_console_not_ready
dedent|''
name|'def'
name|'test_get_spice_console_not_ready'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_spice_console'"
op|','
nl|'\n'
name|'fake_get_spice_console_not_ready'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getSPICEConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'spice-html5'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'409'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_spice_console_no_type
dedent|''
name|'def'
name|'test_get_spice_console_no_type'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_spice_console'"
op|','
nl|'\n'
name|'fake_get_spice_console_invalid_type'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getSPICEConsole'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_spice_console_no_instance
dedent|''
name|'def'
name|'test_get_spice_console_no_instance'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get_not_found'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getSPICEConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'spice-html5'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_spice_console_no_instance_on_console_get
dedent|''
name|'def'
name|'test_get_spice_console_no_instance_on_console_get'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_spice_console'"
op|','
nl|'\n'
name|'fake_get_spice_console_not_found'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getSPICEConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'spice-html5'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_spice_console_invalid_type
dedent|''
name|'def'
name|'test_get_spice_console_invalid_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'os-getSPICEConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'invalid'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_spice_console'"
op|','
nl|'\n'
name|'fake_get_spice_console_invalid_type'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_rdp_console
dedent|''
name|'def'
name|'test_get_rdp_console'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'os-getRDPConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'rdp-html5'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'200'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'output'
op|','
nl|'\n'
op|'{'
string|"u'console'"
op|':'
op|'{'
string|"u'url'"
op|':'
string|"u'http://fake'"
op|','
string|"u'type'"
op|':'
string|"u'rdp-html5'"
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_rdp_console_not_ready
dedent|''
name|'def'
name|'test_get_rdp_console_not_ready'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_rdp_console'"
op|','
nl|'\n'
name|'fake_get_rdp_console_not_ready'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getRDPConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'rdp-html5'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
op|')'
newline|'\n'
name|'output'
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
name|'assertEqual'
op|'('
name|'res'
op|'.'
name|'status_int'
op|','
number|'409'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_rdp_console_no_type
dedent|''
name|'def'
name|'test_get_rdp_console_no_type'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_rdp_console'"
op|','
nl|'\n'
name|'fake_get_rdp_console_invalid_type'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getRDPConsole'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_rdp_console_no_instance
dedent|''
name|'def'
name|'test_get_rdp_console_no_instance'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get'"
op|','
name|'fake_get_not_found'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getRDPConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'rdp-html5'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_rdp_console_no_instance_on_console_get
dedent|''
name|'def'
name|'test_get_rdp_console_no_instance_on_console_get'
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
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_rdp_console'"
op|','
nl|'\n'
name|'fake_get_rdp_console_not_found'
op|')'
newline|'\n'
name|'body'
op|'='
op|'{'
string|"'os-getRDPConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'rdp-html5'"
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
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
DECL|member|test_get_rdp_console_invalid_type
dedent|''
name|'def'
name|'test_get_rdp_console_invalid_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
op|'{'
string|"'os-getRDPConsole'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'invalid'"
op|'}'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'compute_api'
op|'.'
name|'API'
op|','
string|"'get_rdp_console'"
op|','
nl|'\n'
name|'fake_get_rdp_console_invalid_type'
op|')'
newline|'\n'
name|'req'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|"'/v2/fake/servers/1/action'"
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
nl|'\n'
name|'res'
op|'='
name|'req'
op|'.'
name|'get_response'
op|'('
name|'self'
op|'.'
name|'app'
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
dedent|''
dedent|''
endmarker|''
end_unit
