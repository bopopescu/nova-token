begin_unit
comment|'# Copyright 2012 Nebula, Inc.'
nl|'\n'
comment|'# Copyright 2013 IBM Corp.'
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
DECL|class|AdminActionsSamplesJsonTest
name|'class'
name|'AdminActionsSamplesJsonTest'
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
string|'"os-admin-actions"'
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
string|'"""setUp Method for AdminActions api samples extension\n\n        This method creates the server that will be used in each tests\n        """'
newline|'\n'
name|'super'
op|'('
name|'AdminActionsSamplesJsonTest'
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
name|'uuid'
op|'='
name|'self'
op|'.'
name|'_post_server'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_post_reset_network
dedent|''
name|'def'
name|'test_post_reset_network'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api samples to reset server network request.'
nl|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'admin-actions-reset-network'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_post_inject_network_info
dedent|''
name|'def'
name|'test_post_inject_network_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# Get api samples to inject network info request.'
nl|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'admin-actions-inject-network-info'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'202'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_post_reset_state
dedent|''
name|'def'
name|'test_post_reset_state'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
comment|'# get api samples to server reset state request.'
nl|'\n'
indent|'        '
name|'response'
op|'='
name|'self'
op|'.'
name|'_do_post'
op|'('
string|"'servers/%s/action'"
op|'%'
name|'self'
op|'.'
name|'uuid'
op|','
nl|'\n'
string|"'admin-actions-reset-server-state'"
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'response'
op|'.'
name|'status_code'
op|','
number|'202'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
