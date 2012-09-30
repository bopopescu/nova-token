begin_unit
comment|'#!/usr/bin/env python'
nl|'\n'
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2011 Nexenta Systems, Inc.'
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
string|'"""\nUnit tests for OpenStack Nova volume driver\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
name|'import'
name|'urllib2'
newline|'\n'
nl|'\n'
name|'import'
name|'nova'
op|'.'
name|'flags'
newline|'\n'
name|'import'
name|'nova'
op|'.'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'nexenta'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'nexenta'
name|'import'
name|'jsonrpc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'nexenta'
name|'import'
name|'volume'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'nova'
op|'.'
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestNexentaDriver
name|'class'
name|'TestNexentaDriver'
op|'('
name|'nova'
op|'.'
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|TEST_VOLUME_NAME
indent|'    '
name|'TEST_VOLUME_NAME'
op|'='
string|"'volume1'"
newline|'\n'
DECL|variable|TEST_VOLUME_NAME2
name|'TEST_VOLUME_NAME2'
op|'='
string|"'volume2'"
newline|'\n'
DECL|variable|TEST_SNAPSHOT_NAME
name|'TEST_SNAPSHOT_NAME'
op|'='
string|"'snapshot1'"
newline|'\n'
DECL|variable|TEST_VOLUME_REF
name|'TEST_VOLUME_REF'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'TEST_VOLUME_NAME'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|TEST_VOLUME_REF2
name|'TEST_VOLUME_REF2'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'TEST_VOLUME_NAME2'
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|TEST_SNAPSHOT_REF
name|'TEST_SNAPSHOT_REF'
op|'='
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'TEST_SNAPSHOT_NAME'
op|','
nl|'\n'
string|"'volume_name'"
op|':'
name|'TEST_VOLUME_NAME'
op|','
nl|'\n'
op|'}'
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
name|'super'
op|'('
name|'TestNexentaDriver'
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
name|'flags'
op|'('
nl|'\n'
name|'nexenta_host'
op|'='
string|"'1.1.1.1'"
op|','
nl|'\n'
name|'nexenta_volume'
op|'='
string|"'nova'"
op|','
nl|'\n'
name|'nexenta_target_prefix'
op|'='
string|"'iqn:'"
op|','
nl|'\n'
name|'nexenta_target_group_prefix'
op|'='
string|"'nova/'"
op|','
nl|'\n'
name|'nexenta_blocksize'
op|'='
string|"'8K'"
op|','
nl|'\n'
name|'nexenta_sparse'
op|'='
name|'True'
op|','
nl|'\n'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nms_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'for'
name|'mod'
name|'in'
op|'['
string|"'volume'"
op|','
string|"'zvol'"
op|','
string|"'iscsitarget'"
op|','
nl|'\n'
string|"'stmf'"
op|','
string|"'scsidisk'"
op|','
string|"'snapshot'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'setattr'
op|'('
name|'self'
op|'.'
name|'nms_mock'
op|','
name|'mod'
op|','
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'stubs'
op|'.'
name|'Set'
op|'('
name|'jsonrpc'
op|','
string|"'NexentaJSONProxy'"
op|','
nl|'\n'
name|'lambda'
op|'*'
name|'_'
op|','
op|'**'
name|'__'
op|':'
name|'self'
op|'.'
name|'nms_mock'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'drv'
op|'='
name|'volume'
op|'.'
name|'NexentaDriver'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'drv'
op|'.'
name|'do_setup'
op|'('
op|'{'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setup_error
dedent|''
name|'def'
name|'test_setup_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'volume'
op|'.'
name|'object_exists'
op|'('
string|"'nova'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'True'
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'check_for_setup_error'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_setup_error_fail
dedent|''
name|'def'
name|'test_setup_error_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'volume'
op|'.'
name|'object_exists'
op|'('
string|"'nova'"
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'False'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'LookupError'
op|','
name|'self'
op|'.'
name|'drv'
op|'.'
name|'check_for_setup_error'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_local_path
dedent|''
name|'def'
name|'test_local_path'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'NotImplementedError'
op|','
name|'self'
op|'.'
name|'drv'
op|'.'
name|'local_path'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_volume
dedent|''
name|'def'
name|'test_create_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'zvol'
op|'.'
name|'create'
op|'('
string|"'nova/volume1'"
op|','
string|"'1G'"
op|','
string|"'8K'"
op|','
name|'True'
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'create_volume'
op|'('
name|'self'
op|'.'
name|'TEST_VOLUME_REF'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_volume
dedent|''
name|'def'
name|'test_delete_volume'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'zvol'
op|'.'
name|'destroy'
op|'('
string|"'nova/volume1'"
op|','
string|"''"
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'delete_volume'
op|'('
name|'self'
op|'.'
name|'TEST_VOLUME_REF'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_snapshot
dedent|''
name|'def'
name|'test_create_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'zvol'
op|'.'
name|'create_snapshot'
op|'('
string|"'nova/volume1'"
op|','
string|"'snapshot1'"
op|','
string|"''"
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'create_snapshot'
op|'('
name|'self'
op|'.'
name|'TEST_SNAPSHOT_REF'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_volume_from_snapshot
dedent|''
name|'def'
name|'test_create_volume_from_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'zvol'
op|'.'
name|'clone'
op|'('
string|"'nova/volume1@snapshot1'"
op|','
string|"'nova/volume2'"
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'create_volume_from_snapshot'
op|'('
name|'self'
op|'.'
name|'TEST_VOLUME_REF2'
op|','
nl|'\n'
name|'self'
op|'.'
name|'TEST_SNAPSHOT_REF'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_delete_snapshot
dedent|''
name|'def'
name|'test_delete_snapshot'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'snapshot'
op|'.'
name|'destroy'
op|'('
string|"'nova/volume1@snapshot1'"
op|','
string|"''"
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'delete_snapshot'
op|'('
name|'self'
op|'.'
name|'TEST_SNAPSHOT_REF'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_CREATE_EXPORT_METHODS
dedent|''
name|'_CREATE_EXPORT_METHODS'
op|'='
op|'['
nl|'\n'
op|'('
string|"'iscsitarget'"
op|','
string|"'create_target'"
op|','
op|'('
op|'{'
string|"'target_name'"
op|':'
string|"'iqn:volume1'"
op|'}'
op|','
op|')'
op|','
nl|'\n'
string|"u'Unable to create iscsi target\\n'"
nl|'\n'
string|"u' iSCSI target iqn.1986-03.com.sun:02:nova-volume1 already'"
nl|'\n'
string|"u' configured\\n'"
nl|'\n'
string|"u' itadm create-target failed with error 17\\n'"
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|'('
string|"'stmf'"
op|','
string|"'create_targetgroup'"
op|','
op|'('
string|"'nova/volume1'"
op|','
op|')'
op|','
nl|'\n'
string|"u'Unable to create targetgroup: stmfadm: nova/volume1:'"
nl|'\n'
string|"u' already exists\\n'"
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|'('
string|"'stmf'"
op|','
string|"'add_targetgroup_member'"
op|','
op|'('
string|"'nova/volume1'"
op|','
string|"'iqn:volume1'"
op|')'
op|','
nl|'\n'
string|"u'Unable to add member to targetgroup: stmfadm:'"
nl|'\n'
string|"u' iqn.1986-03.com.sun:02:nova-volume1: already exists\\n'"
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|'('
string|"'scsidisk'"
op|','
string|"'create_lu'"
op|','
op|'('
string|"'nova/volume1'"
op|','
op|'{'
op|'}'
op|')'
op|','
nl|'\n'
string|'u"Unable to create lu with zvol \'nova/volume1\':\\n"'
nl|'\n'
string|'u" sbdadm: filename /dev/zvol/rdsk/nova/volume1: in use\\n"'
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|'('
string|"'scsidisk'"
op|','
string|"'add_lun_mapping_entry'"
op|','
op|'('
string|"'nova/volume1'"
op|','
op|'{'
nl|'\n'
string|"'target_group'"
op|':'
string|"'nova/volume1'"
op|','
string|"'lun'"
op|':'
string|"'0'"
op|'}'
op|')'
op|','
nl|'\n'
string|'u"Unable to add view to zvol \'nova/volume1\' (LUNs in use: ):\\n"'
nl|'\n'
string|'u" stmfadm: view entry exists\\n"'
op|','
nl|'\n'
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|member|_stub_export_method
name|'def'
name|'_stub_export_method'
op|'('
name|'self'
op|','
name|'module'
op|','
name|'method'
op|','
name|'args'
op|','
name|'error'
op|','
name|'fail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'='
name|'getattr'
op|'('
name|'self'
op|'.'
name|'nms_mock'
op|','
name|'module'
op|')'
newline|'\n'
name|'m'
op|'='
name|'getattr'
op|'('
name|'m'
op|','
name|'method'
op|')'
newline|'\n'
name|'mock'
op|'='
name|'m'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
name|'if'
name|'fail'
op|':'
newline|'\n'
indent|'            '
name|'mock'
op|'.'
name|'AndRaise'
op|'('
name|'nexenta'
op|'.'
name|'NexentaException'
op|'('
name|'error'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_stub_all_export_methods
dedent|''
dedent|''
name|'def'
name|'_stub_all_export_methods'
op|'('
name|'self'
op|','
name|'fail'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'for'
name|'params'
name|'in'
name|'self'
op|'.'
name|'_CREATE_EXPORT_METHODS'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_stub_export_method'
op|'('
op|'*'
name|'params'
op|','
name|'fail'
op|'='
name|'fail'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_export
dedent|''
dedent|''
name|'def'
name|'test_create_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_stub_all_export_methods'
op|'('
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
name|'retval'
op|'='
name|'self'
op|'.'
name|'drv'
op|'.'
name|'create_export'
op|'('
op|'{'
op|'}'
op|','
name|'self'
op|'.'
name|'TEST_VOLUME_REF'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
name|'retval'
op|','
nl|'\n'
op|'{'
string|"'provider_location'"
op|':'
nl|'\n'
string|"'%s:%s,1 %s%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'nexenta_host'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'nexenta_iscsi_target_portal_port'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'nexenta_target_prefix'
op|','
nl|'\n'
name|'self'
op|'.'
name|'TEST_VOLUME_NAME'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__get_test
dedent|''
name|'def'
name|'__get_test'
op|'('
name|'i'
op|')'
op|':'
newline|'\n'
DECL|function|_test_create_export_fail
indent|'        '
name|'def'
name|'_test_create_export_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'params'
name|'in'
name|'self'
op|'.'
name|'_CREATE_EXPORT_METHODS'
op|'['
op|':'
name|'i'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_stub_export_method'
op|'('
op|'*'
name|'params'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'_stub_export_method'
op|'('
op|'*'
name|'self'
op|'.'
name|'_CREATE_EXPORT_METHODS'
op|'['
name|'i'
op|']'
op|','
nl|'\n'
name|'fail'
op|'='
name|'True'
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'nexenta'
op|'.'
name|'NexentaException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'drv'
op|'.'
name|'create_export'
op|','
op|'{'
op|'}'
op|','
name|'self'
op|'.'
name|'TEST_VOLUME_REF'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_test_create_export_fail'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'len'
op|'('
name|'_CREATE_EXPORT_METHODS'
op|')'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'locals'
op|'('
op|')'
op|'['
string|"'test_create_export_fail_%d'"
op|'%'
name|'i'
op|']'
op|'='
name|'__get_test'
op|'('
name|'i'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_ensure_export
dedent|''
name|'def'
name|'test_ensure_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'_stub_all_export_methods'
op|'('
name|'fail'
op|'='
name|'True'
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'ensure_export'
op|'('
op|'{'
op|'}'
op|','
name|'self'
op|'.'
name|'TEST_VOLUME_REF'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_export
dedent|''
name|'def'
name|'test_remove_export'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'scsidisk'
op|'.'
name|'delete_lu'
op|'('
string|"'nova/volume1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'stmf'
op|'.'
name|'destroy_targetgroup'
op|'('
string|"'nova/volume1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'iscsitarget'
op|'.'
name|'delete_target'
op|'('
string|"'iqn:volume1'"
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'remove_export'
op|'('
op|'{'
op|'}'
op|','
name|'self'
op|'.'
name|'TEST_VOLUME_REF'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_export_fail_0
dedent|''
name|'def'
name|'test_remove_export_fail_0'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'scsidisk'
op|'.'
name|'delete_lu'
op|'('
string|"'nova/volume1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'stmf'
op|'.'
name|'destroy_targetgroup'
op|'('
string|"'nova/volume1'"
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'nexenta'
op|'.'
name|'NexentaException'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'iscsitarget'
op|'.'
name|'delete_target'
op|'('
string|"'iqn:volume1'"
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'remove_export'
op|'('
op|'{'
op|'}'
op|','
name|'self'
op|'.'
name|'TEST_VOLUME_REF'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_remove_export_fail_1
dedent|''
name|'def'
name|'test_remove_export_fail_1'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'scsidisk'
op|'.'
name|'delete_lu'
op|'('
string|"'nova/volume1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'stmf'
op|'.'
name|'destroy_targetgroup'
op|'('
string|"'nova/volume1'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nms_mock'
op|'.'
name|'iscsitarget'
op|'.'
name|'delete_target'
op|'('
string|"'iqn:volume1'"
op|')'
op|'.'
name|'AndRaise'
op|'('
nl|'\n'
name|'nexenta'
op|'.'
name|'NexentaException'
op|'('
op|')'
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
name|'self'
op|'.'
name|'drv'
op|'.'
name|'remove_export'
op|'('
op|'{'
op|'}'
op|','
name|'self'
op|'.'
name|'TEST_VOLUME_REF'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestNexentaJSONRPC
dedent|''
dedent|''
name|'class'
name|'TestNexentaJSONRPC'
op|'('
name|'nova'
op|'.'
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|variable|URL
indent|'    '
name|'URL'
op|'='
string|"'http://example.com/'"
newline|'\n'
DECL|variable|URL_S
name|'URL_S'
op|'='
string|"'https://example.com/'"
newline|'\n'
DECL|variable|USER
name|'USER'
op|'='
string|"'user'"
newline|'\n'
DECL|variable|PASSWORD
name|'PASSWORD'
op|'='
string|"'password'"
newline|'\n'
DECL|variable|HEADERS
name|'HEADERS'
op|'='
op|'{'
string|"'Authorization'"
op|':'
string|"'Basic %s'"
op|'%'
op|'('
name|'base64'
op|'.'
name|'b64encode'
op|'('
nl|'\n'
string|"':'"
op|'.'
name|'join'
op|'('
op|'('
name|'USER'
op|','
name|'PASSWORD'
op|')'
op|')'
op|')'
op|','
op|')'
op|','
nl|'\n'
string|"'Content-Type'"
op|':'
string|"'application/json'"
op|'}'
newline|'\n'
DECL|variable|REQUEST
name|'REQUEST'
op|'='
string|"'the request'"
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
name|'super'
op|'('
name|'TestNexentaJSONRPC'
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
name|'proxy'
op|'='
name|'jsonrpc'
op|'.'
name|'NexentaJSONProxy'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'URL'
op|','
name|'self'
op|'.'
name|'USER'
op|','
name|'self'
op|'.'
name|'PASSWORD'
op|','
name|'auto'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'urllib2'
op|','
string|"'Request'"
op|','
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'urllib2'
op|','
string|"'urlopen'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_info_mock'
op|'='
name|'self'
op|'.'
name|'mox'
op|'.'
name|'CreateMockAnything'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_mock'
op|'.'
name|'info'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'resp_info_mock'
op|')'
newline|'\n'
name|'urllib2'
op|'.'
name|'urlopen'
op|'('
name|'self'
op|'.'
name|'REQUEST'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'resp_mock'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call
dedent|''
name|'def'
name|'test_call'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'self'
op|'.'
name|'URL'
op|','
nl|'\n'
string|'\'{"object": null, "params": ["arg1", "arg2"], "method": null}\''
op|','
nl|'\n'
name|'self'
op|'.'
name|'HEADERS'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'REQUEST'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_info_mock'
op|'.'
name|'status'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'resp_mock'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|'\'{"error": null, "result": "the result"}\''
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
name|'result'
op|'='
name|'self'
op|'.'
name|'proxy'
op|'('
string|"'arg1'"
op|','
string|"'arg2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"the result"'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_deep
dedent|''
name|'def'
name|'test_call_deep'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'self'
op|'.'
name|'URL'
op|','
nl|'\n'
string|'\'{"object": "obj1.subobj", "params": ["arg1", "arg2"],\''
nl|'\n'
string|'\' "method": "meth"}\''
op|','
nl|'\n'
name|'self'
op|'.'
name|'HEADERS'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'REQUEST'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_info_mock'
op|'.'
name|'status'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'resp_mock'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|'\'{"error": null, "result": "the result"}\''
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
name|'result'
op|'='
name|'self'
op|'.'
name|'proxy'
op|'.'
name|'obj1'
op|'.'
name|'subobj'
op|'.'
name|'meth'
op|'('
string|"'arg1'"
op|','
string|"'arg2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"the result"'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_auto
dedent|''
name|'def'
name|'test_call_auto'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'self'
op|'.'
name|'URL'
op|','
nl|'\n'
string|'\'{"object": null, "params": ["arg1", "arg2"], "method": null}\''
op|','
nl|'\n'
name|'self'
op|'.'
name|'HEADERS'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'REQUEST'
op|')'
newline|'\n'
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'self'
op|'.'
name|'URL_S'
op|','
nl|'\n'
string|'\'{"object": null, "params": ["arg1", "arg2"], "method": null}\''
op|','
nl|'\n'
name|'self'
op|'.'
name|'HEADERS'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'REQUEST'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_info_mock'
op|'.'
name|'status'
op|'='
string|"'EOF in headers'"
newline|'\n'
name|'self'
op|'.'
name|'resp_mock'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|'\'{"error": null, "result": "the result"}\''
op|')'
newline|'\n'
name|'urllib2'
op|'.'
name|'urlopen'
op|'('
name|'self'
op|'.'
name|'REQUEST'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'resp_mock'
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
name|'result'
op|'='
name|'self'
op|'.'
name|'proxy'
op|'('
string|"'arg1'"
op|','
string|"'arg2'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEquals'
op|'('
string|'"the result"'
op|','
name|'result'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_error
dedent|''
name|'def'
name|'test_call_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'self'
op|'.'
name|'URL'
op|','
nl|'\n'
string|'\'{"object": null, "params": ["arg1", "arg2"], "method": null}\''
op|','
nl|'\n'
name|'self'
op|'.'
name|'HEADERS'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'REQUEST'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_info_mock'
op|'.'
name|'status'
op|'='
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'resp_mock'
op|'.'
name|'read'
op|'('
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
string|'\'{"error": {"message": "the error"}, "result": "the result"}\''
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
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'jsonrpc'
op|'.'
name|'NexentaJSONException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'proxy'
op|','
string|"'arg1'"
op|','
string|"'arg2'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_call_fail
dedent|''
name|'def'
name|'test_call_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'urllib2'
op|'.'
name|'Request'
op|'('
name|'self'
op|'.'
name|'URL'
op|','
nl|'\n'
string|'\'{"object": null, "params": ["arg1", "arg2"], "method": null}\''
op|','
nl|'\n'
name|'self'
op|'.'
name|'HEADERS'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'self'
op|'.'
name|'REQUEST'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'resp_info_mock'
op|'.'
name|'status'
op|'='
string|"'EOF in headers'"
newline|'\n'
name|'self'
op|'.'
name|'proxy'
op|'.'
name|'auto'
op|'='
name|'False'
newline|'\n'
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
name|'assertRaises'
op|'('
name|'jsonrpc'
op|'.'
name|'NexentaJSONException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'proxy'
op|','
string|"'arg1'"
op|','
string|"'arg2'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
