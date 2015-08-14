begin_unit
comment|'# Copyright 2014 NEC Corporation.  All rights reserved.'
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
op|'.'
name|'api'
op|'.'
name|'validation'
name|'import'
name|'parameter_types'
newline|'\n'
nl|'\n'
DECL|variable|service_update
name|'service_update'
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
string|"'host'"
op|':'
name|'parameter_types'
op|'.'
name|'hostname'
op|','
nl|'\n'
string|"'binary'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'host'"
op|','
string|"'binary'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|service_update_v211
name|'service_update_v211'
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
string|"'host'"
op|':'
name|'parameter_types'
op|'.'
name|'hostname'
op|','
nl|'\n'
string|"'binary'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'disabled_reason'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
string|"'minLength'"
op|':'
number|'1'
op|','
string|"'maxLength'"
op|':'
number|'255'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'forced_down'"
op|':'
name|'parameter_types'
op|'.'
name|'boolean'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'host'"
op|','
string|"'binary'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
nl|'\n'
op|'}'
newline|'\n'
endmarker|''
end_unit