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
name|'json'
newline|'\n'
name|'import'
name|'stubout'
newline|'\n'
name|'import'
name|'unittest'
newline|'\n'
name|'import'
name|'webob'
newline|'\n'
name|'import'
name|'os'
op|'.'
name|'path'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
name|'import'
name|'openstack'
newline|'\n'
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
name|'flavors'
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
name|'import'
name|'nova'
op|'.'
name|'wsgi'
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
DECL|variable|response_body
name|'response_body'
op|'='
string|'"Try to say this Mr. Knox, sir..."'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StubController
name|'class'
name|'StubController'
op|'('
name|'nova'
op|'.'
name|'wsgi'
op|'.'
name|'Controller'
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
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'body'
op|'='
name|'body'
newline|'\n'
nl|'\n'
DECL|member|index
dedent|''
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
name|'return'
name|'self'
op|'.'
name|'body'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|StubExtensionManager
dedent|''
dedent|''
name|'class'
name|'StubExtensionManager'
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
name|'resource_ext'
op|'='
name|'None'
op|','
name|'action_ext'
op|'='
name|'None'
op|','
name|'response_ext'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'resource_ext'
op|'='
name|'resource_ext'
newline|'\n'
name|'self'
op|'.'
name|'action_ext'
op|'='
name|'action_ext'
newline|'\n'
name|'self'
op|'.'
name|'response_ext'
op|'='
name|'response_ext'
newline|'\n'
nl|'\n'
DECL|member|get_name
dedent|''
name|'def'
name|'get_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Tweedle Beetle Extension"'
newline|'\n'
nl|'\n'
DECL|member|get_alias
dedent|''
name|'def'
name|'get_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"TWDLBETL"'
newline|'\n'
nl|'\n'
DECL|member|get_description
dedent|''
name|'def'
name|'get_description'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"Provides access to Tweedle Beetles"'
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
name|'resource_exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'resource_ext'
op|':'
newline|'\n'
indent|'            '
name|'resource_exts'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'resource_ext'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'resource_exts'
newline|'\n'
nl|'\n'
DECL|member|get_actions
dedent|''
name|'def'
name|'get_actions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'action_exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'action_ext'
op|':'
newline|'\n'
indent|'            '
name|'action_exts'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'action_ext'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'action_exts'
newline|'\n'
nl|'\n'
DECL|member|get_response_extensions
dedent|''
name|'def'
name|'get_response_extensions'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response_exts'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'response_ext'
op|':'
newline|'\n'
indent|'            '
name|'response_exts'
op|'.'
name|'append'
op|'('
name|'self'
op|'.'
name|'response_ext'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'response_exts'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionControllerTest
dedent|''
dedent|''
name|'class'
name|'ExtensionControllerTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_index
indent|'    '
name|'def'
name|'test_index'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'openstack'
op|'.'
name|'APIRouter'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/extensions"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_by_alias
dedent|''
name|'def'
name|'test_get_by_alias'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'openstack'
op|'.'
name|'APIRouter'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/extensions/FOXNSOX"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResourceExtensionTest
dedent|''
dedent|''
name|'class'
name|'ResourceExtensionTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_no_extension_present
indent|'    '
name|'def'
name|'test_no_extension_present'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'manager'
op|'='
name|'StubExtensionManager'
op|'('
name|'None'
op|')'
newline|'\n'
name|'app'
op|'='
name|'openstack'
op|'.'
name|'APIRouter'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|','
name|'manager'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/blah"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_resources
dedent|''
name|'def'
name|'test_get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res_ext'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'tweedles'"
op|','
nl|'\n'
name|'StubController'
op|'('
name|'response_body'
op|')'
op|')'
newline|'\n'
name|'manager'
op|'='
name|'StubExtensionManager'
op|'('
name|'res_ext'
op|')'
newline|'\n'
name|'app'
op|'='
name|'openstack'
op|'.'
name|'APIRouter'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|','
name|'manager'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/tweedles"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response_body'
op|','
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_resources_with_controller
dedent|''
name|'def'
name|'test_get_resources_with_controller'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'res_ext'
op|'='
name|'extensions'
op|'.'
name|'ResourceExtension'
op|'('
string|"'tweedles'"
op|','
nl|'\n'
name|'StubController'
op|'('
name|'response_body'
op|')'
op|')'
newline|'\n'
name|'manager'
op|'='
name|'StubExtensionManager'
op|'('
name|'res_ext'
op|')'
newline|'\n'
name|'app'
op|'='
name|'openstack'
op|'.'
name|'APIRouter'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|','
name|'manager'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/tweedles"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response_body'
op|','
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtensionManagerTest
dedent|''
dedent|''
name|'class'
name|'ExtensionManagerTest'
op|'('
name|'unittest'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|variable|response_body
indent|'    '
name|'response_body'
op|'='
string|'"Try to say this Mr. Knox, sir..."'
newline|'\n'
nl|'\n'
DECL|member|setUp
name|'def'
name|'setUp'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'FLAGS'
op|'.'
name|'osapi_extensions_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
nl|'\n'
string|'"extensions"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_resources
dedent|''
name|'def'
name|'test_get_resources'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'openstack'
op|'.'
name|'APIRouter'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/foxnsocks"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response_body'
op|','
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ActionExtensionTest
dedent|''
dedent|''
name|'class'
name|'ActionExtensionTest'
op|'('
name|'unittest'
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
name|'FLAGS'
op|'.'
name|'osapi_extensions_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'__file__'
op|')'
op|','
nl|'\n'
string|'"extensions"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_send_server_action_request
dedent|''
name|'def'
name|'_send_server_action_request'
op|'('
name|'self'
op|','
name|'url'
op|','
name|'body'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'app'
op|'='
name|'openstack'
op|'.'
name|'APIRouter'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
name|'url'
op|')'
newline|'\n'
name|'request'
op|'.'
name|'method'
op|'='
string|"'POST'"
newline|'\n'
name|'request'
op|'.'
name|'content_type'
op|'='
string|"'application/json'"
newline|'\n'
name|'request'
op|'.'
name|'body'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'body'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'return'
name|'response'
newline|'\n'
nl|'\n'
DECL|member|test_extended_action
dedent|''
name|'def'
name|'test_extended_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'add_tweedle'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_send_server_action_request'
op|'('
string|'"/servers/1/action"'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Tweedle Beetle Added."'
op|','
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
name|'body'
op|'='
name|'dict'
op|'('
name|'delete_tweedle'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_send_server_action_request'
op|'('
string|'"/servers/1/action"'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Tweedle Beetle Deleted."'
op|','
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_action_body
dedent|''
name|'def'
name|'test_invalid_action_body'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'blah'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
comment|"# Doesn't exist"
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_send_server_action_request'
op|'('
string|'"/servers/1/action"'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'501'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_invalid_action
dedent|''
name|'def'
name|'test_invalid_action'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'body'
op|'='
name|'dict'
op|'('
name|'blah'
op|'='
name|'dict'
op|'('
name|'name'
op|'='
string|'"test"'
op|')'
op|')'
newline|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_send_server_action_request'
op|'('
string|'"/asdf/1/action"'
op|','
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'404'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ResponseExtensionTest
dedent|''
dedent|''
name|'class'
name|'ResponseExtensionTest'
op|'('
name|'unittest'
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
name|'ResponseExtensionTest'
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
op|'='
name|'stubout'
op|'.'
name|'StubOutForTesting'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthManager'
op|'.'
name|'reset_fake_data'
op|'('
op|')'
newline|'\n'
name|'fakes'
op|'.'
name|'FakeAuthDatabase'
op|'.'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fakes'
op|'.'
name|'stub_out_auth'
op|'('
name|'self'
op|'.'
name|'stubs'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_resources_with_stub_mgr
dedent|''
name|'def'
name|'test_get_resources_with_stub_mgr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'test_resp'
op|'='
string|'"Gooey goo for chewy chewing!"'
newline|'\n'
nl|'\n'
DECL|function|_resp_handler
name|'def'
name|'_resp_handler'
op|'('
name|'res'
op|')'
op|':'
newline|'\n'
comment|'# only handle JSON responses'
nl|'\n'
indent|'            '
name|'data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'res'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'data'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'googoose'"
op|']'
op|'='
name|'test_resp'
newline|'\n'
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
name|'resp_ext'
op|'='
name|'extensions'
op|'.'
name|'ResponseExtension'
op|'('
string|"'GET'"
op|','
nl|'\n'
string|"'/v1.0/flavors/:(id)'"
op|','
nl|'\n'
name|'_resp_handler'
op|')'
newline|'\n'
nl|'\n'
name|'manager'
op|'='
name|'StubExtensionManager'
op|'('
name|'None'
op|','
name|'None'
op|','
name|'resp_ext'
op|')'
newline|'\n'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|','
name|'manager'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/v1.0/flavors/1"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'response_data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_resp'
op|','
name|'response_data'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'googoose'"
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_resources_with_mgr
dedent|''
name|'def'
name|'test_get_resources_with_mgr'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'        '
name|'test_resp'
op|'='
string|'"Gooey goo for chewy chewing!"'
newline|'\n'
nl|'\n'
name|'app'
op|'='
name|'fakes'
op|'.'
name|'wsgi_app'
op|'('
op|')'
newline|'\n'
name|'ext_midware'
op|'='
name|'extensions'
op|'.'
name|'ExtensionMiddleware'
op|'('
name|'app'
op|')'
newline|'\n'
name|'request'
op|'='
name|'webob'
op|'.'
name|'Request'
op|'.'
name|'blank'
op|'('
string|'"/v1.0/flavors/1"'
op|')'
newline|'\n'
name|'response'
op|'='
name|'request'
op|'.'
name|'get_response'
op|'('
name|'ext_midware'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
number|'200'
op|','
name|'response'
op|'.'
name|'status_int'
op|')'
newline|'\n'
name|'response_data'
op|'='
name|'json'
op|'.'
name|'loads'
op|'('
name|'response'
op|'.'
name|'body'
op|')'
newline|'\n'
name|'print'
name|'response_data'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'test_resp'
op|','
name|'response_data'
op|'['
string|"'flavor'"
op|']'
op|'['
string|"'googoose'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"Pig Bands!"'
op|','
name|'response_data'
op|'['
string|"'big_bands'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
