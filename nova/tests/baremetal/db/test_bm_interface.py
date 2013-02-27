begin_unit
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
string|'"""\nBare-metal DB testcase for BareMetalInterface\n"""'
newline|'\n'
nl|'\n'
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
op|'.'
name|'db'
name|'import'
name|'exception'
name|'as'
name|'db_exc'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'baremetal'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'baremetal'
name|'import'
name|'db'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|BareMetalInterfaceTestCase
name|'class'
name|'BareMetalInterfaceTestCase'
op|'('
name|'base'
op|'.'
name|'BMDBTestCase'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|test_unique_address
indent|'    '
name|'def'
name|'test_unique_address'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pif1_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|','
string|"'11:11:11:11:11:11'"
op|','
nl|'\n'
string|"'0x1'"
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'db_exc'
op|'.'
name|'DBError'
op|','
nl|'\n'
name|'db'
op|'.'
name|'bm_interface_create'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
number|'2'
op|','
string|"'11:11:11:11:11:11'"
op|','
string|"'0x2'"
op|','
number|'2'
op|')'
newline|'\n'
comment|'# succeed after delete pif1'
nl|'\n'
name|'db'
op|'.'
name|'bm_interface_destroy'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'pif1_id'
op|')'
newline|'\n'
name|'pif2_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'2'
op|','
string|"'11:11:11:11:11:11'"
op|','
nl|'\n'
string|"'0x2'"
op|','
number|'2'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'pif2_id'
name|'is'
name|'not'
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_unique_vif_uuid
dedent|''
name|'def'
name|'test_unique_vif_uuid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pif1_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|','
string|"'11:11:11:11:11:11'"
op|','
nl|'\n'
string|"'0x1'"
op|','
number|'1'
op|')'
newline|'\n'
name|'pif2_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'2'
op|','
string|"'22:22:22:22:22:22'"
op|','
nl|'\n'
string|"'0x2'"
op|','
number|'2'
op|')'
newline|'\n'
name|'db'
op|'.'
name|'bm_interface_set_vif_uuid'
op|'('
name|'self'
op|'.'
name|'context'
op|','
name|'pif1_id'
op|','
string|"'AAAA'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'db'
op|'.'
name|'bm_interface_set_vif_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'pif2_id'
op|','
string|"'AAAA'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_vif_not_found
dedent|''
name|'def'
name|'test_vif_not_found'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pif_id'
op|'='
name|'db'
op|'.'
name|'bm_interface_create'
op|'('
name|'self'
op|'.'
name|'context'
op|','
number|'1'
op|','
string|"'11:11:11:11:11:11'"
op|','
nl|'\n'
string|"'0x1'"
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'NovaException'
op|','
nl|'\n'
name|'db'
op|'.'
name|'bm_interface_set_vif_uuid'
op|','
nl|'\n'
name|'self'
op|'.'
name|'context'
op|','
name|'pif_id'
op|'+'
number|'1'
op|','
string|"'AAAA'"
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
