begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2012 OpenStack Foundation'
nl|'\n'
comment|'# All Rights Reserved'
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
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'quantumclient'
op|'.'
name|'v2_0'
name|'import'
name|'client'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'excutils'
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
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
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
nl|'\n'
nl|'\n'
DECL|variable|cached_admin_client
name|'cached_admin_client'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_fill_admin_details
name|'def'
name|'_fill_admin_details'
op|'('
name|'params'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'params'
op|'['
string|"'username'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'quantum_admin_username'
newline|'\n'
name|'params'
op|'['
string|"'tenant_name'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'quantum_admin_tenant_name'
newline|'\n'
name|'params'
op|'['
string|"'region_name'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'quantum_region_name'
newline|'\n'
name|'params'
op|'['
string|"'password'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'quantum_admin_password'
newline|'\n'
name|'params'
op|'['
string|"'auth_url'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'quantum_admin_auth_url'
newline|'\n'
name|'params'
op|'['
string|"'timeout'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'quantum_url_timeout'
newline|'\n'
name|'params'
op|'['
string|"'auth_strategy'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'quantum_auth_strategy'
newline|'\n'
name|'params'
op|'['
string|"'insecure'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'quantum_api_insecure'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_client
dedent|''
name|'def'
name|'_get_client'
op|'('
name|'token'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'cached_admin_client'
newline|'\n'
nl|'\n'
name|'should_cache'
op|'='
name|'False'
newline|'\n'
name|'params'
op|'='
op|'{'
nl|'\n'
string|"'endpoint_url'"
op|':'
name|'CONF'
op|'.'
name|'quantum_url'
op|','
nl|'\n'
string|"'timeout'"
op|':'
name|'CONF'
op|'.'
name|'quantum_url_timeout'
op|','
nl|'\n'
string|"'insecure'"
op|':'
name|'CONF'
op|'.'
name|'quantum_api_insecure'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'if'
name|'token'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'['
string|"'token'"
op|']'
op|'='
name|'token'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'CONF'
op|'.'
name|'quantum_auth_strategy'
op|':'
newline|'\n'
indent|'            '
name|'should_cache'
op|'='
name|'True'
newline|'\n'
name|'_fill_admin_details'
op|'('
name|'params'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'auth_strategy'"
op|']'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'new_client'
op|'='
name|'client'
op|'.'
name|'Client'
op|'('
op|'**'
name|'params'
op|')'
newline|'\n'
name|'if'
name|'should_cache'
op|':'
newline|'\n'
comment|"# in this case, we don't have the token yet"
nl|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'new_client'
op|'.'
name|'httpclient'
op|'.'
name|'authenticate'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"quantum authentication failed"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'cached_admin_client'
op|'='
name|'new_client'
newline|'\n'
dedent|''
name|'return'
name|'new_client'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_client
dedent|''
name|'def'
name|'get_client'
op|'('
name|'context'
op|','
name|'admin'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'admin'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'cached_admin_client'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'cached_admin_client'
newline|'\n'
nl|'\n'
dedent|''
name|'token'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'token'
op|'='
name|'context'
op|'.'
name|'auth_token'
newline|'\n'
dedent|''
name|'return'
name|'_get_client'
op|'('
name|'token'
op|'='
name|'token'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
