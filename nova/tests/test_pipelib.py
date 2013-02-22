begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
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
name|'cloudpipe'
name|'import'
name|'pipelib'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'crypto'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PipelibTest
name|'class'
name|'PipelibTest'
op|'('
name|'test'
op|'.'
name|'TestCase'
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
name|'PipelibTest'
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
name|'cloudpipe'
op|'='
name|'pipelib'
op|'.'
name|'CloudPipe'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'project'
op|'='
string|'"222"'
newline|'\n'
name|'self'
op|'.'
name|'user'
op|'='
string|'"111"'
newline|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
name|'self'
op|'.'
name|'user'
op|','
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_encoded_zip
dedent|''
name|'def'
name|'test_get_encoded_zip'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tmpdir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ca_path'
op|'='
name|'tmpdir'
op|')'
newline|'\n'
name|'crypto'
op|'.'
name|'ensure_ca_filesystem'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'ret'
op|'='
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'get_encoded_zip'
op|'('
name|'self'
op|'.'
name|'project'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'ret'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_launch_vpn_instance
dedent|''
dedent|''
name|'def'
name|'test_launch_vpn_instance'
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
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'compute_api'
op|','
nl|'\n'
string|'"create"'
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
op|'('
name|'None'
op|','
string|'"r-fakeres"'
op|')'
op|')'
newline|'\n'
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tmpdir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'ca_path'
op|'='
name|'tmpdir'
op|','
name|'keys_path'
op|'='
name|'tmpdir'
op|')'
newline|'\n'
name|'crypto'
op|'.'
name|'ensure_ca_filesystem'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'launch_vpn_instance'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setup_security_group
dedent|''
dedent|''
name|'def'
name|'test_setup_security_group'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'group_name'
op|'='
string|'"%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'project'
op|','
name|'CONF'
op|'.'
name|'vpn_key_suffix'
op|')'
newline|'\n'
nl|'\n'
comment|'# First attempt, does not exist (thus its created)'
nl|'\n'
name|'res1_group'
op|'='
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'setup_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res1_group'
op|','
name|'group_name'
op|')'
newline|'\n'
nl|'\n'
comment|'# Second attempt, it exists in the DB'
nl|'\n'
name|'res2_group'
op|'='
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'setup_security_group'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res1_group'
op|','
name|'res2_group'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setup_key_pair
dedent|''
name|'def'
name|'test_setup_key_pair'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_name'
op|'='
string|'"%s%s"'
op|'%'
op|'('
name|'self'
op|'.'
name|'project'
op|','
name|'CONF'
op|'.'
name|'vpn_key_suffix'
op|')'
newline|'\n'
name|'with'
name|'utils'
op|'.'
name|'tempdir'
op|'('
op|')'
name|'as'
name|'tmpdir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'flags'
op|'('
name|'keys_path'
op|'='
name|'tmpdir'
op|')'
newline|'\n'
nl|'\n'
comment|'# First attempt, key does not exist (thus it is generated)'
nl|'\n'
name|'res1_key'
op|'='
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'setup_key_pair'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res1_key'
op|','
name|'key_name'
op|')'
newline|'\n'
nl|'\n'
comment|'# Second attempt, it exists in the DB'
nl|'\n'
name|'res2_key'
op|'='
name|'self'
op|'.'
name|'cloudpipe'
op|'.'
name|'setup_key_pair'
op|'('
name|'self'
op|'.'
name|'context'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'res2_key'
op|','
name|'res1_key'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
