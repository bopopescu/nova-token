begin_unit
comment|'#    Copyright 2014 Red Hat, Inc.'
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
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkRequest
name|'class'
name|'NetworkRequest'
op|'('
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|'# Version 1.1: Added pci_request_id'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'network_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'address'"
op|':'
name|'fields'
op|'.'
name|'IPAddressField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'port_id'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
string|"'pci_request_id'"
op|':'
name|'fields'
op|'.'
name|'UUIDField'
op|'('
name|'nullable'
op|'='
name|'True'
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|obj_load_attr
name|'def'
name|'obj_load_attr'
op|'('
name|'self'
op|','
name|'attr'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'setattr'
op|'('
name|'self'
op|','
name|'attr'
op|','
name|'None'
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_tuple
dedent|''
name|'def'
name|'to_tuple'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'address'
op|'='
name|'str'
op|'('
name|'self'
op|'.'
name|'address'
op|')'
name|'if'
name|'self'
op|'.'
name|'address'
name|'is'
name|'not'
name|'None'
name|'else'
name|'None'
newline|'\n'
name|'if'
name|'utils'
op|'.'
name|'is_neutron'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'network_id'
op|','
name|'address'
op|','
name|'self'
op|'.'
name|'port_id'
op|','
name|'self'
op|'.'
name|'pci_request_id'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'network_id'
op|','
name|'address'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_tuple
name|'def'
name|'from_tuple'
op|'('
name|'cls'
op|','
name|'net_tuple'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'len'
op|'('
name|'net_tuple'
op|')'
op|'=='
number|'4'
op|':'
newline|'\n'
indent|'            '
name|'network_id'
op|','
name|'address'
op|','
name|'port_id'
op|','
name|'pci_request_id'
op|'='
name|'net_tuple'
newline|'\n'
name|'return'
name|'cls'
op|'('
name|'network_id'
op|'='
name|'network_id'
op|','
name|'address'
op|'='
name|'address'
op|','
nl|'\n'
name|'port_id'
op|'='
name|'port_id'
op|','
name|'pci_request_id'
op|'='
name|'pci_request_id'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'len'
op|'('
name|'net_tuple'
op|')'
op|'=='
number|'3'
op|':'
newline|'\n'
comment|'# NOTE(alex_xu): This is only for compatible with icehouse , and'
nl|'\n'
comment|'# should be removed in the next cycle.'
nl|'\n'
indent|'            '
name|'network_id'
op|','
name|'address'
op|','
name|'port_id'
op|'='
name|'net_tuple'
newline|'\n'
name|'return'
name|'cls'
op|'('
name|'network_id'
op|'='
name|'network_id'
op|','
name|'address'
op|'='
name|'address'
op|','
nl|'\n'
name|'port_id'
op|'='
name|'port_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'network_id'
op|','
name|'address'
op|'='
name|'net_tuple'
newline|'\n'
name|'return'
name|'cls'
op|'('
name|'network_id'
op|'='
name|'network_id'
op|','
name|'address'
op|'='
name|'address'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NetworkRequestList
dedent|''
dedent|''
dedent|''
name|'class'
name|'NetworkRequestList'
op|'('
name|'obj_base'
op|'.'
name|'ObjectListBase'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
DECL|variable|fields
indent|'    '
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'NetworkRequest'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|variable|child_versions
name|'child_versions'
op|'='
op|'{'
nl|'\n'
string|"'1.0'"
op|':'
string|"'1.0'"
op|','
nl|'\n'
string|"'1.1'"
op|':'
string|"'1.1'"
op|','
nl|'\n'
op|'}'
newline|'\n'
DECL|variable|VERSION
name|'VERSION'
op|'='
string|"'1.1'"
newline|'\n'
nl|'\n'
DECL|member|as_tuples
name|'def'
name|'as_tuples'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'x'
op|'.'
name|'to_tuple'
op|'('
op|')'
name|'for'
name|'x'
name|'in'
name|'self'
op|'.'
name|'objects'
op|']'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|is_single_unspecified
name|'def'
name|'is_single_unspecified'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'('
op|'('
name|'len'
op|'('
name|'self'
op|'.'
name|'objects'
op|')'
op|'=='
number|'1'
op|')'
name|'and'
nl|'\n'
op|'('
name|'self'
op|'.'
name|'objects'
op|'['
number|'0'
op|']'
op|'.'
name|'to_tuple'
op|'('
op|')'
op|'=='
name|'NetworkRequest'
op|'('
op|')'
op|'.'
name|'to_tuple'
op|'('
op|')'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
