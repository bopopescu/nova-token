begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
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
name|'mock'
newline|'\n'
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'greenthread'
newline|'\n'
nl|'\n'
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
name|'import'
name|'utils'
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
nl|'\n'
nl|'\n'
DECL|class|CallXenAPIHelpersTestCase
name|'class'
name|'CallXenAPIHelpersTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
op|')'
op|':'
newline|'\n'
DECL|member|test_vbd_plug
indent|'    '
name|'def'
name|'test_vbd_plug'
op|'('
name|'self'
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
name|'volume_utils'
op|'.'
name|'vbd_plug'
op|'('
name|'session'
op|','
string|'"vbd_ref"'
op|','
string|'"vm_ref:123"'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"VBD.plug"'
op|','
string|'"vbd_ref"'
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
name|'utils'
op|','
string|"'synchronized'"
op|')'
newline|'\n'
DECL|member|test_vbd_plug_check_synchronized
name|'def'
name|'test_vbd_plug_check_synchronized'
op|'('
name|'self'
op|','
name|'mock_synchronized'
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
name|'volume_utils'
op|'.'
name|'vbd_plug'
op|'('
name|'session'
op|','
string|'"vbd_ref"'
op|','
string|'"vm_ref:123"'
op|')'
newline|'\n'
name|'mock_synchronized'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"xenapi-events-vm_ref:123"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vbd_unplug
dedent|''
name|'def'
name|'test_vbd_unplug'
op|'('
name|'self'
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
name|'volume_utils'
op|'.'
name|'vbd_unplug'
op|'('
name|'session'
op|','
string|'"vbd_ref"'
op|','
string|'"vm_ref:123"'
op|')'
newline|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"VBD.unplug"'
op|','
string|'"vbd_ref"'
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
name|'utils'
op|','
string|"'synchronized'"
op|')'
newline|'\n'
DECL|member|test_vbd_unplug_check_synchronized
name|'def'
name|'test_vbd_unplug_check_synchronized'
op|'('
name|'self'
op|','
name|'mock_synchronized'
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
name|'volume_utils'
op|'.'
name|'vbd_unplug'
op|'('
name|'session'
op|','
string|'"vbd_ref"'
op|','
string|'"vm_ref:123"'
op|')'
newline|'\n'
name|'mock_synchronized'
op|'.'
name|'assert_called_once_with'
op|'('
string|'"xenapi-events-vm_ref:123"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ISCSIParametersTestCase
dedent|''
dedent|''
name|'class'
name|'ISCSIParametersTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
op|')'
op|':'
newline|'\n'
DECL|member|test_target_host
indent|'    '
name|'def'
name|'test_target_host'
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
name|'volume_utils'
op|'.'
name|'_get_target_host'
op|'('
string|"'host:port'"
op|')'
op|','
nl|'\n'
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_utils'
op|'.'
name|'_get_target_host'
op|'('
string|"'host'"
op|')'
op|','
nl|'\n'
string|"'host'"
op|')'
newline|'\n'
nl|'\n'
comment|'# There is no default value'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_utils'
op|'.'
name|'_get_target_host'
op|'('
string|"':port'"
op|')'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_utils'
op|'.'
name|'_get_target_host'
op|'('
name|'None'
op|')'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_target_port
dedent|''
name|'def'
name|'test_target_port'
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
name|'volume_utils'
op|'.'
name|'_get_target_port'
op|'('
string|"'host:port'"
op|')'
op|','
nl|'\n'
string|"'port'"
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_utils'
op|'.'
name|'_get_target_port'
op|'('
string|"'host'"
op|')'
op|','
nl|'\n'
string|"'3260'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|IntroduceTestCase
dedent|''
dedent|''
name|'class'
name|'IntroduceTestCase'
op|'('
name|'stubs'
op|'.'
name|'XenAPITestBaseNoDB'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'volume_utils'
op|','
string|"'_get_vdi_ref'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'greenthread'
op|','
string|"'sleep'"
op|')'
newline|'\n'
DECL|member|test_introduce_vdi_retry
name|'def'
name|'test_introduce_vdi_retry'
op|'('
name|'self'
op|','
name|'mock_sleep'
op|','
name|'mock_get_vdi_ref'
op|')'
op|':'
newline|'\n'
DECL|function|fake_get_vdi_ref
indent|'        '
name|'def'
name|'fake_get_vdi_ref'
op|'('
name|'session'
op|','
name|'sr_ref'
op|','
name|'vdi_uuid'
op|','
name|'target_lun'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'fake_get_vdi_ref'
op|'.'
name|'call_count'
op|'+='
number|'1'
newline|'\n'
name|'if'
name|'fake_get_vdi_ref'
op|'.'
name|'call_count'
op|'=='
number|'2'
op|':'
newline|'\n'
indent|'                '
name|'return'
string|"'vdi_ref'"
newline|'\n'
nl|'\n'
DECL|function|fake_call_xenapi
dedent|''
dedent|''
name|'def'
name|'fake_call_xenapi'
op|'('
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'method'
op|'=='
string|"'SR.scan'"
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'elif'
name|'method'
op|'=='
string|"'VDI.get_record'"
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'{'
string|"'managed'"
op|':'
string|"'true'"
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'side_effect'
op|'='
name|'fake_call_xenapi'
newline|'\n'
nl|'\n'
name|'mock_get_vdi_ref'
op|'.'
name|'side_effect'
op|'='
name|'fake_get_vdi_ref'
newline|'\n'
name|'fake_get_vdi_ref'
op|'.'
name|'call_count'
op|'='
number|'0'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'volume_utils'
op|'.'
name|'introduce_vdi'
op|'('
name|'session'
op|','
string|"'sr_ref'"
op|')'
op|','
nl|'\n'
string|"'vdi_ref'"
op|')'
newline|'\n'
name|'mock_sleep'
op|'.'
name|'assert_called_once_with'
op|'('
number|'20'
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
name|'volume_utils'
op|','
string|"'_get_vdi_ref'"
op|')'
newline|'\n'
op|'@'
name|'mock'
op|'.'
name|'patch'
op|'.'
name|'object'
op|'('
name|'greenthread'
op|','
string|"'sleep'"
op|')'
newline|'\n'
DECL|member|test_introduce_vdi_exception
name|'def'
name|'test_introduce_vdi_exception'
op|'('
name|'self'
op|','
name|'mock_sleep'
op|','
name|'mock_get_vdi_ref'
op|')'
op|':'
newline|'\n'
DECL|function|fake_call_xenapi
indent|'        '
name|'def'
name|'fake_call_xenapi'
op|'('
name|'method'
op|','
op|'*'
name|'args'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'method'
op|'=='
string|"'SR.scan'"
op|':'
newline|'\n'
indent|'                '
name|'return'
newline|'\n'
dedent|''
name|'elif'
name|'method'
op|'=='
string|"'VDI.get_record'"
op|':'
newline|'\n'
indent|'                '
name|'return'
op|'{'
string|"'managed'"
op|':'
string|"'true'"
op|'}'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'session'
op|'='
name|'mock'
op|'.'
name|'Mock'
op|'('
op|')'
newline|'\n'
name|'session'
op|'.'
name|'call_xenapi'
op|'.'
name|'side_effect'
op|'='
name|'fake_call_xenapi'
newline|'\n'
name|'mock_get_vdi_ref'
op|'.'
name|'return_value'
op|'='
name|'None'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'volume_utils'
op|'.'
name|'StorageError'
op|','
nl|'\n'
name|'volume_utils'
op|'.'
name|'introduce_vdi'
op|','
name|'session'
op|','
string|"'sr_ref'"
op|')'
newline|'\n'
name|'mock_sleep'
op|'.'
name|'assert_called_once_with'
op|'('
number|'20'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
