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
name|'random'
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
name|'import'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'xenapi'
name|'import'
name|'connection'
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
nl|'\n'
nl|'\n'
DECL|function|stubout_firewall_driver
name|'def'
name|'stubout_firewall_driver'
op|'('
name|'stubs'
op|','
name|'conn'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|function|fake_none
indent|'    '
name|'def'
name|'fake_none'
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
newline|'\n'
nl|'\n'
dedent|''
name|'vmops'
op|'='
name|'conn'
op|'.'
name|'_vmops'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'firewall_driver'
op|','
string|"'prepare_instance_filter'"
op|','
name|'fake_none'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vmops'
op|'.'
name|'firewall_driver'
op|','
string|"'instance_filter_exists'"
op|','
name|'fake_none'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_instance_snapshot
dedent|''
name|'def'
name|'stubout_instance_snapshot'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_fetch_image
indent|'    '
name|'def'
name|'fake_fetch_image'
op|'('
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'image'
op|','
name|'type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'{'
string|"'root'"
op|':'
name|'dict'
op|'('
name|'uuid'
op|'='
name|'_make_fake_vdi'
op|'('
op|')'
op|','
name|'file'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
string|"'kernel'"
op|':'
name|'dict'
op|'('
name|'uuid'
op|'='
name|'_make_fake_vdi'
op|'('
op|')'
op|','
name|'file'
op|'='
name|'None'
op|')'
op|','
nl|'\n'
string|"'ramdisk'"
op|':'
name|'dict'
op|'('
name|'uuid'
op|'='
name|'_make_fake_vdi'
op|'('
op|')'
op|','
name|'file'
op|'='
name|'None'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'fetch_image'"
op|','
name|'fake_fetch_image'
op|')'
newline|'\n'
nl|'\n'
DECL|function|fake_wait_for_vhd_coalesce
name|'def'
name|'fake_wait_for_vhd_coalesce'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
comment|'#TODO(sirp): Should we actually fake out the data here'
nl|'\n'
indent|'        '
name|'return'
string|'"fakeparent"'
op|','
string|'"fakebase"'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_wait_for_vhd_coalesce'"
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
op|'('
number|'5'
op|','
number|'6'
op|','
number|'2'
op|')'
op|','
op|'**'
name|'opt_args'
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
op|','
op|'**'
name|'opt_args'
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
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'xenapi_conn'
op|'.'
name|'XenAPISession'
op|','
string|"'_get_product_version'"
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
DECL|function|stubout_image_service_download
dedent|''
name|'def'
name|'stubout_image_service_download'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
DECL|function|fake_download
indent|'    '
name|'def'
name|'fake_download'
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
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'image'
op|'.'
name|'fake'
op|'.'
name|'_FakeImageService'
op|','
nl|'\n'
string|"'download'"
op|','
name|'fake_download'
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
DECL|function|fake_stream_disk
indent|'    '
name|'def'
name|'fake_stream_disk'
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
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_stream_disk'"
op|','
name|'fake_stream_disk'
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
string|'"""Assumes VMs stu have PV kernels"""'
newline|'\n'
nl|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
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
op|','
string|"'_determine_is_pv_objectstore'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|stubout_is_snapshot
dedent|''
name|'def'
name|'stubout_is_snapshot'
op|'('
name|'stubs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Always returns true\n        xenapi fake driver does not create vmrefs for snapshots """'
newline|'\n'
nl|'\n'
DECL|function|f
name|'def'
name|'f'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'is_snapshot'"
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
DECL|function|stubout_fetch_disk_image
dedent|''
name|'def'
name|'stubout_fetch_disk_image'
op|'('
name|'stubs'
op|','
name|'raise_failure'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Simulates a failure in fetch image_glance_disk."""'
newline|'\n'
nl|'\n'
DECL|function|_fake_fetch_disk_image
name|'def'
name|'_fake_fetch_disk_image'
op|'('
name|'context'
op|','
name|'session'
op|','
name|'instance'
op|','
name|'image'
op|','
nl|'\n'
name|'image_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'raise_failure'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'fake'
op|'.'
name|'Failure'
op|'('
string|'"Test Exception raised by "'
nl|'\n'
string|'"fake fetch_image_glance_disk"'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'image_type'
op|'=='
name|'vm_utils'
op|'.'
name|'ImageType'
op|'.'
name|'KERNEL'
op|':'
newline|'\n'
indent|'            '
name|'filename'
op|'='
string|'"kernel"'
newline|'\n'
dedent|''
name|'elif'
name|'image_type'
op|'=='
name|'vm_utils'
op|'.'
name|'ImageType'
op|'.'
name|'RAMDISK'
op|':'
newline|'\n'
indent|'            '
name|'filename'
op|'='
string|'"ramdisk"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'filename'
op|'='
string|'"unknown"'
newline|'\n'
nl|'\n'
dedent|''
name|'vdi_type'
op|'='
name|'vm_utils'
op|'.'
name|'ImageType'
op|'.'
name|'to_string'
op|'('
name|'image_type'
op|')'
newline|'\n'
name|'return'
op|'{'
name|'vdi_type'
op|':'
name|'dict'
op|'('
name|'uuid'
op|'='
name|'None'
op|','
name|'file'
op|'='
name|'filename'
op|')'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_fetch_disk_image'"
op|','
name|'_fake_fetch_disk_image'
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
DECL|function|f
name|'def'
name|'f'
op|'('
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
op|','
string|"'create_vm'"
op|','
name|'f'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_make_fake_vdi
dedent|''
name|'def'
name|'_make_fake_vdi'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
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
name|'sr_ref'
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
name|'return'
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
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
nl|'\n'
DECL|variable|_fake_iptables_save_output
name|'_fake_iptables_save_output'
op|'='
op|'('
string|'"# Generated by iptables-save v1.4.10 on "'
nl|'\n'
string|'"Sun Nov  6 22:49:02 2011\\n"'
nl|'\n'
string|'"*filter\\n"'
nl|'\n'
string|'":INPUT ACCEPT [0:0]\\n"'
nl|'\n'
string|'":FORWARD ACCEPT [0:0]\\n"'
nl|'\n'
string|'":OUTPUT ACCEPT [0:0]\\n"'
nl|'\n'
string|'"COMMIT\\n"'
nl|'\n'
string|'"# Completed on Sun Nov  6 22:49:02 2011\\n"'
op|')'
newline|'\n'
nl|'\n'
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
indent|'        '
name|'if'
op|'('
name|'plugin'
op|','
name|'method'
op|')'
op|'=='
op|'('
string|"'glance'"
op|','
string|"'download_vhd'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fake'
op|'.'
name|'as_json'
op|'('
name|'dict'
op|'('
name|'vdi_type'
op|'='
string|"'root'"
op|','
nl|'\n'
name|'vdi_uuid'
op|'='
name|'_make_fake_vdi'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'elif'
op|'('
name|'plugin'
op|','
name|'method'
op|')'
op|'=='
op|'('
string|'"xenhost"'
op|','
string|'"iptables_config"'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fake'
op|'.'
name|'as_json'
op|'('
name|'out'
op|'='
name|'self'
op|'.'
name|'_fake_iptables_save_output'
op|','
nl|'\n'
name|'err'
op|'='
string|"''"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'super'
op|'('
name|'FakeSessionForVMTests'
op|','
name|'self'
op|')'
op|'.'
nl|'\n'
name|'host_call_plugin'
op|'('
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|host_call_plugin_swap
dedent|''
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
name|'if'
op|'('
name|'plugin'
op|','
name|'method'
op|')'
op|'=='
op|'('
string|"'glance'"
op|','
string|"'download_vhd'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'fake'
op|'.'
name|'as_json'
op|'('
name|'dict'
op|'('
name|'vdi_type'
op|'='
string|"'root'"
op|','
nl|'\n'
name|'vdi_uuid'
op|'='
name|'_make_fake_vdi'
op|'('
op|')'
op|')'
op|','
nl|'\n'
name|'dict'
op|'('
name|'vdi_type'
op|'='
string|"'swap'"
op|','
nl|'\n'
name|'vdi_uuid'
op|'='
name|'_make_fake_vdi'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
op|'('
name|'super'
op|'('
name|'FakeSessionForVMTests'
op|','
name|'self'
op|')'
op|'.'
nl|'\n'
name|'host_call_plugin'
op|'('
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
op|')'
newline|'\n'
nl|'\n'
DECL|member|VM_start
dedent|''
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
name|'return'
name|'vm'
newline|'\n'
nl|'\n'
DECL|member|VM_start_on
dedent|''
name|'def'
name|'VM_start_on'
op|'('
name|'self'
op|','
name|'_1'
op|','
name|'vm_ref'
op|','
name|'host_ref'
op|','
name|'_2'
op|','
name|'_3'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vm_rec'
op|'='
name|'self'
op|'.'
name|'VM_start'
op|'('
name|'_1'
op|','
name|'vm_ref'
op|','
name|'_2'
op|','
name|'_3'
op|')'
newline|'\n'
name|'vm_rec'
op|'['
string|"'resident_on'"
op|']'
op|'='
name|'host_ref'
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
name|'sr_ref'
op|','
name|'read_only'
op|'='
name|'True'
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
nl|'\n'
DECL|class|FakeSessionForFirewallTests
dedent|''
dedent|''
name|'class'
name|'FakeSessionForFirewallTests'
op|'('
name|'FakeSessionForVMTests'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Stubs out a XenApi Session for doing IPTable Firewall tests """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'uri'
op|','
name|'test_case'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'FakeSessionForFirewallTests'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'uri'
op|')'
newline|'\n'
name|'if'
name|'hasattr'
op|'('
name|'test_case'
op|','
string|"'_in_filter_rules'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_in_filter_rules'
op|'='
name|'test_case'
op|'.'
name|'_in_filter_rules'
newline|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'test_case'
op|','
string|"'_in6_filter_rules'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_in6_filter_rules'
op|'='
name|'test_case'
op|'.'
name|'_in6_filter_rules'
newline|'\n'
dedent|''
name|'if'
name|'hasattr'
op|'('
name|'test_case'
op|','
string|"'_in_nat_rules'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_in_nat_rules'
op|'='
name|'test_case'
op|'.'
name|'_in_nat_rules'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_test_case'
op|'='
name|'test_case'
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
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Mock method four host_call_plugin to be used in unit tests\n           for the dom0 iptables Firewall drivers for XenAPI\n\n        """'
newline|'\n'
name|'if'
name|'plugin'
op|'=='
string|'"xenhost"'
name|'and'
name|'method'
op|'=='
string|'"iptables_config"'
op|':'
newline|'\n'
comment|'# The command to execute is a json-encoded list'
nl|'\n'
indent|'            '
name|'cmd_args'
op|'='
name|'args'
op|'.'
name|'get'
op|'('
string|"'cmd_args'"
op|','
name|'None'
op|')'
newline|'\n'
name|'cmd'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'cmd_args'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'cmd'
op|':'
newline|'\n'
indent|'                '
name|'ret_str'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'output'
op|'='
string|"''"
newline|'\n'
name|'process_input'
op|'='
name|'args'
op|'.'
name|'get'
op|'('
string|"'process_input'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'cmd'
op|'=='
op|'['
string|"'ip6tables-save'"
op|','
string|"'-t'"
op|','
string|"'filter'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'output'
op|'='
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_in6_filter_rules'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'cmd'
op|'=='
op|'['
string|"'iptables-save'"
op|','
string|"'-t'"
op|','
string|"'filter'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'output'
op|'='
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_in_filter_rules'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'cmd'
op|'=='
op|'['
string|"'iptables-save'"
op|','
string|"'-t'"
op|','
string|"'nat'"
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'output'
op|'='
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'self'
op|'.'
name|'_in_nat_rules'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'cmd'
op|'=='
op|'['
string|"'iptables-restore'"
op|','
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'lines'
op|'='
name|'process_input'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
name|'if'
string|"'*filter'"
name|'in'
name|'lines'
op|':'
newline|'\n'
indent|'                        '
name|'if'
name|'self'
op|'.'
name|'_test_case'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                            '
name|'self'
op|'.'
name|'_test_case'
op|'.'
name|'_out_rules'
op|'='
name|'lines'
newline|'\n'
dedent|''
name|'output'
op|'='
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'lines'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'cmd'
op|'=='
op|'['
string|"'ip6tables-restore'"
op|','
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'lines'
op|'='
name|'process_input'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
name|'if'
string|"'*filter'"
name|'in'
name|'lines'
op|':'
newline|'\n'
indent|'                        '
name|'output'
op|'='
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'lines'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'ret_str'
op|'='
name|'fake'
op|'.'
name|'as_json'
op|'('
name|'out'
op|'='
name|'output'
op|','
name|'err'
op|'='
string|"''"
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'ret_str'
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
DECL|function|fake_acquire_bootlock
indent|'    '
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
DECL|function|fake_generate_ephemeral
dedent|''
name|'def'
name|'fake_generate_ephemeral'
op|'('
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|function|fake_wait_for_device
dedent|''
name|'def'
name|'fake_wait_for_device'
op|'('
name|'dev'
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
name|'vm_utils'
op|','
string|"'generate_ephemeral'"
op|','
name|'fake_generate_ephemeral'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
op|','
string|"'_wait_for_device'"
op|','
name|'fake_wait_for_device'
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
DECL|function|fake_move_disks
dedent|''
name|'def'
name|'fake_move_disks'
op|'('
name|'self'
op|','
name|'instance'
op|','
name|'disk_info'
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
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
string|"'fake'"
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
name|'vdi_rec'
op|'['
string|"'other_config'"
op|']'
op|'['
string|"'nova_disk_type'"
op|']'
op|'='
string|"'root'"
newline|'\n'
name|'return'
op|'{'
string|"'uuid'"
op|':'
name|'vdi_rec'
op|'['
string|"'uuid'"
op|']'
op|','
string|"'ref'"
op|':'
name|'vdi_ref'
op|'}'
newline|'\n'
nl|'\n'
DECL|function|fake_get_vdi
dedent|''
name|'def'
name|'fake_get_vdi'
op|'('
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
string|"'derp'"
op|','
string|"'herp'"
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
DECL|function|fake_sr
dedent|''
name|'def'
name|'fake_sr'
op|'('
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
DECL|function|fake_get_sr_path
dedent|''
name|'def'
name|'fake_get_sr_path'
op|'('
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
DECL|function|fake_generate_ephemeral
dedent|''
name|'def'
name|'fake_generate_ephemeral'
op|'('
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
name|'vmops'
op|'.'
name|'VMOps'
op|','
string|"'_move_disks'"
op|','
name|'fake_move_disks'
op|')'
newline|'\n'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'vm_utils'
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
name|'vm_utils'
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
name|'vm_utils'
op|','
string|"'generate_ephemeral'"
op|','
name|'fake_generate_ephemeral'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
