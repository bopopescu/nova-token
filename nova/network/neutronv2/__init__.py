begin_unit
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
name|'neutronclient'
op|'.'
name|'common'
name|'import'
name|'exceptions'
newline|'\n'
name|'from'
name|'neutronclient'
op|'.'
name|'v2_0'
name|'import'
name|'client'
name|'as'
name|'clientv20'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'local'
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
DECL|function|_get_client
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
name|'params'
op|'='
op|'{'
nl|'\n'
string|"'endpoint_url'"
op|':'
name|'CONF'
op|'.'
name|'neutron_url'
op|','
nl|'\n'
string|"'timeout'"
op|':'
name|'CONF'
op|'.'
name|'neutron_url_timeout'
op|','
nl|'\n'
string|"'insecure'"
op|':'
name|'CONF'
op|'.'
name|'neutron_api_insecure'
op|','
nl|'\n'
string|"'ca_cert'"
op|':'
name|'CONF'
op|'.'
name|'neutron_ca_certificates_file'
op|','
nl|'\n'
string|"'auth_strategy'"
op|':'
name|'CONF'
op|'.'
name|'neutron_auth_strategy'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
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
string|"'username'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'neutron_admin_username'
newline|'\n'
name|'if'
name|'CONF'
op|'.'
name|'neutron_admin_tenant_id'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'tenant_id'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'neutron_admin_tenant_id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'params'
op|'['
string|"'tenant_name'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'neutron_admin_tenant_name'
newline|'\n'
dedent|''
name|'params'
op|'['
string|"'password'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'neutron_admin_password'
newline|'\n'
name|'params'
op|'['
string|"'auth_url'"
op|']'
op|'='
name|'CONF'
op|'.'
name|'neutron_admin_auth_url'
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
comment|'# NOTE(dprince): In the case where no auth_token is present'
nl|'\n'
comment|'# we allow use of neutron admin tenant credentials if'
nl|'\n'
comment|'# it is an admin context.'
nl|'\n'
comment|'# This is to support some services (metadata API) where'
nl|'\n'
comment|'# an admin context is used without an auth token.'
nl|'\n'
indent|'    '
name|'if'
name|'admin'
name|'or'
op|'('
name|'context'
op|'.'
name|'is_admin'
name|'and'
name|'not'
name|'context'
op|'.'
name|'auth_token'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(dims): We need to use admin token, let us cache a'
nl|'\n'
comment|'# thread local copy for re-using this client'
nl|'\n'
comment|'# multiple times and to avoid excessive calls'
nl|'\n'
comment|'# to neutron to fetch tokens. Some of the hackiness in this code'
nl|'\n'
comment|'# will go away once BP auth-plugins is implemented.'
nl|'\n'
comment|'# That blue print will ensure that tokens can be shared'
nl|'\n'
comment|'# across clients as well'
nl|'\n'
indent|'        '
name|'if'
name|'not'
name|'hasattr'
op|'('
name|'local'
op|'.'
name|'strong_store'
op|','
string|"'neutron_client'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'local'
op|'.'
name|'strong_store'
op|'.'
name|'neutron_client'
op|'='
name|'_get_client'
op|'('
name|'token'
op|'='
name|'None'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'local'
op|'.'
name|'strong_store'
op|'.'
name|'neutron_client'
newline|'\n'
nl|'\n'
comment|'# We got a user token that we can use that as-is'
nl|'\n'
dedent|''
name|'if'
name|'context'
op|'.'
name|'auth_token'
op|':'
newline|'\n'
indent|'        '
name|'token'
op|'='
name|'context'
op|'.'
name|'auth_token'
newline|'\n'
name|'return'
name|'_get_client'
op|'('
name|'token'
op|'='
name|'token'
op|')'
newline|'\n'
nl|'\n'
comment|'# We did not get a user token and we should not be using'
nl|'\n'
comment|'# an admin token so log an error'
nl|'\n'
dedent|''
name|'raise'
name|'exceptions'
op|'.'
name|'Unauthorized'
op|'('
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
