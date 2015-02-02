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
nl|'\n'
DECL|variable|base_create
name|'base_create'
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
string|"'server'"
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
name|'hostname'
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'parameter_types'
op|'.'
name|'image_ref'
op|','
nl|'\n'
string|"'flavorRef'"
op|':'
name|'parameter_types'
op|'.'
name|'flavor_ref'
op|','
nl|'\n'
string|"'adminPass'"
op|':'
name|'parameter_types'
op|'.'
name|'admin_password'
op|','
nl|'\n'
string|"'metadata'"
op|':'
name|'parameter_types'
op|'.'
name|'metadata'
op|','
nl|'\n'
string|"'networks'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
string|"'array'"
op|','
nl|'\n'
string|"'items'"
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
string|"'fixed_ip'"
op|':'
name|'parameter_types'
op|'.'
name|'ip_address'
op|','
nl|'\n'
string|"'port'"
op|':'
op|'{'
nl|'\n'
string|"'type'"
op|':'
op|'['
string|"'string'"
op|','
string|"'null'"
op|']'
op|','
nl|'\n'
string|"'format'"
op|':'
string|"'uuid'"
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'uuid'"
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
string|"'additionalProperties'"
op|':'
name|'False'
op|','
nl|'\n'
op|'}'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'name'"
op|','
string|"'flavorRef'"
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
string|"'server'"
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
DECL|variable|base_update
name|'base_update'
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
string|"'server'"
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
name|'hostname'
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
string|"'server'"
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
DECL|variable|base_rebuild
name|'base_rebuild'
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
string|"'rebuild'"
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
name|'hostname'
op|','
nl|'\n'
string|"'imageRef'"
op|':'
name|'parameter_types'
op|'.'
name|'image_ref'
op|','
nl|'\n'
string|"'adminPass'"
op|':'
name|'parameter_types'
op|'.'
name|'admin_password'
op|','
nl|'\n'
string|"'metadata'"
op|':'
name|'parameter_types'
op|'.'
name|'metadata'
op|','
nl|'\n'
string|"'preserve_ephemeral'"
op|':'
name|'parameter_types'
op|'.'
name|'boolean'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'imageRef'"
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
string|"'rebuild'"
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
DECL|variable|base_resize
name|'base_resize'
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
string|"'resize'"
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
string|"'flavorRef'"
op|':'
name|'parameter_types'
op|'.'
name|'flavor_ref'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'flavorRef'"
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
string|"'resize'"
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
DECL|variable|create_image
name|'create_image'
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
string|"'createImage'"
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
string|"'metadata'"
op|':'
name|'parameter_types'
op|'.'
name|'metadata'
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
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'createImage'"
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
DECL|variable|reboot
name|'reboot'
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
string|"'reboot'"
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
string|"'type'"
op|':'
op|'{'
nl|'\n'
string|"'enum'"
op|':'
op|'['
string|"'HARD'"
op|','
string|"'Hard'"
op|','
string|"'hard'"
op|','
string|"'SOFT'"
op|','
string|"'Soft'"
op|','
string|"'soft'"
op|']'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'type'"
op|']'
op|','
nl|'\n'
string|"'additionalProperties'"
op|':'
name|'False'
nl|'\n'
op|'}'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'reboot'"
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
