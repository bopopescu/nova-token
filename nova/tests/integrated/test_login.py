begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Justin Santa Barbara'
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
name|'unittest'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'log'
name|'import'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
name|'import'
name|'integrated_helpers'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'api'
name|'import'
name|'client'
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
string|"'nova.tests.integrated'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LoginTest
name|'class'
name|'LoginTest'
op|'('
name|'integrated_helpers'
op|'.'
name|'_IntegratedTestBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_login
indent|'    '
name|'def'
name|'test_login'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Simple check - we list flavors - so we know we\'re logged in."""'
newline|'\n'
name|'flavors'
op|'='
name|'self'
op|'.'
name|'api'
op|'.'
name|'get_flavors'
op|'('
op|')'
newline|'\n'
name|'for'
name|'flavor'
name|'in'
name|'flavors'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"flavor: %s"'
op|')'
op|'%'
name|'flavor'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_login_password
dedent|''
dedent|''
name|'def'
name|'test_bad_login_password'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that I get a 401 with a bad username."""'
newline|'\n'
name|'bad_credentials_api'
op|'='
name|'client'
op|'.'
name|'TestOpenStackClient'
op|'('
name|'self'
op|'.'
name|'user'
op|'.'
name|'name'
op|','
nl|'\n'
string|'"notso_password"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'user'
op|'.'
name|'auth_url'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiAuthenticationException'
op|','
nl|'\n'
name|'bad_credentials_api'
op|'.'
name|'get_flavors'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_login_username
dedent|''
name|'def'
name|'test_bad_login_username'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that I get a 401 with a bad password."""'
newline|'\n'
name|'bad_credentials_api'
op|'='
name|'client'
op|'.'
name|'TestOpenStackClient'
op|'('
string|'"notso_username"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'user'
op|'.'
name|'secret'
op|','
nl|'\n'
name|'self'
op|'.'
name|'user'
op|'.'
name|'auth_url'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiAuthenticationException'
op|','
nl|'\n'
name|'bad_credentials_api'
op|'.'
name|'get_flavors'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_bad_login_both_bad
dedent|''
name|'def'
name|'test_bad_login_both_bad'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Test that I get a 401 with both bad username and bad password."""'
newline|'\n'
name|'bad_credentials_api'
op|'='
name|'client'
op|'.'
name|'TestOpenStackClient'
op|'('
string|'"notso_username"'
op|','
nl|'\n'
string|'"notso_password"'
op|','
nl|'\n'
name|'self'
op|'.'
name|'user'
op|'.'
name|'auth_url'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'client'
op|'.'
name|'OpenStackApiAuthenticationException'
op|','
nl|'\n'
name|'bad_credentials_api'
op|'.'
name|'get_flavors'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'__name__'
op|'=='
string|'"__main__"'
op|':'
newline|'\n'
indent|'    '
name|'unittest'
op|'.'
name|'main'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
