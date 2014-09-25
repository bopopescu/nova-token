begin_unit
comment|'# Copyright 2013 Cloudbase Solutions Srl'
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
name|'re'
newline|'\n'
nl|'\n'
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
op|'.'
name|'tests'
op|'.'
name|'integrated'
op|'.'
name|'v3'
name|'import'
name|'test_servers'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConsoleAuthTokensSampleJsonTests
name|'class'
name|'ConsoleAuthTokensSampleJsonTests'
op|'('
name|'test_servers'
op|'.'
name|'ServersSampleBase'
op|')'
op|':'
newline|'\n'
DECL|variable|extension_name
indent|'    '
name|'extension_name'
op|'='
string|'"os-console-auth-tokens"'
newline|'\n'
DECL|variable|extra_extensions_to_load
name|'extra_extensions_to_load'
op|'='
op|'['
string|'"os-remote-consoles"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_console_url
name|'def'
name|'_get_console_url'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'data'
op|')'
op|'['
string|'"console"'
op|']'
op|'['
string|'"url"'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_get_console_token
dedent|''
name|'def'
name|'_get_console_token'
op|'('
name|'self'
op|','
name|'uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'uuid'
op|','
nl|'\n'
string|"'get-rdp-console-post-req'"
op|','
nl|'\n'
op|'{'
string|"'action'"
op|':'
string|"'os-getRDPConsole'"
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'url'
op|'='
name|'self'
op|'.'
name|'_get_console_url'
op|'('
name|'response'
op|'.'
name|'content'
op|')'
newline|'\n'
name|'return'
name|'re'
op|'.'
name|'match'
op|'('
string|"'.+?token=([^&]+)'"
op|','
name|'url'
op|')'
op|'.'
name|'groups'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
DECL|member|test_get_console_connect_info
dedent|''
name|'def'
name|'test_get_console_connect_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'flags'
op|'('
name|'enabled'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'rdp'"
op|')'
newline|'\n'
nl|'\n'
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
name|'token'
op|'='
name|'self'
op|'.'
name|'_get_console_token'
op|'('
name|'uuid'
op|')'
newline|'\n'
nl|'\n'
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_get'
op|'('
string|"'os-console-auth-tokens/%s'"
op|'%'
name|'token'
op|')'
newline|'\n'
nl|'\n'
name|'subs'
op|'='
name|'self'
op|'.'
name|'_get_regexes'
op|'('
op|')'
newline|'\n'
name|'subs'
op|'['
string|'"uuid"'
op|']'
op|'='
name|'uuid'
newline|'\n'
name|'subs'
op|'['
string|'"host"'
op|']'
op|'='
string|'r"[\\w\\.\\-]+"'
newline|'\n'
name|'subs'
op|'['
string|'"port"'
op|']'
op|'='
string|'"[0-9]+"'
newline|'\n'
name|'subs'
op|'['
string|'"internal_access_path"'
op|']'
op|'='
string|'".*"'
newline|'\n'
name|'self'
op|'.'
name|'_verify_response'
op|'('
string|"'get-console-connect-info-get-resp'"
op|','
name|'subs'
op|','
nl|'\n'
name|'response'
op|','
number|'200'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
