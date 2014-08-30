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
comment|'# NOTE(oomichi): The metadata of flavor_extraspecs should accept numbers'
nl|'\n'
comment|'# as its values.'
nl|'\n'
DECL|variable|metadata
name|'metadata'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'parameter_types'
op|'.'
name|'metadata'
op|')'
newline|'\n'
name|'metadata'
op|'['
string|"'patternProperties'"
op|']'
op|'['
string|"'^[a-zA-Z0-9-_:. ]{1,255}$'"
op|']'
op|'['
string|"'type'"
op|']'
op|'='
op|'['
string|"'string'"
op|','
string|"'number'"
op|']'
newline|'\n'
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
string|"'extra_specs'"
op|':'
name|'metadata'
nl|'\n'
op|'}'
op|','
nl|'\n'
string|"'required'"
op|':'
op|'['
string|"'extra_specs'"
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
DECL|variable|update
name|'update'
op|'='
name|'copy'
op|'.'
name|'deepcopy'
op|'('
name|'metadata'
op|')'
newline|'\n'
name|'update'
op|'.'
name|'update'
op|'('
op|'{'
nl|'\n'
string|"'minProperties'"
op|':'
number|'1'
op|','
nl|'\n'
string|"'maxProperties'"
op|':'
number|'1'
nl|'\n'
op|'}'
op|')'
newline|'\n'
endmarker|''
end_unit
