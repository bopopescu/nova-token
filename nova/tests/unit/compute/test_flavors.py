begin_unit
comment|'# Copyright 2014 IBM Corp.'
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
string|'"""Tests for flavor basic functions"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'flavors'
newline|'\n'
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
nl|'\n'
nl|'\n'
DECL|class|ExtraSpecTestCase
name|'class'
name|'ExtraSpecTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|_flavor_validate_extra_spec_keys_invalid_input
indent|'    '
name|'def'
name|'_flavor_validate_extra_spec_keys_invalid_input'
op|'('
name|'self'
op|','
name|'key_name_list'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'exception'
op|'.'
name|'InvalidInput'
op|','
nl|'\n'
name|'flavors'
op|'.'
name|'validate_extra_spec_keys'
op|','
name|'key_name_list'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_validate_extra_spec_keys_invalid_input
dedent|''
name|'def'
name|'test_flavor_validate_extra_spec_keys_invalid_input'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'lists'
op|'='
op|'['
op|'['
string|"''"
op|','
op|']'
op|','
op|'['
string|"'*'"
op|','
op|']'
op|','
op|'['
string|"'+'"
op|','
op|']'
op|']'
newline|'\n'
name|'for'
name|'x'
name|'in'
name|'lists'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_flavor_validate_extra_spec_keys_invalid_input'
op|'('
name|'x'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_flavor_validate_extra_spec_keys
dedent|''
dedent|''
name|'def'
name|'test_flavor_validate_extra_spec_keys'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_name_list'
op|'='
op|'['
string|"'abc'"
op|','
string|"'ab c'"
op|','
string|"'a-b-c'"
op|','
string|"'a_b-c'"
op|','
string|"'a:bc'"
op|']'
newline|'\n'
name|'flavors'
op|'.'
name|'validate_extra_spec_keys'
op|'('
name|'key_name_list'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|CreateFlavorTestCase
dedent|''
dedent|''
name|'class'
name|'CreateFlavorTestCase'
op|'('
name|'test'
op|'.'
name|'NoDBTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|test_create_flavor_ram_error
indent|'    '
name|'def'
name|'test_create_flavor_ram_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'('
string|'"ram_test"'
op|','
string|'"9999999999"'
op|','
string|'"1"'
op|','
string|'"10"'
op|','
string|'"1"'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavors'
op|'.'
name|'create'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Be sure this will never be executed."'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"ram"'
op|','
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_flavor_disk_error
dedent|''
dedent|''
name|'def'
name|'test_create_flavor_disk_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'('
string|'"disk_test"'
op|','
string|'"1024"'
op|','
string|'"1"'
op|','
string|'"9999999999"'
op|','
string|'"1"'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavors'
op|'.'
name|'create'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Be sure this will never be executed."'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"disk"'
op|','
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_create_flavor_ephemeral_error
dedent|''
dedent|''
name|'def'
name|'test_create_flavor_ephemeral_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'('
string|'"ephemeral_test"'
op|','
string|'"1024"'
op|','
string|'"1"'
op|','
string|'"10"'
op|','
string|'"9999999999"'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'flavors'
op|'.'
name|'create'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'fail'
op|'('
string|'"Be sure this will never be executed."'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidInput'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'assertIn'
op|'('
string|'"ephemeral"'
op|','
name|'e'
op|'.'
name|'message'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
