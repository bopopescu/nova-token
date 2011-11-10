begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2010 Citrix Systems, Inc.'
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
string|'"""Stubouts, mocks and fixtures for the test suite"""'
newline|'\n'
nl|'\n'
name|'import'
name|'eventlet'
newline|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
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
name|'import'
name|'volume_utils'
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
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'vmops'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_instance_snapshot
name|'def'
name|'stubout_instance_snapshot'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|fake_fetch_image
name|'def'
name|'fake_fetch_image'
op|'('
name|'cls'
op|','
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'image'
op|','
name|'user'
op|','
nl|'\n'
name|'project'
op|','
name|'type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
op|'.'
name|'fake'
name|'import'
name|'create_vdi'
newline|'\n'
name|'name_label'
op|'='
string|'"instance-%s"'
op|'%'
name|'instance'
op|'.'
name|'id'
newline|'\n'
comment|'#TODO: create fake SR record'
nl|'\n'
name|'sr_ref'
op|'='
string|'"fakesr"'
newline|'\n'
name|'vdi_ref'
op|'='
name|'create_vdi'
op|'('
name|'name_label'
op|'='
name|'name_label'
op|','
name|'read_only'
op|'='
name|'False'
op|','
nl|'\n'
name|'sr_ref'
op|'='
name|'sr_ref'
op|','
name|'sharable'
op|'='
name|'False'
op|')'
newline|'\n'
name|'vdi_rec'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_record"'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'vdi_uuid'
op|'='
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
name|'return'
op|'['
name|'dict'
op|'('
name|'vdi_type'
op|'='
string|"'os'"
op|','
name|'vdi_uuid'
op|'='
name|'vdi_uuid'
op|')'
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|'.'
name|'VMHelper'
op|','
string|"'fetch_image'"
op|','
name|'fake_fetch_image'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_parse_xmlrpc_value
name|'def'
name|'fake_parse_xmlrpc_value'
op|'('
name|'val'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'val'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'xenapi_conn'
op|','
string|"'_parse_xmlrpc_value'"
op|','
name|'fake_parse_xmlrpc_value'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_wait_for_vhd_coalesce
name|'def'
name|'fake_wait_for_vhd_coalesce'
op|'('
name|'session'
op|','
name|'instance_id'
op|','
name|'sr_ref'
op|','
name|'vdi_ref'
op|','
nl|'\n'
name|'original_parent_uuid'
op|')'
op|':'
newline|'\n'
comment|'#TODO(sirp): Should we actually fake out the data here'
nl|'\n'
indent|'        '
name|'return'
string|'"fakeparent"'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'wait_for_vhd_coalesce'"
op|','
name|'fake_wait_for_vhd_coalesce'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_session
dedent|''
name|'def'
name|'stubout_session'
op|'('
name|'stubs'
op|','
name|'cls'
op|','
name|'product_version'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out three methods from XenAPISession"""'
newline|'\n'
DECL|function|fake_import
name|'def'
name|'fake_import'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Stubs out get_imported_xenapi of XenAPISession"""'
newline|'\n'
name|'fake_module'
op|'='
string|"'nova.virt.xenapi.fake'"
newline|'\n'
name|'from_list'
op|'='
op|'['
string|"'fake'"
op|']'
newline|'\n'
name|'return'
name|'__import__'
op|'('
name|'fake_module'
op|','
name|'globals'
op|'('
op|')'
op|','
name|'locals'
op|'('
op|')'
op|','
name|'from_list'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|','
string|"'_create_session'"
op|','
nl|'\n'
name|'lambda'
name|'s'
op|','
name|'url'
op|':'
name|'cls'
op|'('
name|'url'
op|')'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|','
string|"'get_imported_xenapi'"
op|','
nl|'\n'
name|'fake_import'
op|')'
newline|'\n'
name|'if'
name|'product_version'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'product_version'
op|'='
op|'('
number|'5'
op|','
number|'6'
op|','
number|'2'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|','
string|"'get_product_version'"
op|','
nl|'\n'
name|'lambda'
name|'s'
op|':'
name|'product_version'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_get_target
dedent|''
name|'def'
name|'stub_out_get_target'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out _get_target in volume_utils"""'
newline|'\n'
DECL|function|fake_get_target
name|'def'
name|'fake_get_target'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
name|'None'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'volume_utils'
op|','
string|"'_get_target'"
op|','
name|'fake_get_target'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_get_this_vm_uuid
dedent|''
name|'def'
name|'stubout_get_this_vm_uuid'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|f
indent|'    '
name|'def'
name|'f'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vms'
op|'='
op|'['
name|'rec'
op|'['
string|"'uuid'"
op|']'
name|'for'
name|'ref'
op|','
name|'rec'
nl|'\n'
name|'in'
name|'fake'
op|'.'
name|'get_all_records'
op|'('
string|"'VM'"
op|')'
op|'.'
name|'iteritems'
op|'('
op|')'
nl|'\n'
name|'if'
name|'rec'
op|'['
string|"'is_control_domain'"
op|']'
op|']'
newline|'\n'
name|'return'
name|'vms'
op|'['
number|'0'
op|']'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'get_this_vm_uuid'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_stream_disk
dedent|''
name|'def'
name|'stubout_stream_disk'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|f
indent|'    '
name|'def'
name|'f'
op|'('
name|'_1'
op|','
name|'_2'
op|','
name|'_3'
op|','
name|'_4'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_stream_disk'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_is_vdi_pv
dedent|''
name|'def'
name|'stubout_is_vdi_pv'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|f
indent|'    '
name|'def'
name|'f'
op|'('
name|'_1'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_is_vdi_pv'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_determine_is_pv_objectstore
dedent|''
name|'def'
name|'stubout_determine_is_pv_objectstore'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Assumes VMs never have PV kernels"""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|'.'
name|'VMHelper'
op|','
string|"'_determine_is_pv_objectstore'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_lookup_image
dedent|''
name|'def'
name|'stubout_lookup_image'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simulates a failure in lookup image."""'
newline|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
name|'_1'
op|','
name|'_2'
op|','
name|'_3'
op|','
name|'_4'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'Exception'
op|'('
string|'"Test Exception raised by fake lookup_image"'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'lookup_image'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_fetch_image_glance_disk
dedent|''
name|'def'
name|'stubout_fetch_image_glance_disk'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simulates a failure in fetch image_glance_disk."""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'fake'
op|'.'
name|'Failure'
op|'('
string|'"Test Exception raised by "'
op|'+'
nl|'\n'
string|'"fake fetch_image_glance_disk"'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|'.'
name|'VMHelper'
op|','
string|"'_fetch_image_glance_disk'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_create_vm
dedent|''
name|'def'
name|'stubout_create_vm'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simulates a failure in create_vm."""'
newline|'\n'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'fake'
op|'.'
name|'Failure'
op|'('
string|'"Test Exception raised by "'
op|'+'
nl|'\n'
string|'"fake create_vm"'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|'.'
name|'VMHelper'
op|','
string|"'create_vm'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_loopingcall_start
dedent|''
name|'def'
name|'stubout_loopingcall_start'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_start
indent|'    '
name|'def'
name|'fake_start'
op|'('
name|'self'
op|','
name|'interval'
op|','
name|'now'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'f'
op|'('
op|'*'
name|'self'
op|'.'
name|'args'
op|','
op|'**'
name|'self'
op|'.'
name|'kw'
op|')'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|'.'
name|'LoopingCall'
op|','
string|"'start'"
op|','
name|'fake_start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_loopingcall_delay
dedent|''
name|'def'
name|'stubout_loopingcall_delay'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_start
indent|'    '
name|'def'
name|'fake_start'
op|'('
name|'self'
op|','
name|'interval'
op|','
name|'now'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_running'
op|'='
name|'True'
newline|'\n'
name|'eventlet'
op|'.'
name|'sleep'
op|'('
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'f'
op|'('
op|'*'
name|'self'
op|'.'
name|'args'
op|','
op|'**'
name|'self'
op|'.'
name|'kw'
op|')'
newline|'\n'
comment|'# This would fail before parallel xenapi calls were fixed'
nl|'\n'
name|'assert'
name|'self'
op|'.'
name|'_running'
op|'=='
name|'False'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'utils'
op|'.'
name|'LoopingCall'
op|','
string|"'start'"
op|','
name|'fake_start'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeSessionForVMTests
dedent|''
name|'class'
name|'FakeSessionForVMTests'
op|'('
name|'fake'
op|'.'
name|'SessionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Stubs out a XenAPISession for VM tests """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'uri'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeSessionForVMTests'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'uri'
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_call_plugin
dedent|''
name|'def'
name|'host_call_plugin'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'_2'
op|','
name|'plugin'
op|','
name|'method'
op|','
name|'_5'
op|')'
op|':'
newline|'\n'
comment|"# If the call is for 'copy_kernel_vdi' return None."
nl|'\n'
indent|'        '
name|'if'
name|'method'
op|'=='
string|"'copy_kernel_vdi'"
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'sr_ref'
op|'='
name|'fake'
op|'.'
name|'get_all'
op|'('
string|"'SR'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vdi_ref'
op|'='
name|'fake'
op|'.'
name|'create_vdi'
op|'('
string|"''"
op|','
name|'False'
op|','
name|'sr_ref'
op|','
name|'False'
op|')'
newline|'\n'
name|'vdi_rec'
op|'='
name|'fake'
op|'.'
name|'get_record'
op|'('
string|"'VDI'"
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'if'
name|'plugin'
op|'=='
string|'"glance"'
name|'and'
name|'method'
op|'=='
string|'"download_vhd"'
op|':'
newline|'\n'
indent|'            '
name|'ret_str'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
op|'['
name|'dict'
op|'('
name|'vdi_type'
op|'='
string|"'os'"
op|','
nl|'\n'
name|'vdi_uuid'
op|'='
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'ret_str'
op|'='
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'return'
string|"'<string>%s</string>'"
op|'%'
name|'ret_str'
newline|'\n'
nl|'\n'
DECL|member|host_call_plugin_swap
dedent|''
name|'def'
name|'host_call_plugin_swap'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'_2'
op|','
name|'plugin'
op|','
name|'method'
op|','
name|'_5'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'sr_ref'
op|'='
name|'fake'
op|'.'
name|'get_all'
op|'('
string|"'SR'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'vdi_ref'
op|'='
name|'fake'
op|'.'
name|'create_vdi'
op|'('
string|"''"
op|','
name|'False'
op|','
name|'sr_ref'
op|','
name|'False'
op|')'
newline|'\n'
name|'vdi_rec'
op|'='
name|'fake'
op|'.'
name|'get_record'
op|'('
string|"'VDI'"
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'if'
name|'plugin'
op|'=='
string|'"glance"'
name|'and'
name|'method'
op|'=='
string|'"download_vhd"'
op|':'
newline|'\n'
indent|'            '
name|'swap_vdi_ref'
op|'='
name|'fake'
op|'.'
name|'create_vdi'
op|'('
string|"''"
op|','
name|'False'
op|','
name|'sr_ref'
op|','
name|'False'
op|')'
newline|'\n'
name|'swap_vdi_rec'
op|'='
name|'fake'
op|'.'
name|'get_record'
op|'('
string|"'VDI'"
op|','
name|'swap_vdi_ref'
op|')'
newline|'\n'
name|'ret_str'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
nl|'\n'
op|'['
name|'dict'
op|'('
name|'vdi_type'
op|'='
string|"'os'"
op|','
name|'vdi_uuid'
op|'='
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'vdi_type'
op|'='
string|"'swap'"
op|','
name|'vdi_uuid'
op|'='
name|'swap_vdi_rec'
op|'['
string|"'uuid'"
op|']'
op|')'
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'ret_str'
op|'='
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
newline|'\n'
dedent|''
name|'return'
string|"'<string>%s</string>'"
op|'%'
name|'ret_str'
newline|'\n'
nl|'\n'
DECL|member|VM_start
dedent|''
name|'def'
name|'VM_start'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'ref'
op|','
name|'_2'
op|','
name|'_3'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'fake'
op|'.'
name|'get_record'
op|'('
string|"'VM'"
op|','
name|'ref'
op|')'
newline|'\n'
name|'if'
name|'vm'
op|'['
string|"'power_state'"
op|']'
op|'!='
string|"'Halted'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'fake'
op|'.'
name|'Failure'
op|'('
op|'['
string|"'VM_BAD_POWER_STATE'"
op|','
name|'ref'
op|','
string|"'Halted'"
op|','
nl|'\n'
name|'vm'
op|'['
string|"'power_state'"
op|']'
op|']'
op|')'
newline|'\n'
dedent|''
name|'vm'
op|'['
string|"'power_state'"
op|']'
op|'='
string|"'Running'"
newline|'\n'
name|'vm'
op|'['
string|"'is_a_template'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vm'
op|'['
string|"'is_control_domain'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vm'
op|'['
string|"'domid'"
op|']'
op|'='
name|'random'
op|'.'
name|'randrange'
op|'('
number|'1'
op|','
number|'1'
op|'<<'
number|'16'
op|')'
newline|'\n'
nl|'\n'
DECL|member|VM_snapshot
dedent|''
name|'def'
name|'VM_snapshot'
op|'('
name|'self'
op|','
name|'session_ref'
op|','
name|'vm_ref'
op|','
name|'label'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'status'
op|'='
string|'"Running"'
newline|'\n'
name|'template_vm_ref'
op|'='
name|'fake'
op|'.'
name|'create_vm'
op|'('
name|'label'
op|','
name|'status'
op|','
name|'is_a_template'
op|'='
name|'True'
op|','
nl|'\n'
name|'is_control_domain'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'sr_ref'
op|'='
string|'"fakesr"'
newline|'\n'
name|'template_vdi_ref'
op|'='
name|'fake'
op|'.'
name|'create_vdi'
op|'('
name|'label'
op|','
name|'read_only'
op|'='
name|'True'
op|','
nl|'\n'
name|'sr_ref'
op|'='
name|'sr_ref'
op|','
name|'sharable'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
name|'template_vbd_ref'
op|'='
name|'fake'
op|'.'
name|'create_vbd'
op|'('
name|'template_vm_ref'
op|','
name|'template_vdi_ref'
op|')'
newline|'\n'
name|'return'
name|'template_vm_ref'
newline|'\n'
nl|'\n'
DECL|member|VDI_destroy
dedent|''
name|'def'
name|'VDI_destroy'
op|'('
name|'self'
op|','
name|'session_ref'
op|','
name|'vdi_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake'
op|'.'
name|'destroy_vdi'
op|'('
name|'vdi_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|VM_destroy
dedent|''
name|'def'
name|'VM_destroy'
op|'('
name|'self'
op|','
name|'session_ref'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fake'
op|'.'
name|'destroy_vm'
op|'('
name|'vm_ref'
op|')'
newline|'\n'
nl|'\n'
DECL|member|SR_scan
dedent|''
name|'def'
name|'SR_scan'
op|'('
name|'self'
op|','
name|'session_ref'
op|','
name|'sr_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|VDI_set_name_label
dedent|''
name|'def'
name|'VDI_set_name_label'
op|'('
name|'self'
op|','
name|'session_ref'
op|','
name|'vdi_ref'
op|','
name|'name_label'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_vm_methods
dedent|''
dedent|''
name|'def'
name|'stub_out_vm_methods'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_shutdown
indent|'    '
name|'def'
name|'fake_shutdown'
op|'('
name|'self'
op|','
name|'inst'
op|','
name|'vm'
op|','
name|'method'
op|'='
string|'"clean"'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_acquire_bootlock
dedent|''
name|'def'
name|'fake_acquire_bootlock'
op|'('
name|'self'
op|','
name|'vm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_release_bootlock
dedent|''
name|'def'
name|'fake_release_bootlock'
op|'('
name|'self'
op|','
name|'vm'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_spawn_rescue
dedent|''
name|'def'
name|'fake_spawn_rescue'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'inst'
op|','
name|'network_info'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'inst'
op|'.'
name|'_rescue'
op|'='
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|'"_shutdown"'
op|','
name|'fake_shutdown'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|'"_acquire_bootlock"'
op|','
name|'fake_acquire_bootlock'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|'"_release_bootlock"'
op|','
name|'fake_release_bootlock'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|'"spawn_rescue"'
op|','
name|'fake_spawn_rescue'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeSessionForVolumeTests
dedent|''
name|'class'
name|'FakeSessionForVolumeTests'
op|'('
name|'fake'
op|'.'
name|'SessionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Stubs out a XenAPISession for Volume tests """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'uri'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeSessionForVolumeTests'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'uri'
op|')'
newline|'\n'
nl|'\n'
DECL|member|VDI_introduce
dedent|''
name|'def'
name|'VDI_introduce'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'uuid'
op|','
name|'_2'
op|','
name|'_3'
op|','
name|'_4'
op|','
name|'_5'
op|','
nl|'\n'
name|'_6'
op|','
name|'_7'
op|','
name|'_8'
op|','
name|'_9'
op|','
name|'_10'
op|','
name|'_11'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'valid_vdi'
op|'='
name|'False'
newline|'\n'
name|'refs'
op|'='
name|'fake'
op|'.'
name|'get_all'
op|'('
string|"'VDI'"
op|')'
newline|'\n'
name|'for'
name|'ref'
name|'in'
name|'refs'
op|':'
newline|'\n'
indent|'            '
name|'rec'
op|'='
name|'fake'
op|'.'
name|'get_record'
op|'('
string|"'VDI'"
op|','
name|'ref'
op|')'
newline|'\n'
name|'if'
name|'rec'
op|'['
string|"'uuid'"
op|']'
op|'=='
name|'uuid'
op|':'
newline|'\n'
indent|'                '
name|'valid_vdi'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'not'
name|'valid_vdi'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'fake'
op|'.'
name|'Failure'
op|'('
op|'['
op|'['
string|"'INVALID_VDI'"
op|','
string|"'session'"
op|','
name|'self'
op|'.'
name|'_session'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeSessionForVolumeFailedTests
dedent|''
dedent|''
dedent|''
name|'class'
name|'FakeSessionForVolumeFailedTests'
op|'('
name|'FakeSessionForVolumeTests'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Stubs out a XenAPISession for Volume tests: it injects failures """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'uri'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeSessionForVolumeFailedTests'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'uri'
op|')'
newline|'\n'
nl|'\n'
DECL|member|VDI_introduce
dedent|''
name|'def'
name|'VDI_introduce'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'uuid'
op|','
name|'_2'
op|','
name|'_3'
op|','
name|'_4'
op|','
name|'_5'
op|','
nl|'\n'
name|'_6'
op|','
name|'_7'
op|','
name|'_8'
op|','
name|'_9'
op|','
name|'_10'
op|','
name|'_11'
op|')'
op|':'
newline|'\n'
comment|'# This is for testing failure'
nl|'\n'
indent|'        '
name|'raise'
name|'fake'
op|'.'
name|'Failure'
op|'('
op|'['
op|'['
string|"'INVALID_VDI'"
op|','
string|"'session'"
op|','
name|'self'
op|'.'
name|'_session'
op|']'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|PBD_unplug
dedent|''
name|'def'
name|'PBD_unplug'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'rec'
op|'='
name|'fake'
op|'.'
name|'get_record'
op|'('
string|"'PBD'"
op|','
name|'ref'
op|')'
newline|'\n'
name|'rec'
op|'['
string|"'currently-attached'"
op|']'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|SR_forget
dedent|''
name|'def'
name|'SR_forget'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|FakeSessionForMigrationTests
dedent|''
dedent|''
name|'class'
name|'FakeSessionForMigrationTests'
op|'('
name|'fake'
op|'.'
name|'SessionBase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Stubs out a XenAPISession for Migration tests"""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'uri'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeSessionForMigrationTests'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'uri'
op|')'
newline|'\n'
nl|'\n'
DECL|member|VDI_get_by_uuid
dedent|''
name|'def'
name|'VDI_get_by_uuid'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'hurr'"
newline|'\n'
nl|'\n'
DECL|member|VM_start
dedent|''
name|'def'
name|'VM_start'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'ref'
op|','
name|'_2'
op|','
name|'_3'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm'
op|'='
name|'fake'
op|'.'
name|'get_record'
op|'('
string|"'VM'"
op|','
name|'ref'
op|')'
newline|'\n'
name|'if'
name|'vm'
op|'['
string|"'power_state'"
op|']'
op|'!='
string|"'Halted'"
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'fake'
op|'.'
name|'Failure'
op|'('
op|'['
string|"'VM_BAD_POWER_STATE'"
op|','
name|'ref'
op|','
string|"'Halted'"
op|','
nl|'\n'
name|'vm'
op|'['
string|"'power_state'"
op|']'
op|']'
op|')'
newline|'\n'
dedent|''
name|'vm'
op|'['
string|"'power_state'"
op|']'
op|'='
string|"'Running'"
newline|'\n'
name|'vm'
op|'['
string|"'is_a_template'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vm'
op|'['
string|"'is_control_domain'"
op|']'
op|'='
name|'False'
newline|'\n'
name|'vm'
op|'['
string|"'domid'"
op|']'
op|'='
name|'random'
op|'.'
name|'randrange'
op|'('
number|'1'
op|','
number|'1'
op|'<<'
number|'16'
op|')'
newline|'\n'
nl|'\n'
DECL|member|VM_set_name_label
dedent|''
name|'def'
name|'VM_set_name_label'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|VDI_set_name_label
dedent|''
name|'def'
name|'VDI_set_name_label'
op|'('
name|'self'
op|','
name|'session_ref'
op|','
name|'vdi_ref'
op|','
name|'name_label'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stub_out_migration_methods
dedent|''
dedent|''
name|'def'
name|'stub_out_migration_methods'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_create_snapshot
indent|'    '
name|'def'
name|'fake_create_snapshot'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'vm_ref'"
op|','
name|'dict'
op|'('
name|'image'
op|'='
string|"'foo'"
op|','
name|'snap'
op|'='
string|"'bar'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|fake_get_vdi
name|'def'
name|'fake_get_vdi'
op|'('
name|'cls'
op|','
name|'session'
op|','
name|'vm_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vdi_ref'
op|'='
name|'fake'
op|'.'
name|'create_vdi'
op|'('
name|'name_label'
op|'='
string|"'derp'"
op|','
name|'read_only'
op|'='
name|'False'
op|','
nl|'\n'
name|'sr_ref'
op|'='
string|"'herp'"
op|','
name|'sharable'
op|'='
name|'False'
op|')'
newline|'\n'
name|'vdi_rec'
op|'='
name|'session'
op|'.'
name|'call_xenapi'
op|'('
string|'"VDI.get_record"'
op|','
name|'vdi_ref'
op|')'
newline|'\n'
name|'return'
name|'vdi_ref'
op|','
op|'{'
string|"'uuid'"
op|':'
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
op|','
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_shutdown
dedent|''
name|'def'
name|'fake_shutdown'
op|'('
name|'self'
op|','
name|'inst'
op|','
name|'vm'
op|','
name|'hard'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|fake_sr
name|'def'
name|'fake_sr'
op|'('
name|'cls'
op|','
name|'session'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|function|fake_get_sr_path
name|'def'
name|'fake_get_sr_path'
op|'('
name|'cls'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|'"fake"'
newline|'\n'
nl|'\n'
DECL|function|fake_destroy
dedent|''
name|'def'
name|'fake_destroy'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_reset_network
dedent|''
name|'def'
name|'fake_reset_network'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|"'_destroy'"
op|','
name|'fake_destroy'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|'.'
name|'VMHelper'
op|','
string|"'scan_default_sr'"
op|','
name|'fake_sr'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|'.'
name|'VMHelper'
op|','
string|"'scan_sr'"
op|','
name|'fake_sr'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|"'_create_snapshot'"
op|','
name|'fake_create_snapshot'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|'.'
name|'VMHelper'
op|','
string|"'get_vdi_for_vm_safely'"
op|','
name|'fake_get_vdi'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|','
string|"'wait_for_task'"
op|','
name|'lambda'
name|'x'
op|','
name|'y'
op|','
name|'z'
op|':'
name|'None'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|'.'
name|'VMHelper'
op|','
string|"'get_sr_path'"
op|','
name|'fake_get_sr_path'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|"'reset_network'"
op|','
name|'fake_reset_network'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|"'_shutdown'"
op|','
name|'fake_shutdown'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
