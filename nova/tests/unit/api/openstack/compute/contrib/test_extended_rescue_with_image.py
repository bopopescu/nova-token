begin_unit
comment|'#   Copyright 2014 OpenStack Foundation'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'#   not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'#   a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#       http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#   Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'#   distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'#   WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'#   License for the specific language governing permissions and limitations'
nl|'\n'
comment|'#   under the License.'
nl|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'openstack'
name|'import'
name|'common'
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
name|'legacy_v2'
op|'.'
name|'contrib'
name|'import'
name|'rescue'
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
name|'import'
name|'compute'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'context'
name|'as'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'password_length'"
op|','
string|"'nova.utils'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeRequest
name|'class'
name|'FakeRequest'
op|'('
name|'object'
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
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'environ'
op|'='
op|'{'
string|'"nova.context"'
op|':'
name|'context'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExtendedRescueWithImageTest
dedent|''
dedent|''
name|'class'
name|'ExtendedRescueWithImageTest'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
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
name|'ExtendedRescueWithImageTest'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
name|'ext_mgr'
op|'='
name|'extensions'
op|'.'
name|'ExtensionManager'
op|'('
op|')'
newline|'\n'
name|'ext_mgr'
op|'.'
name|'extensions'
op|'='
op|'{'
string|"'os-extended-rescue-with-image'"
op|':'
string|"'fake'"
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'='
name|'rescue'
op|'.'
name|'RescueController'
op|'('
name|'ext_mgr'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'common'
op|','
string|"'get_instance'"
op|','
nl|'\n'
name|'return_value'
op|'='
string|'"instance"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'compute'
op|'.'
name|'api'
op|'.'
name|'API'
op|','
string|'"rescue"'
op|')'
newline|'\n'
DECL|member|_make_rescue_request_with_image_ref
name|'def'
name|'_make_rescue_request_with_image_ref'
op|'('
name|'self'
op|','
name|'body'
op|','
name|'mock_rescue'
op|','
nl|'\n'
name|'mock_get_instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
string|'"instance"'
newline|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_get_instance'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'return_value'
op|'='
name|'instance'
op|')'
newline|'\n'
name|'fake_context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
string|"'fake'"
op|','
string|"'fake'"
op|')'
newline|'\n'
name|'req'
op|'='
name|'FakeRequest'
op|'('
name|'fake_context'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'controller'
op|'.'
name|'_rescue'
op|'('
name|'req'
op|','
string|'"id"'
op|','
name|'body'
op|')'
newline|'\n'
name|'rescue_image_ref'
op|'='
name|'body'
op|'['
string|'"rescue"'
op|']'
op|'.'
name|'get'
op|'('
string|'"rescue_image_ref"'
op|')'
newline|'\n'
name|'mock_rescue'
op|'.'
name|'assert_called_with'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
name|'mock'
op|'.'
name|'ANY'
op|','
nl|'\n'
name|'rescue_password'
op|'='
name|'mock'
op|'.'
name|'ANY'
op|','
name|'rescue_image_ref'
op|'='
name|'rescue_image_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_with_image_specified
dedent|''
name|'def'
name|'test_rescue_with_image_specified'
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
name|'rescue'
op|'='
op|'{'
string|'"rescue_image_ref"'
op|':'
string|'"image-ref"'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_make_rescue_request_with_image_ref'
op|'('
name|'body'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_rescue_without_image_specified
dedent|''
name|'def'
name|'test_rescue_without_image_specified'
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
name|'rescue'
op|'='
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_make_rescue_request_with_image_ref'
op|'('
name|'body'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
