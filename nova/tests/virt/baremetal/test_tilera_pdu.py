begin_unit
comment|'# coding=utf-8'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011-2013 University of Southern California / ISI'
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
string|'"""Test class for baremetal PDU power manager."""'
newline|'\n'
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
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'utils'
name|'as'
name|'bm_db_utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'baremetal_states'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'tilera_pdu'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'utils'
name|'as'
name|'bm_utils'
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
DECL|class|BareMetalPduTestCase
name|'class'
name|'BareMetalPduTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
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
name|'BareMetalPduTestCase'
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
name|'tile_power_wait'
op|'='
number|'0'
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'node'
op|'='
name|'bm_db_utils'
op|'.'
name|'new_bm_node'
op|'('
nl|'\n'
name|'id'
op|'='
number|'123'
op|','
nl|'\n'
name|'pm_address'
op|'='
string|"'fake-address'"
op|','
nl|'\n'
name|'pm_user'
op|'='
string|"'fake-user'"
op|','
nl|'\n'
name|'pm_password'
op|'='
string|"'fake-password'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'='
name|'tilera_pdu'
op|'.'
name|'Pdu'
op|'('
name|'self'
op|'.'
name|'node'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tile_pdu_on'
op|'='
number|'1'
newline|'\n'
name|'self'
op|'.'
name|'tile_pdu_off'
op|'='
number|'2'
newline|'\n'
name|'self'
op|'.'
name|'tile_pdu_status'
op|'='
number|'9'
newline|'\n'
nl|'\n'
DECL|member|test_construct
dedent|''
name|'def'
name|'test_construct'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'node_id'
op|','
number|'123'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'address'
op|','
string|"'fake-address'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'user'
op|','
string|"'fake-user'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'password'
op|','
string|"'fake-password'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_exec_pdutool
dedent|''
name|'def'
name|'test_exec_pdutool'
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
name|'tile_pdu_mgr'
op|'='
string|"'fake-pdu-mgr'"
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'flags'
op|'('
name|'tile_pdu_ip'
op|'='
string|"'fake-address'"
op|','
name|'group'
op|'='
string|"'baremetal'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'utils'
op|','
string|"'execute'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'bm_utils'
op|','
string|"'unlink_without_raise'"
op|')'
newline|'\n'
name|'args'
op|'='
op|'['
nl|'\n'
string|"'fake-pdu-mgr'"
op|','
nl|'\n'
string|"'fake-address'"
op|','
nl|'\n'
name|'self'
op|'.'
name|'tile_pdu_on'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|')'
op|'.'
name|'AndReturn'
op|'('
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
nl|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_on'
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
DECL|member|test_is_power
dedent|''
name|'def'
name|'test_is_power'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|','
string|"'_exec_pdutool'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_status'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'tile_pdu_on'
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
name|'tilera_pdu'
op|'.'
name|'_is_power'
op|'('
name|'self'
op|'.'
name|'tile_pdu_on'
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
DECL|member|test_power_already_on
dedent|''
name|'def'
name|'test_power_already_on'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|','
string|"'_exec_pdutool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_on'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_status'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'tile_pdu_on'
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
name|'tilera_pdu'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_power_on'
op|'('
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_on_ok
dedent|''
name|'def'
name|'test_power_on_ok'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|','
string|"'_exec_pdutool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_on'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_status'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'tile_pdu_on'
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
name|'tilera_pdu'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_power_on'
op|'('
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'ACTIVE'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_on_fail
dedent|''
name|'def'
name|'test_power_on_fail'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|','
string|"'_exec_pdutool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_on'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_status'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'tile_pdu_off'
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
name|'tilera_pdu'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_power_on'
op|'('
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'ERROR'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_on_max_retries
dedent|''
name|'def'
name|'test_power_on_max_retries'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|','
string|"'_exec_pdutool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_on'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_status'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'tile_pdu_off'
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
name|'tilera_pdu'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'DELETED'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_power_on'
op|'('
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'ERROR'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_power_off_ok
dedent|''
name|'def'
name|'test_power_off_ok'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'mox'
op|'.'
name|'StubOutWithMock'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|','
string|"'_exec_pdutool'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_off'
op|')'
op|'.'
name|'AndReturn'
op|'('
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_exec_pdutool'
op|'('
name|'self'
op|'.'
name|'tile_pdu_status'
op|')'
op|'.'
name|'AndReturn'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'tile_pdu_off'
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
name|'tilera_pdu'
op|'.'
name|'state'
op|'='
name|'baremetal_states'
op|'.'
name|'ACTIVE'
newline|'\n'
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'_power_off'
op|'('
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
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'tilera_pdu'
op|'.'
name|'state'
op|','
name|'baremetal_states'
op|'.'
name|'DELETED'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
