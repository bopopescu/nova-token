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
name|'random'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'import'
name|'mock'
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
name|'exception'
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
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'stubs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'driver'
name|'as'
name|'xenapi_conn'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'image'
name|'import'
name|'glance'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vm_utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestGlanceStore
name|'class'
name|'TestGlanceStore'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
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
name|'TestGlanceStore'
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
name|'store'
op|'='
name|'glance'
op|'.'
name|'GlanceStore'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'glance_host'
op|'='
string|"'1.1.1.1'"
op|','
nl|'\n'
name|'glance_port'
op|'='
number|'123'
op|','
nl|'\n'
name|'glance_api_insecure'
op|'='
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'connection_url'
op|'='
string|"'test_url'"
op|','
nl|'\n'
name|'connection_password'
op|'='
string|"'test_pass'"
op|','
nl|'\n'
name|'group'
op|'='
string|"'xenserver'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'context'
op|'='
name|'context'
op|'.'
name|'RequestContext'
op|'('
nl|'\n'
string|"'user'"
op|','
string|"'project'"
op|','
name|'auth_token'
op|'='
string|"'foobar'"
op|')'
newline|'\n'
nl|'\n'
name|'fake'
op|'.'
name|'reset'
op|'('
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'stubout_session'
op|'('
name|'self'
op|'.'
name|'stubs'
op|','
name|'fake'
op|'.'
name|'SessionBase'
op|')'
newline|'\n'
name|'driver'
op|'='
name|'xenapi_conn'
op|'.'
name|'XenAPIDriver'
op|'('
name|'False'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'='
name|'driver'
op|'.'
name|'_session'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
nl|'\n'
name|'vm_utils'
op|','
string|"'get_sr_path'"
op|','
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
string|"'/fake/sr/path'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'instance'
op|'='
op|'{'
string|"'uuid'"
op|':'
string|"'blah'"
op|','
nl|'\n'
string|"'system_metadata'"
op|':'
op|'['
op|']'
op|','
nl|'\n'
string|"'auto_disk_config'"
op|':'
name|'True'
op|','
nl|'\n'
string|"'os_type'"
op|':'
string|"'default'"
op|','
nl|'\n'
string|"'xenapi_use_agent'"
op|':'
string|"'true'"
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_params
dedent|''
name|'def'
name|'_get_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'image_id'"
op|':'
string|"'fake_image_uuid'"
op|','
nl|'\n'
string|"'glance_host'"
op|':'
string|"'1.1.1.1'"
op|','
nl|'\n'
string|"'glance_port'"
op|':'
number|'123'
op|','
nl|'\n'
string|"'glance_use_ssl'"
op|':'
name|'False'
op|','
nl|'\n'
string|"'sr_path'"
op|':'
string|"'/fake/sr/path'"
op|','
nl|'\n'
string|"'extra_headers'"
op|':'
op|'{'
string|"'X-Service-Catalog'"
op|':'
string|"'[]'"
op|','
nl|'\n'
string|"'X-Auth-Token'"
op|':'
string|"'foobar'"
op|','
nl|'\n'
string|"'X-Roles'"
op|':'
string|"''"
op|','
nl|'\n'
string|"'X-Tenant-Id'"
op|':'
string|"'project'"
op|','
nl|'\n'
string|"'X-User-Id'"
op|':'
string|"'user'"
op|','
nl|'\n'
string|"'X-Identity-Status'"
op|':'
string|"'Confirmed'"
op|'}'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|_get_download_params
dedent|''
name|'def'
name|'_get_download_params'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_params'
op|'('
op|')'
newline|'\n'
name|'params'
op|'['
string|"'uuid_stack'"
op|']'
op|'='
op|'['
string|"'uuid1'"
op|']'
newline|'\n'
name|'return'
name|'params'
newline|'\n'
nl|'\n'
DECL|member|test_download_image
dedent|''
name|'def'
name|'test_download_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_download_params'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_make_uuid_stack'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'a'
op|','
op|'**'
name|'kw'
op|':'
op|'['
string|"'uuid1'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'download_vhd'"
op|','
op|'**'
name|'params'
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
name|'self'
op|'.'
name|'store'
op|'.'
name|'download_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
string|"'fake_image_uuid'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
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
name|'vm_utils'
op|','
string|"'_make_uuid_stack'"
op|','
name|'return_value'
op|'='
op|'['
string|"'uuid1'"
op|']'
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'random'
op|','
string|"'shuffle'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'time'
op|','
string|"'sleep'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|"'nova.virt.xenapi.client.session'"
op|')'
op|','
nl|'\n'
string|"'debug'"
op|')'
newline|'\n'
DECL|member|test_download_image_retry
name|'def'
name|'test_download_image_retry'
op|'('
name|'self'
op|','
name|'mock_log_debug'
op|','
nl|'\n'
name|'mock_sleep'
op|','
name|'mock_shuffle'
op|','
nl|'\n'
name|'mock_make_uuid_stack'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_download_params'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'glance_num_retries'
op|'='
number|'2'
op|')'
newline|'\n'
nl|'\n'
name|'params'
op|'.'
name|'pop'
op|'('
string|'"glance_port"'
op|')'
newline|'\n'
name|'params'
op|'.'
name|'pop'
op|'('
string|'"glance_host"'
op|')'
newline|'\n'
name|'calls'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
string|"'glance'"
op|','
string|"'download_vhd'"
op|','
name|'glance_port'
op|'='
number|'9292'
op|','
nl|'\n'
name|'glance_host'
op|'='
string|"'10.0.1.1'"
op|','
op|'**'
name|'params'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
string|"'glance'"
op|','
string|"'download_vhd'"
op|','
name|'glance_port'
op|'='
number|'9293'
op|','
nl|'\n'
name|'glance_host'
op|'='
string|"'10.0.0.1'"
op|','
op|'**'
name|'params'
op|')'
op|']'
newline|'\n'
name|'log_calls'
op|'='
op|'['
name|'mock'
op|'.'
name|'call'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
op|'{'
string|"'callback_result'"
op|':'
string|"'10.0.1.1'"
op|','
nl|'\n'
string|"'attempts'"
op|':'
number|'3'
op|','
string|"'attempt'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'fn'"
op|':'
string|"'download_vhd'"
op|','
nl|'\n'
string|"'plugin'"
op|':'
string|"'glance'"
op|'}'
op|')'
op|','
nl|'\n'
name|'mock'
op|'.'
name|'call'
op|'('
name|'mock'
op|'.'
name|'ANY'
op|','
op|'{'
string|"'callback_result'"
op|':'
string|"'10.0.0.1'"
op|','
nl|'\n'
string|"'attempts'"
op|':'
number|'3'
op|','
string|"'attempt'"
op|':'
number|'2'
op|','
nl|'\n'
string|"'fn'"
op|':'
string|"'download_vhd'"
op|','
nl|'\n'
string|"'plugin'"
op|':'
string|"'glance'"
op|'}'
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'glance_api_servers'
op|'='
op|'['
string|"'10.0.1.1:9292'"
op|','
nl|'\n'
string|"'http://10.0.0.1:9293'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'glance_api_servers'
op|'='
name|'glance_api_servers'
op|')'
newline|'\n'
nl|'\n'
name|'with'
op|'('
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|')'
nl|'\n'
op|')'
name|'as'
name|'mock_call_plugin_serialized'
op|':'
newline|'\n'
indent|'            '
name|'error_details'
op|'='
op|'['
string|'""'
op|','
string|'""'
op|','
string|'"RetryableError"'
op|','
string|'""'
op|']'
newline|'\n'
name|'error'
op|'='
name|'self'
op|'.'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'details'
op|'='
name|'error_details'
op|')'
newline|'\n'
name|'mock_call_plugin_serialized'
op|'.'
name|'side_effect'
op|'='
op|'['
name|'error'
op|','
string|'"success"'
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'store'
op|'.'
name|'download_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'session'
op|','
nl|'\n'
string|"'fake_image_uuid'"
op|')'
newline|'\n'
nl|'\n'
name|'mock_call_plugin_serialized'
op|'.'
name|'assert_has_calls'
op|'('
name|'calls'
op|')'
newline|'\n'
name|'mock_log_debug'
op|'.'
name|'assert_has_calls'
op|'('
name|'log_calls'
op|','
name|'any_order'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_upload_params
dedent|''
dedent|''
name|'def'
name|'_get_upload_params'
op|'('
name|'self'
op|','
name|'auto_disk_config'
op|'='
name|'True'
op|','
nl|'\n'
name|'expected_os_type'
op|'='
string|"'default'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_params'
op|'('
op|')'
newline|'\n'
name|'params'
op|'['
string|"'vdi_uuids'"
op|']'
op|'='
op|'['
string|"'fake_vdi_uuid'"
op|']'
newline|'\n'
name|'params'
op|'['
string|"'properties'"
op|']'
op|'='
op|'{'
string|"'auto_disk_config'"
op|':'
name|'auto_disk_config'
op|','
nl|'\n'
string|"'os_type'"
op|':'
name|'expected_os_type'
op|'}'
newline|'\n'
name|'return'
name|'params'
newline|'\n'
nl|'\n'
DECL|member|_test_upload_image
dedent|''
name|'def'
name|'_test_upload_image'
op|'('
name|'self'
op|','
name|'auto_disk_config'
op|','
name|'expected_os_type'
op|'='
string|"'default'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_upload_params'
op|'('
name|'auto_disk_config'
op|','
name|'expected_os_type'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'upload_vhd'"
op|','
op|'**'
name|'params'
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
name|'self'
op|'.'
name|'store'
op|'.'
name|'upload_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
op|'['
string|"'fake_vdi_uuid'"
op|']'
op|','
string|"'fake_image_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upload_image
dedent|''
name|'def'
name|'test_upload_image'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_test_upload_image'
op|'('
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upload_image_None_os_type
dedent|''
name|'def'
name|'test_upload_image_None_os_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'instance'
op|'['
string|"'os_type'"
op|']'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_test_upload_image'
op|'('
name|'True'
op|','
string|"'linux'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upload_image_no_os_type
dedent|''
name|'def'
name|'test_upload_image_no_os_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'del'
name|'self'
op|'.'
name|'instance'
op|'['
string|"'os_type'"
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_test_upload_image'
op|'('
name|'True'
op|','
string|"'linux'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upload_image_auto_config_disk_disabled
dedent|''
name|'def'
name|'test_upload_image_auto_config_disk_disabled'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sys_meta'
op|'='
op|'['
op|'{'
string|'"key"'
op|':'
string|'"image_auto_disk_config"'
op|','
string|'"value"'
op|':'
string|'"Disabled"'
op|'}'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'instance'
op|'['
string|'"system_metadata"'
op|']'
op|'='
name|'sys_meta'
newline|'\n'
name|'self'
op|'.'
name|'_test_upload_image'
op|'('
string|'"disabled"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upload_image_raises_exception
dedent|''
name|'def'
name|'test_upload_image_raises_exception'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_upload_params'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'upload_vhd'"
op|','
nl|'\n'
op|'**'
name|'params'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'RuntimeError'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'RuntimeError'
op|','
name|'self'
op|'.'
name|'store'
op|'.'
name|'upload_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
op|'['
string|"'fake_vdi_uuid'"
op|']'
op|','
string|"'fake_image_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upload_image_retries_then_raises_exception
dedent|''
name|'def'
name|'test_upload_image_retries_then_raises_exception'
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
name|'glance_num_retries'
op|'='
number|'2'
op|')'
newline|'\n'
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_upload_params'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'time'
op|','
string|"'sleep'"
op|')'
newline|'\n'
name|'error_details'
op|'='
op|'['
string|'""'
op|','
string|'""'
op|','
string|'"RetryableError"'
op|','
string|'""'
op|']'
newline|'\n'
name|'error'
op|'='
name|'self'
op|'.'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'details'
op|'='
name|'error_details'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'upload_vhd'"
op|','
nl|'\n'
op|'**'
name|'params'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'error'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.5'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'upload_vhd'"
op|','
nl|'\n'
op|'**'
name|'params'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'error'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'upload_vhd'"
op|','
nl|'\n'
op|'**'
name|'params'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'error'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'CouldNotUploadImage'
op|','
nl|'\n'
name|'self'
op|'.'
name|'store'
op|'.'
name|'upload_image'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
op|'['
string|"'fake_vdi_uuid'"
op|']'
op|','
string|"'fake_image_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_upload_image_retries_on_signal_exception
dedent|''
name|'def'
name|'test_upload_image_retries_on_signal_exception'
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
name|'glance_num_retries'
op|'='
number|'2'
op|')'
newline|'\n'
name|'params'
op|'='
name|'self'
op|'.'
name|'_get_upload_params'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'session'
op|','
string|"'call_plugin_serialized'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'time'
op|','
string|"'sleep'"
op|')'
newline|'\n'
name|'error_details'
op|'='
op|'['
string|'""'
op|','
string|'"task signaled"'
op|','
string|'""'
op|','
string|'""'
op|']'
newline|'\n'
name|'error'
op|'='
name|'self'
op|'.'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'details'
op|'='
name|'error_details'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'upload_vhd'"
op|','
nl|'\n'
op|'**'
name|'params'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'error'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'0.5'
op|')'
newline|'\n'
comment|'# Note(johngarbutt) XenServer 6.1 and later has this error'
nl|'\n'
name|'error_details'
op|'='
op|'['
string|'""'
op|','
string|'"signal: SIGTERM"'
op|','
string|'""'
op|','
string|'""'
op|']'
newline|'\n'
name|'error'
op|'='
name|'self'
op|'.'
name|'session'
op|'.'
name|'XenAPI'
op|'.'
name|'Failure'
op|'('
name|'details'
op|'='
name|'error_details'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'upload_vhd'"
op|','
nl|'\n'
op|'**'
name|'params'
op|')'
op|'.'
name|'AndRaise'
op|'('
name|'error'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'session'
op|'.'
name|'call_plugin_serialized'
op|'('
string|"'glance'"
op|','
string|"'upload_vhd'"
op|','
nl|'\n'
op|'**'
name|'params'
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
name|'self'
op|'.'
name|'store'
op|'.'
name|'upload_image'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'self'
op|'.'
name|'session'
op|','
name|'self'
op|'.'
name|'instance'
op|','
nl|'\n'
op|'['
string|"'fake_vdi_uuid'"
op|']'
op|','
string|"'fake_image_uuid'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'VerifyAll'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
