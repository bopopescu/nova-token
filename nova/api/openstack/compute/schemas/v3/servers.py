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
name|'name'
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
string|"'oneOf'"
op|':'
op|'['
nl|'\n'
op|'{'
string|"'format'"
op|':'
string|"'ipv4'"
op|'}'
op|','
nl|'\n'
op|'{'
string|"'format'"
op|':'
string|"'ipv6'"
op|'}'
nl|'\n'
op|']'
nl|'\n'
op|'}'
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
comment|'# TODO(oomichi): After all extension schema patches are merged,'
nl|'\n'
comment|'# this code should be enabled. If enabling before merger, API'
nl|'\n'
comment|'# extension parameters would be considered as bad parameters.'
nl|'\n'
comment|"# 'additionalProperties': False,"
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
comment|'# TODO(oomichi): Now v3 code will be used for v2.1 only and v2.1 needs'
nl|'\n'
comment|'# to allow additionalProperties for some extensions.'
nl|'\n'
comment|"# 'additionalProperties': False,"
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
name|'name'
op|','
nl|'\n'
op|'}'
op|','
nl|'\n'
comment|'# TODO(oomichi): ditto, enable here after all extension schema'
nl|'\n'
comment|'# patches are merged.'
nl|'\n'
comment|"# 'additionalProperties': False,"
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
endmarker|''
end_unit
