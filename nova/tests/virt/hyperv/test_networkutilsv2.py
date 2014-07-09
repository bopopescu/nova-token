begin_unit
comment|'#  Copyright 2013 Cloudbase Solutions Srl'
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
name|'nova'
name|'import'
name|'test'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'networkutilsv2'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'hyperv'
name|'import'
name|'vmutils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkUtilsV2TestCase
name|'class'
name|'NetworkUtilsV2TestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unit tests for the Hyper-V NetworkUtilsV2 class."""'
newline|'\n'
nl|'\n'
DECL|variable|_FAKE_VSWITCH_NAME
name|'_FAKE_VSWITCH_NAME'
op|'='
string|'"fake_vswitch_name"'
newline|'\n'
DECL|variable|_FAKE_VSWITCH_PATH
name|'_FAKE_VSWITCH_PATH'
op|'='
string|'"fake_vswitch_path"'
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
name|'self'
op|'.'
name|'_networkutils'
op|'='
name|'networkutilsv2'
op|'.'
name|'NetworkUtilsV2'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_networkutils'
op|'.'
name|'_conn'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'NetworkUtilsV2TestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_external_vswitch
dedent|''
name|'def'
name|'test_get_external_vswitch'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_vswitch'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_vswitch'
op|'.'
name|'path_'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_FAKE_VSWITCH_PATH'
newline|'\n'
name|'self'
op|'.'
name|'_networkutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualEthernetSwitch'
op|'.'
name|'return_value'
op|'='
op|'['
nl|'\n'
name|'mock_vswitch'
op|']'
newline|'\n'
nl|'\n'
name|'switch_path'
op|'='
name|'self'
op|'.'
name|'_networkutils'
op|'.'
name|'get_external_vswitch'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_VSWITCH_NAME'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_FAKE_VSWITCH_PATH'
op|','
name|'switch_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_external_vswitch_not_found
dedent|''
name|'def'
name|'test_get_external_vswitch_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_vswitch'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_vswitch'
op|'.'
name|'path_'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_FAKE_VSWITCH_PATH'
newline|'\n'
name|'self'
op|'.'
name|'_networkutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_VirtualEthernetSwitch'
op|'.'
name|'return_value'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'vmutils'
op|'.'
name|'HyperVException'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_networkutils'
op|'.'
name|'get_external_vswitch'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_FAKE_VSWITCH_NAME'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_get_external_vswitch_no_name
dedent|''
name|'def'
name|'test_get_external_vswitch_no_name'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mock_vswitch'
op|'='
name|'mock'
op|'.'
name|'MagicMock'
op|'('
op|')'
newline|'\n'
name|'mock_vswitch'
op|'.'
name|'path_'
op|'.'
name|'return_value'
op|'='
name|'self'
op|'.'
name|'_FAKE_VSWITCH_PATH'
newline|'\n'
nl|'\n'
name|'mock_ext_port'
op|'='
name|'self'
op|'.'
name|'_networkutils'
op|'.'
name|'_conn'
op|'.'
name|'Msvm_ExternalEthernetPort'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'mock_lep'
op|'='
name|'mock_ext_port'
op|'.'
name|'associators'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'mock_lep1'
op|'='
name|'mock_lep'
op|'.'
name|'associators'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'mock_esw'
op|'='
name|'mock_lep1'
op|'.'
name|'associators'
op|'('
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
name|'mock_esw'
op|'.'
name|'associators'
op|'.'
name|'return_value'
op|'='
op|'['
name|'mock_vswitch'
op|']'
newline|'\n'
nl|'\n'
name|'switch_path'
op|'='
name|'self'
op|'.'
name|'_networkutils'
op|'.'
name|'get_external_vswitch'
op|'('
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_FAKE_VSWITCH_PATH'
op|','
name|'switch_path'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
