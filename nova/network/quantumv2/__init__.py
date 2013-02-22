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
name|'import'
name|'client'
newline|'\n'
name|'from'
name|'quantumclient'
op|'.'
name|'v2_0'
name|'import'
name|'client'
name|'as'
name|'clientv20'
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
DECL|function|_get_auth_token
name|'def'
name|'_get_auth_token'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'httpclient'
op|'='
name|'client'
op|'.'
name|'HTTPClient'
op|'('
nl|'\n'
name|'username'
op|'='
name|'CONF'
op|'.'
name|'quantum_admin_username'
op|','
nl|'\n'
name|'tenant_name'
op|'='
name|'CONF'
op|'.'
name|'quantum_admin_tenant_name'
op|','
nl|'\n'
name|'region_name'
op|'='
name|'CONF'
op|'.'
name|'quantum_region_name'
op|','
nl|'\n'
name|'password'
op|'='
name|'CONF'
op|'.'
name|'quantum_admin_password'
op|','
nl|'\n'
name|'auth_url'
op|'='
name|'CONF'
op|'.'
name|'quantum_admin_auth_url'
op|','
nl|'\n'
name|'timeout'
op|'='
name|'CONF'
op|'.'
name|'quantum_url_timeout'
op|','
nl|'\n'
name|'auth_strategy'
op|'='
name|'CONF'
op|'.'
name|'quantum_auth_strategy'
op|','
nl|'\n'
name|'insecure'
op|'='
name|'CONF'
op|'.'
name|'quantum_api_insecure'
op|')'
newline|'\n'
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
indent|'        '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|'"_get_auth_token() failed"'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'httpclient'
op|'.'
name|'auth_token'
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
name|'if'
name|'not'
name|'token'
name|'and'
name|'CONF'
op|'.'
name|'quantum_auth_strategy'
op|':'
newline|'\n'
indent|'        '
name|'token'
op|'='
name|'_get_auth_token'
op|'('
op|')'
newline|'\n'
dedent|''
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
name|'params'
op|'['
string|"'auth_strategy'"
op|']'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'return'
name|'clientv20'
op|'.'
name|'Client'
op|'('
op|'**'
name|'params'
op|')'
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
