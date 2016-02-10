begin_unit
comment|'# Copyright (c) 2013 The Johns Hopkins University/Applied Physics Laboratory'
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
string|'"""\nTest cases for the conf key manager.\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'array'
newline|'\n'
name|'import'
name|'codecs'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'conf_key_mgr'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'keymgr'
name|'import'
name|'key'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'tests'
op|'.'
name|'unit'
op|'.'
name|'keymgr'
name|'import'
name|'test_single_key_mgr'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'fixed_key'"
op|','
string|"'nova.keymgr.conf_key_mgr'"
op|','
name|'group'
op|'='
string|"'keymgr'"
op|')'
newline|'\n'
DECL|variable|decode_hex
name|'decode_hex'
op|'='
name|'codecs'
op|'.'
name|'getdecoder'
op|'('
string|'"hex_codec"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ConfKeyManagerTestCase
name|'class'
name|'ConfKeyManagerTestCase'
op|'('
name|'test_single_key_mgr'
op|'.'
name|'SingleKeyManagerTestCase'
op|')'
op|':'
newline|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'ConfKeyManagerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_hex_key'
op|'='
string|"'0'"
op|'*'
number|'64'
newline|'\n'
nl|'\n'
DECL|member|_create_key_manager
dedent|''
name|'def'
name|'_create_key_manager'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_default'
op|'('
string|"'fixed_key'"
op|','
name|'default'
op|'='
name|'self'
op|'.'
name|'_hex_key'
op|','
name|'group'
op|'='
string|"'keymgr'"
op|')'
newline|'\n'
name|'return'
name|'conf_key_mgr'
op|'.'
name|'ConfKeyManager'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setUp
dedent|''
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
name|'ConfKeyManagerTestCase'
op|','
name|'self'
op|')'
op|'.'
name|'setUp'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'encoded_key'
op|'='
name|'array'
op|'.'
name|'array'
op|'('
string|"'B'"
op|','
name|'decode_hex'
op|'('
name|'self'
op|'.'
name|'_hex_key'
op|')'
op|'['
number|'0'
op|']'
op|')'
op|'.'
name|'tolist'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'key'
op|'='
name|'key'
op|'.'
name|'SymmetricKey'
op|'('
string|"'AES'"
op|','
name|'encoded_key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_init
dedent|''
name|'def'
name|'test_init'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_manager'
op|'='
name|'self'
op|'.'
name|'_create_key_manager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_hex_key'
op|','
name|'key_manager'
op|'.'
name|'_hex_key'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_init_value_error
dedent|''
name|'def'
name|'test_init_value_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'CONF'
op|'.'
name|'set_default'
op|'('
string|"'fixed_key'"
op|','
name|'default'
op|'='
name|'None'
op|','
name|'group'
op|'='
string|"'keymgr'"
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertRaises'
op|'('
name|'ValueError'
op|','
name|'conf_key_mgr'
op|'.'
name|'ConfKeyManager'
op|')'
newline|'\n'
nl|'\n'
DECL|member|test_generate_hex_key
dedent|''
name|'def'
name|'test_generate_hex_key'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'key_manager'
op|'='
name|'self'
op|'.'
name|'_create_key_manager'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'assertEqual'
op|'('
name|'self'
op|'.'
name|'_hex_key'
op|','
name|'key_manager'
op|'.'
name|'_generate_hex_key'
op|'('
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
