begin_unit
comment|'# Copyright 2014 NEC Corporation.'
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
op|'.'
name|'api'
op|'.'
name|'validation'
name|'import'
name|'parameter_types'
newline|'\n'
nl|'\n'
DECL|variable|rescue
name|'rescue'
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
string|"'rescue'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'object'"
op|','
string|"'null'"
op|']'
op|','
nl|'\n'
string|"'properties'"
op|':'
op|'{'
nl|'\n'
string|"'adminPass'"
op|':'
name|'parameter_types'
op|'.'
name|'admin_password'
op|','
nl|'\n'
string|"'rescue_image_ref'"
op|':'
name|'parameter_types'
op|'.'
name|'image_ref'
op|','
nl|'\n'
op|'}'
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
string|"'rescue'"
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
