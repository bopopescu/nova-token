begin_unit
comment|'# Copyright 2014 IBM Corporation.  All rights reserved.'
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
nl|'\n'
DECL|variable|ip_range
name|'ip_range'
op|'='
op|'{'
nl|'\n'
comment|'# TODO(eliqiao) need to find a better pattern'
nl|'\n'
string|"'type'"
op|':'
string|"'string'"
op|','
nl|'\n'
string|"'pattern'"
op|':'
string|"'^[0-9./a-fA-F]*$'"
op|','
nl|'\n'
op|'}'
newline|'\n'
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
string|"'floating_ips_bulk_create'"
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
string|"'ip_range'"
op|':'
name|'ip_range'
op|','
nl|'\n'
string|"'pool'"
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
string|"'interface'"
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
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'ip_range'"
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
string|"'floating_ips_bulk_create'"
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
DECL|variable|delete
name|'delete'
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
string|"'ip_range'"
op|':'
name|'ip_range'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'ip_range'"
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
endmarker|''
end_unit