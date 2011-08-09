begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2011 Isaku Yamahata'
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
name|'nova'
name|'import'
name|'flags'
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
name|'import'
name|'driver'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|TestVirtDriver
name|'class'
name|'TestVirtDriver'
op|'('
name|'test'
op|'.'
name|'TestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_block_device
indent|'    '
name|'def'
name|'test_block_device'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'swap'
op|'='
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'1'
op|'}'
newline|'\n'
name|'ephemerals'
op|'='
op|'['
op|'{'
string|"'num'"
op|':'
number|'0'
op|','
nl|'\n'
string|"'virtual_name'"
op|':'
string|"'ephemeral0'"
op|','
nl|'\n'
string|"'device_name'"
op|':'
string|"'/dev/sdc1'"
op|','
nl|'\n'
string|"'size'"
op|':'
number|'1'
op|'}'
op|']'
newline|'\n'
name|'block_device_mapping'
op|'='
op|'['
op|'{'
string|"'mount_device'"
op|':'
string|"'/dev/sde'"
op|','
nl|'\n'
string|"'device_path'"
op|':'
string|"'fake_device'"
op|'}'
op|']'
newline|'\n'
name|'block_device_info'
op|'='
op|'{'
nl|'\n'
string|"'root_device_name'"
op|':'
string|"'/dev/sda'"
op|','
nl|'\n'
string|"'swap'"
op|':'
name|'swap'
op|','
nl|'\n'
string|"'ephemerals'"
op|':'
name|'ephemerals'
op|','
nl|'\n'
string|"'block_device_mapping'"
op|':'
name|'block_device_mapping'
op|'}'
newline|'\n'
nl|'\n'
name|'empty_block_device_info'
op|'='
op|'{'
op|'}'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_root'
op|'('
name|'block_device_info'
op|')'
op|','
string|"'/dev/sda'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_root'
op|'('
name|'empty_block_device_info'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_root'
op|'('
name|'None'
op|')'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'block_device_info'
op|')'
op|','
name|'swap'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
nl|'\n'
name|'empty_block_device_info'
op|')'
op|'['
string|"'device_name'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
nl|'\n'
name|'empty_block_device_info'
op|')'
op|'['
string|"'swap_size'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
op|'{'
string|"'swap'"
op|':'
name|'None'
op|'}'
op|')'
op|'['
string|"'device_name'"
op|']'
op|','
nl|'\n'
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
op|'{'
string|"'swap'"
op|':'
name|'None'
op|'}'
op|')'
op|'['
string|"'swap_size'"
op|']'
op|','
nl|'\n'
number|'0'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'None'
op|')'
op|'['
string|"'device_name'"
op|']'
op|','
name|'None'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_swap'
op|'('
name|'None'
op|')'
op|'['
string|"'swap_size'"
op|']'
op|','
number|'0'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
name|'block_device_info'
op|')'
op|','
nl|'\n'
name|'ephemerals'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
name|'empty_block_device_info'
op|')'
op|','
nl|'\n'
op|'['
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
nl|'\n'
name|'driver'
op|'.'
name|'block_device_info_get_ephemerals'
op|'('
name|'None'
op|')'
op|','
nl|'\n'
op|'['
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_swap_is_usable
dedent|''
name|'def'
name|'test_swap_is_usable'
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
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
name|'None'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
op|'{'
string|"'device_name'"
op|':'
name|'None'
op|'}'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertFalse'
op|'('
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'0'
op|'}'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertTrue'
op|'('
name|'driver'
op|'.'
name|'swap_is_usable'
op|'('
op|'{'
string|"'device_name'"
op|':'
string|"'/dev/sdb'"
op|','
nl|'\n'
string|"'swap_size'"
op|':'
number|'1'
op|'}'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
