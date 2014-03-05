begin_unit
comment|'# Copyright 2013 OpenStack Foundation'
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
name|'base64'
newline|'\n'
name|'import'
name|'uuid'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'agent'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'fake'
name|'as'
name|'xenapi_fake'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_fake_instance
name|'def'
name|'_get_fake_instance'
op|'('
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'system_metadata'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'kwargs'
op|'.'
name|'items'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'system_metadata'
op|'.'
name|'append'
op|'('
op|'{'
nl|'\n'
string|'"key"'
op|':'
name|'k'
op|','
nl|'\n'
string|'"value"'
op|':'
name|'v'
nl|'\n'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
op|'{'
nl|'\n'
string|'"system_metadata"'
op|':'
name|'system_metadata'
op|','
nl|'\n'
string|'"uuid"'
op|':'
string|'"uuid"'
op|','
nl|'\n'
string|'"key_data"'
op|':'
string|'"ssh-rsa asdf"'
op|','
nl|'\n'
string|'"os_type"'
op|':'
string|'"asdf"'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AgentTestCaseBase
dedent|''
name|'class'
name|'AgentTestCaseBase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_create_agent
indent|'    '
name|'def'
name|'_create_agent'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'session'
op|'='
string|'"session"'
newline|'\n'
name|'self'
op|'.'
name|'virtapi'
op|'='
string|'"virtapi"'
newline|'\n'
name|'self'
op|'.'
name|'vm_ref'
op|'='
string|'"vm_ref"'
newline|'\n'
name|'return'
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|'('
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'virtapi'
op|','
nl|'\n'
name|'instance'
op|','
name|'self'
op|'.'
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|AgentImageFlagsTestCase
dedent|''
dedent|''
name|'class'
name|'AgentImageFlagsTestCase'
op|'('
name|'AgentTestCaseBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_agent_is_present
indent|'    '
name|'def'
name|'test_agent_is_present'
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
name|'use_agent_default'
op|'='
name|'False'
op|','
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"system_metadata"'
op|':'
nl|'\n'
op|'['
op|'{'
string|'"key"'
op|':'
string|'"image_xenapi_use_agent"'
op|','
string|'"value"'
op|':'
string|'"true"'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'agent'
op|'.'
name|'should_use_agent'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agent_is_disabled
dedent|''
name|'def'
name|'test_agent_is_disabled'
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
name|'use_agent_default'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"system_metadata"'
op|':'
nl|'\n'
op|'['
op|'{'
string|'"key"'
op|':'
string|'"image_xenapi_use_agent"'
op|','
string|'"value"'
op|':'
string|'"false"'
op|'}'
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'agent'
op|'.'
name|'should_use_agent'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agent_uses_deafault_when_prop_invalid
dedent|''
name|'def'
name|'test_agent_uses_deafault_when_prop_invalid'
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
name|'use_agent_default'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"system_metadata"'
op|':'
nl|'\n'
op|'['
op|'{'
string|'"key"'
op|':'
string|'"image_xenapi_use_agent"'
op|','
string|'"value"'
op|':'
string|'"bob"'
op|'}'
op|']'
op|','
nl|'\n'
string|'"uuid"'
op|':'
string|'"uuid"'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'agent'
op|'.'
name|'should_use_agent'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agent_default_not_present
dedent|''
name|'def'
name|'test_agent_default_not_present'
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
name|'use_agent_default'
op|'='
name|'False'
op|','
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"system_metadata"'
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'agent'
op|'.'
name|'should_use_agent'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_agent_default_present
dedent|''
name|'def'
name|'test_agent_default_present'
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
name|'use_agent_default'
op|'='
name|'True'
op|','
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"system_metadata"'
op|':'
op|'['
op|']'
op|'}'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'agent'
op|'.'
name|'should_use_agent'
op|'('
name|'instance'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SysMetaKeyTestBase
dedent|''
dedent|''
name|'class'
name|'SysMetaKeyTestBase'
op|'('
op|')'
op|':'
newline|'\n'
DECL|variable|key
indent|'    '
name|'key'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|_create_agent_with_value
name|'def'
name|'_create_agent_with_value'
op|'('
name|'self'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'kwargs'
op|'='
op|'{'
name|'self'
op|'.'
name|'key'
op|':'
name|'value'
op|'}'
newline|'\n'
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_sys_meta_key_true
dedent|''
name|'def'
name|'test_get_sys_meta_key_true'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent_with_value'
op|'('
string|'"true"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'agent'
op|'.'
name|'_get_sys_meta_key'
op|'('
name|'self'
op|'.'
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_sys_meta_key_false
dedent|''
name|'def'
name|'test_get_sys_meta_key_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent_with_value'
op|'('
string|'"False"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'agent'
op|'.'
name|'_get_sys_meta_key'
op|'('
name|'self'
op|'.'
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_sys_meta_key_invalid_is_false
dedent|''
name|'def'
name|'test_get_sys_meta_key_invalid_is_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent_with_value'
op|'('
string|'"invalid"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'agent'
op|'.'
name|'_get_sys_meta_key'
op|'('
name|'self'
op|'.'
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_sys_meta_key_missing_is_false
dedent|''
name|'def'
name|'test_get_sys_meta_key_missing_is_false'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'agent'
op|'.'
name|'_get_sys_meta_key'
op|'('
name|'self'
op|'.'
name|'key'
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SkipSshFlagTestCase
dedent|''
dedent|''
name|'class'
name|'SkipSshFlagTestCase'
op|'('
name|'SysMetaKeyTestBase'
op|','
name|'AgentTestCaseBase'
op|')'
op|':'
newline|'\n'
DECL|variable|key
indent|'    '
name|'key'
op|'='
string|'"image_xenapi_skip_agent_inject_ssh"'
newline|'\n'
nl|'\n'
DECL|member|test_skip_ssh_key_inject
name|'def'
name|'test_skip_ssh_key_inject'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent_with_value'
op|'('
string|'"True"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'agent'
op|'.'
name|'_skip_ssh_key_inject'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SkipFileInjectAtBootFlagTestCase
dedent|''
dedent|''
name|'class'
name|'SkipFileInjectAtBootFlagTestCase'
op|'('
name|'SysMetaKeyTestBase'
op|','
name|'AgentTestCaseBase'
op|')'
op|':'
newline|'\n'
DECL|variable|key
indent|'    '
name|'key'
op|'='
string|'"image_xenapi_skip_agent_inject_files_at_boot"'
newline|'\n'
nl|'\n'
DECL|member|test_skip_inject_files_at_boot
name|'def'
name|'test_skip_inject_files_at_boot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent_with_value'
op|'('
string|'"True"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'agent'
op|'.'
name|'_skip_inject_files_at_boot'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|InjectSshTestCase
dedent|''
dedent|''
name|'class'
name|'InjectSshTestCase'
op|'('
name|'AgentTestCaseBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_inject_ssh_key_succeeds
indent|'    '
name|'def'
name|'test_inject_ssh_key_succeeds'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'agent'
op|','
string|'"inject_file"'
op|')'
newline|'\n'
nl|'\n'
name|'agent'
op|'.'
name|'inject_file'
op|'('
string|'"/root/.ssh/authorized_keys"'
op|','
nl|'\n'
string|'"\\n# The following ssh key was injected by Nova"'
nl|'\n'
string|'"\\nssh-rsa asdf\\n"'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'.'
name|'inject_ssh_key'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|_test_inject_ssh_key_skipped
dedent|''
name|'def'
name|'_test_inject_ssh_key_skipped'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
comment|'# make sure its not called'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'agent'
op|','
string|'"inject_file"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'agent'
op|'.'
name|'inject_ssh_key'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_ssh_key_skipped_no_key_data
dedent|''
name|'def'
name|'test_inject_ssh_key_skipped_no_key_data'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'['
string|'"key_data"'
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_test_inject_ssh_key_skipped'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_ssh_key_skipped_windows
dedent|''
name|'def'
name|'test_inject_ssh_key_skipped_windows'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'['
string|'"os_type"'
op|']'
op|'='
string|'"windows"'
newline|'\n'
name|'self'
op|'.'
name|'_test_inject_ssh_key_skipped'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_ssh_key_skipped_cloud_init_present
dedent|''
name|'def'
name|'test_inject_ssh_key_skipped_cloud_init_present'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
nl|'\n'
name|'image_xenapi_skip_agent_inject_ssh'
op|'='
string|'"True"'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_test_inject_ssh_key_skipped'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FileInjectionTestCase
dedent|''
dedent|''
name|'class'
name|'FileInjectionTestCase'
op|'('
name|'AgentTestCaseBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_inject_file
indent|'    '
name|'def'
name|'test_inject_file'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'agent'
op|','
string|'"_call_agent"'
op|')'
newline|'\n'
nl|'\n'
name|'b64_path'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
string|"'path'"
op|')'
newline|'\n'
name|'b64_contents'
op|'='
name|'base64'
op|'.'
name|'b64encode'
op|'('
string|"'contents'"
op|')'
newline|'\n'
name|'agent'
op|'.'
name|'_call_agent'
op|'('
string|"'inject_file'"
op|','
nl|'\n'
op|'{'
string|"'b64_contents'"
op|':'
name|'b64_contents'
op|','
nl|'\n'
string|"'b64_path'"
op|':'
name|'b64_path'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'agent'
op|'.'
name|'inject_file'
op|'('
string|'"path"'
op|','
string|'"contents"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_files
dedent|''
name|'def'
name|'test_inject_files'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'agent'
op|','
string|'"inject_file"'
op|')'
newline|'\n'
nl|'\n'
name|'files'
op|'='
op|'['
op|'('
string|'"path1"'
op|','
string|'"content1"'
op|')'
op|','
op|'('
string|'"path2"'
op|','
string|'"content2"'
op|')'
op|']'
newline|'\n'
name|'agent'
op|'.'
name|'inject_file'
op|'('
op|'*'
name|'files'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'agent'
op|'.'
name|'inject_file'
op|'('
op|'*'
name|'files'
op|'['
number|'1'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'agent'
op|'.'
name|'inject_files'
op|'('
name|'files'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_inject_files_skipped_when_cloud_init_installed
dedent|''
name|'def'
name|'test_inject_files_skipped_when_cloud_init_installed'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
nl|'\n'
name|'image_xenapi_skip_agent_inject_files_at_boot'
op|'='
string|'"True"'
op|')'
newline|'\n'
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'agent'
op|','
string|'"inject_file"'
op|')'
newline|'\n'
nl|'\n'
name|'files'
op|'='
op|'['
op|'('
string|'"path1"'
op|','
string|'"content1"'
op|')'
op|','
op|'('
string|'"path2"'
op|','
string|'"content2"'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'ReplayAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'agent'
op|'.'
name|'inject_files'
op|'('
name|'files'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SetAdminPasswordTestCase
dedent|''
dedent|''
name|'class'
name|'SetAdminPasswordTestCase'
op|'('
name|'AgentTestCaseBase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|','
string|"'_call_agent'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'('
string|'"nova.virt.xenapi.agent.SimpleDH"'
op|')'
newline|'\n'
DECL|member|test_exchange_key_with_agent
name|'def'
name|'test_exchange_key_with_agent'
op|'('
name|'self'
op|','
name|'mock_simple_dh'
op|','
name|'mock_call_agent'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'None'
op|')'
newline|'\n'
name|'instance_mock'
op|'='
name|'mock_simple_dh'
op|'('
op|')'
newline|'\n'
name|'instance_mock'
op|'.'
name|'get_public'
op|'.'
name|'return_value'
op|'='
number|'4321'
newline|'\n'
name|'mock_call_agent'
op|'.'
name|'return_value'
op|'='
string|'"1234"'
newline|'\n'
nl|'\n'
name|'result'
op|'='
name|'agent'
op|'.'
name|'_exchange_key_with_agent'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'mock_call_agent'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'key_init'"
op|','
op|'{'
string|'"pub"'
op|':'
string|'"4321"'
op|'}'
op|','
nl|'\n'
name|'success_codes'
op|'='
op|'['
string|"'D0'"
op|']'
op|','
nl|'\n'
name|'ignore_errors'
op|'='
name|'False'
op|')'
newline|'\n'
name|'result'
op|'.'
name|'compute_shared'
op|'.'
name|'assert_called_once_with'
op|'('
number|'1234'
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
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|','
string|"'_call_agent'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|','
nl|'\n'
string|"'_save_instance_password_if_sshkey_present'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|','
string|"'_exchange_key_with_agent'"
op|')'
newline|'\n'
DECL|member|test_set_admin_password_works
name|'def'
name|'test_set_admin_password_works'
op|'('
name|'self'
op|','
name|'mock_exchange'
op|','
name|'mock_save'
op|','
nl|'\n'
name|'mock_call_agent'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_dh'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
name|'spec_set'
op|'='
name|'agent'
op|'.'
name|'SimpleDH'
op|')'
newline|'\n'
name|'mock_dh'
op|'.'
name|'encrypt'
op|'.'
name|'return_value'
op|'='
string|'"enc_pass"'
newline|'\n'
name|'mock_exchange'
op|'.'
name|'return_value'
op|'='
name|'mock_dh'
newline|'\n'
name|'agent_inst'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'agent_inst'
op|'.'
name|'set_admin_password'
op|'('
string|'"new_pass"'
op|')'
newline|'\n'
nl|'\n'
name|'mock_dh'
op|'.'
name|'encrypt'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"new_pass\\n"'
op|')'
newline|'\n'
name|'mock_call_agent'
op|'.'
name|'assert_called_once_with'
op|'('
string|"'password'"
op|','
nl|'\n'
op|'{'
string|"'enc_pass'"
op|':'
string|"'enc_pass'"
op|'}'
op|')'
newline|'\n'
name|'mock_save'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"new_pass"'
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
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|','
string|"'_add_instance_fault'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|','
string|"'_exchange_key_with_agent'"
op|')'
newline|'\n'
DECL|member|test_set_admin_password_silently_fails
name|'def'
name|'test_set_admin_password_silently_fails'
op|'('
name|'self'
op|','
name|'mock_exchange'
op|','
nl|'\n'
name|'mock_add_fault'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'error'
op|'='
name|'exception'
op|'.'
name|'AgentTimeout'
op|'('
name|'method'
op|'='
string|'"fake"'
op|')'
newline|'\n'
name|'mock_exchange'
op|'.'
name|'side_effect'
op|'='
name|'error'
newline|'\n'
name|'agent_inst'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'agent_inst'
op|'.'
name|'set_admin_password'
op|'('
string|'"new_pass"'
op|')'
newline|'\n'
nl|'\n'
name|'mock_add_fault'
op|'.'
name|'assert_called_once_with'
op|'('
name|'error'
op|','
name|'mock'
op|'.'
name|'ANY'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|UpgradeRequiredTestCase
dedent|''
dedent|''
name|'class'
name|'UpgradeRequiredTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_less_than
indent|'    '
name|'def'
name|'test_less_than'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'agent'
op|'.'
name|'is_upgrade_required'
op|'('
string|"'1.2.3.4'"
op|','
string|"'1.2.3.5'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_greater_than
dedent|''
name|'def'
name|'test_greater_than'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'agent'
op|'.'
name|'is_upgrade_required'
op|'('
string|"'1.2.3.5'"
op|','
string|"'1.2.3.4'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_equal
dedent|''
name|'def'
name|'test_equal'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'agent'
op|'.'
name|'is_upgrade_required'
op|'('
string|"'1.2.3.4'"
op|','
string|"'1.2.3.4'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_non_lexical
dedent|''
name|'def'
name|'test_non_lexical'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'agent'
op|'.'
name|'is_upgrade_required'
op|'('
string|"'1.2.3.10'"
op|','
string|"'1.2.3.4'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_length
dedent|''
name|'def'
name|'test_length'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'agent'
op|'.'
name|'is_upgrade_required'
op|'('
string|"'1.2.3'"
op|','
string|"'1.2.3.4'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'uuid'
op|','
string|'"uuid4"'
op|')'
newline|'\n'
DECL|class|CallAgentTestCase
name|'class'
name|'CallAgentTestCase'
op|'('
name|'AgentTestCaseBase'
op|')'
op|':'
newline|'\n'
DECL|member|test_call_agent_success
indent|'    '
name|'def'
name|'test_call_agent_success'
op|'('
name|'self'
op|','
name|'mock_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"uuid"'
op|':'
string|'"fake"'
op|'}'
newline|'\n'
name|'addl_args'
op|'='
op|'{'
string|'"foo"'
op|':'
string|'"bar"'
op|'}'
newline|'\n'
nl|'\n'
name|'session'
op|'.'
name|'VM'
op|'.'
name|'get_domid'
op|'.'
name|'return_value'
op|'='
string|"'42'"
newline|'\n'
name|'mock_uuid'
op|'.'
name|'return_value'
op|'='
number|'1'
newline|'\n'
name|'session'
op|'.'
name|'call_plugin'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'returncode'"
op|':'
string|"'4'"
op|','
nl|'\n'
string|"'message'"
op|':'
string|'"asdf\\\\r\\\\n"'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
string|'"asdf"'
op|','
nl|'\n'
name|'agent'
op|'.'
name|'_call_agent'
op|'('
name|'session'
op|','
name|'instance'
op|','
string|'"vm_ref"'
op|','
nl|'\n'
string|'"method"'
op|','
name|'addl_args'
op|','
name|'timeout'
op|'='
number|'300'
op|','
nl|'\n'
name|'success_codes'
op|'='
op|'['
string|"'0'"
op|','
string|"'4'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'expected_args'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'dom_id'"
op|':'
string|"'42'"
op|','
nl|'\n'
string|"'timeout'"
op|':'
string|"'300'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'expected_args'
op|'.'
name|'update'
op|'('
name|'addl_args'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'VM'
op|'.'
name|'get_domid'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"vm_ref"'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'call_plugin'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"agent"'
op|','
string|'"method"'
op|','
nl|'\n'
name|'expected_args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_call_agent_setup
dedent|''
name|'def'
name|'_call_agent_setup'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'mock_uuid'
op|','
nl|'\n'
name|'returncode'
op|'='
string|"'0'"
op|','
name|'success_codes'
op|'='
name|'None'
op|','
nl|'\n'
name|'exception'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'='
name|'xenapi_fake'
op|'.'
name|'Failure'
newline|'\n'
name|'instance'
op|'='
op|'{'
string|'"uuid"'
op|':'
string|'"fake"'
op|'}'
newline|'\n'
nl|'\n'
name|'session'
op|'.'
name|'VM'
op|'.'
name|'get_domid'
op|'.'
name|'return_value'
op|'='
number|'42'
newline|'\n'
name|'mock_uuid'
op|'.'
name|'return_value'
op|'='
number|'1'
newline|'\n'
name|'if'
name|'exception'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'call_plugin'
op|'.'
name|'side_effect'
op|'='
name|'exception'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'session'
op|'.'
name|'call_plugin'
op|'.'
name|'return_value'
op|'='
op|'{'
string|"'returncode'"
op|':'
name|'returncode'
op|','
nl|'\n'
string|"'message'"
op|':'
string|'"asdf\\\\r\\\\n"'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'agent'
op|'.'
name|'_call_agent'
op|'('
name|'session'
op|','
name|'instance'
op|','
string|'"vm_ref"'
op|','
string|'"method"'
op|','
nl|'\n'
name|'success_codes'
op|'='
name|'success_codes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_assert_agent_called
dedent|''
name|'def'
name|'_assert_agent_called'
op|'('
name|'self'
op|','
name|'session'
op|','
name|'mock_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'expected_args'
op|'='
op|'{'
nl|'\n'
string|"'id'"
op|':'
string|"'1'"
op|','
nl|'\n'
string|"'dom_id'"
op|':'
string|"'42'"
op|','
nl|'\n'
string|"'timeout'"
op|':'
string|"'30'"
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'session'
op|'.'
name|'call_plugin'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"agent"'
op|','
string|'"method"'
op|','
nl|'\n'
name|'expected_args'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'VM'
op|'.'
name|'get_domid'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"vm_ref"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_agent_works_with_defaults
dedent|''
name|'def'
name|'test_call_agent_works_with_defaults'
op|'('
name|'self'
op|','
name|'mock_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_call_agent_setup'
op|'('
name|'session'
op|','
name|'mock_uuid'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assert_agent_called'
op|'('
name|'session'
op|','
name|'mock_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_agent_fails_with_timeout
dedent|''
name|'def'
name|'test_call_agent_fails_with_timeout'
op|'('
name|'self'
op|','
name|'mock_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AgentTimeout'
op|','
name|'self'
op|'.'
name|'_call_agent_setup'
op|','
nl|'\n'
name|'session'
op|','
name|'mock_uuid'
op|','
nl|'\n'
name|'exception'
op|'='
name|'xenapi_fake'
op|'.'
name|'Failure'
op|'('
op|'['
string|'"TIMEOUT:fake"'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assert_agent_called'
op|'('
name|'session'
op|','
name|'mock_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_agent_fails_with_not_implemented
dedent|''
name|'def'
name|'test_call_agent_fails_with_not_implemented'
op|'('
name|'self'
op|','
name|'mock_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AgentNotImplemented'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_call_agent_setup'
op|','
nl|'\n'
name|'session'
op|','
name|'mock_uuid'
op|','
nl|'\n'
name|'exception'
op|'='
name|'xenapi_fake'
op|'.'
name|'Failure'
op|'('
op|'['
string|'"NOT IMPLEMENTED:"'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assert_agent_called'
op|'('
name|'session'
op|','
name|'mock_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_agent_fails_with_other_error
dedent|''
name|'def'
name|'test_call_agent_fails_with_other_error'
op|'('
name|'self'
op|','
name|'mock_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AgentError'
op|','
name|'self'
op|'.'
name|'_call_agent_setup'
op|','
nl|'\n'
name|'session'
op|','
name|'mock_uuid'
op|','
nl|'\n'
name|'exception'
op|'='
name|'xenapi_fake'
op|'.'
name|'Failure'
op|'('
op|'['
string|'"asdf"'
op|']'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assert_agent_called'
op|'('
name|'session'
op|','
name|'mock_uuid'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_agent_fails_with_returned_error
dedent|''
name|'def'
name|'test_call_agent_fails_with_returned_error'
op|'('
name|'self'
op|','
name|'mock_uuid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AgentError'
op|','
name|'self'
op|'.'
name|'_call_agent_setup'
op|','
nl|'\n'
name|'session'
op|','
name|'mock_uuid'
op|','
name|'returncode'
op|'='
string|"'42'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_assert_agent_called'
op|'('
name|'session'
op|','
name|'mock_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|XenAPIBasedAgent
dedent|''
dedent|''
name|'class'
name|'XenAPIBasedAgent'
op|'('
name|'AgentTestCaseBase'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|','
string|'"_add_instance_fault"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'agent'
op|','
string|'"_call_agent"'
op|')'
newline|'\n'
DECL|member|test_call_agent_swallows_error
name|'def'
name|'test_call_agent_swallows_error'
op|'('
name|'self'
op|','
name|'mock_call_agent'
op|','
nl|'\n'
name|'mock_add_instance_fault'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_error'
op|'='
name|'exception'
op|'.'
name|'AgentError'
op|'('
name|'method'
op|'='
string|'"bob"'
op|')'
newline|'\n'
name|'mock_call_agent'
op|'.'
name|'side_effect'
op|'='
name|'fake_error'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'agent'
op|'.'
name|'_call_agent'
op|'('
string|'"bob"'
op|')'
newline|'\n'
nl|'\n'
name|'mock_call_agent'
op|'.'
name|'assert_called_once_with'
op|'('
name|'agent'
op|'.'
name|'session'
op|','
name|'agent'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'agent'
op|'.'
name|'vm_ref'
op|','
string|'"bob"'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'mock_add_instance_fault'
op|'.'
name|'assert_called_once_with'
op|'('
name|'fake_error'
op|','
name|'mock'
op|'.'
name|'ANY'
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
name|'agent'
op|'.'
name|'XenAPIBasedAgent'
op|','
string|'"_add_instance_fault"'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'agent'
op|','
string|'"_call_agent"'
op|')'
newline|'\n'
DECL|member|test_call_agent_throws_error
name|'def'
name|'test_call_agent_throws_error'
op|'('
name|'self'
op|','
name|'mock_call_agent'
op|','
nl|'\n'
name|'mock_add_instance_fault'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake_error'
op|'='
name|'exception'
op|'.'
name|'AgentError'
op|'('
name|'method'
op|'='
string|'"bob"'
op|')'
newline|'\n'
name|'mock_call_agent'
op|'.'
name|'side_effect'
op|'='
name|'fake_error'
newline|'\n'
nl|'\n'
name|'instance'
op|'='
name|'_get_fake_instance'
op|'('
op|')'
newline|'\n'
name|'agent'
op|'='
name|'self'
op|'.'
name|'_create_agent'
op|'('
name|'instance'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'AgentError'
op|','
name|'agent'
op|'.'
name|'_call_agent'
op|','
nl|'\n'
string|'"bob"'
op|','
name|'ignore_errors'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'mock_call_agent'
op|'.'
name|'assert_called_once_with'
op|'('
name|'agent'
op|'.'
name|'session'
op|','
name|'agent'
op|'.'
name|'instance'
op|','
nl|'\n'
name|'agent'
op|'.'
name|'vm_ref'
op|','
string|'"bob"'
op|','
name|'None'
op|','
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'mock_add_instance_fault'
op|'.'
name|'called'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
