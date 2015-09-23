begin_unit
comment|'# Copyright 2013 NEC Corporation.  All rights reserved.'
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
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'validation'
name|'import'
name|'parameter_types'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|create
name|'create'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'keypair'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'parameter_types'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'public_key'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'keypair'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|create_v20
name|'create_v20'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'create'
op|')'
newline|'\n'
name|'create_v20'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'keypair'"
op|']'
op|'['
string|"'properties'"
op|']'
op|'['
string|"'name'"
op|']'
op|'='
op|'('
name|'parameter_types'
op|'.'
nl|'\n'
name|'name_with_leading_trailing_spaces'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|create_v22
name|'create_v22'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'keypair'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'parameter_types'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'type'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'enum'"
op|':'
op|'['
string|"'ssh'"
op|','
string|"'x509'"
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'public_key'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'keypair'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|create_v210
name|'create_v210'
op|'='
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'keypair'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'object'"
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'name'"
op|':'
name|'parameter_types'
op|'.'
name|'name'
op|','
nl|'\n'
string|"'type'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'enum'"
op|':'
op|'['
string|"'ssh'"
op|','
string|"'x509'"
op|']'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'public_key'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
string|"'user_id'"
op|':'
op|'{'
string|"'type'"
op|':'
string|"'string'"
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'keypair'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|server_create
name|'server_create'
op|'='
op|'{'
nl|'\n'
string|"'key_name'"
op|':'
name|'parameter_types'
op|'.'
name|'name'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|server_create_v20
name|'server_create_v20'
op|'='
op|'{'
nl|'\n'
string|"'key_name'"
op|':'
name|'parameter_types'
op|'.'
name|'name_with_leading_trailing_spaces'
op|','
nl|'\n'
op|'}'
newline|'\n'
endmarker|''
end_unit
