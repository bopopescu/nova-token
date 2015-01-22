begin_unit
comment|'# Copyright (c) 2014 Hewlett-Packard Development Company, L.P.'
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
name|'import'
name|'copy'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'fields'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciDevicePool
name|'class'
name|'PciDevicePool'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.0'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'product_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'vendor_id'"
op|':'
name|'fields'
op|'.'
name|'StringField'
op|'('
op|')'
op|','
nl|'\n'
string|"'tags'"
op|':'
name|'fields'
op|'.'
name|'DictOfNullableStringsField'
op|'('
op|')'
op|','
nl|'\n'
string|"'count'"
op|':'
name|'fields'
op|'.'
name|'IntegerField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# NOTE(pmurray): before this object existed the pci device pool data was'
nl|'\n'
comment|'# stored as a dict. For backward compatibility we need to be able to read'
nl|'\n'
comment|'# it in from a dict'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_dict
name|'def'
name|'from_dict'
op|'('
name|'cls'
op|','
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pool_dict'
op|'='
name|'copy'
op|'.'
name|'copy'
op|'('
name|'value'
op|')'
newline|'\n'
name|'pool'
op|'='
name|'cls'
op|'('
op|')'
newline|'\n'
name|'pool'
op|'.'
name|'vendor_id'
op|'='
name|'pool_dict'
op|'.'
name|'pop'
op|'('
string|'"vendor_id"'
op|')'
newline|'\n'
name|'pool'
op|'.'
name|'product_id'
op|'='
name|'pool_dict'
op|'.'
name|'pop'
op|'('
string|'"product_id"'
op|')'
newline|'\n'
name|'pool'
op|'.'
name|'count'
op|'='
name|'pool_dict'
op|'.'
name|'pop'
op|'('
string|'"count"'
op|')'
newline|'\n'
name|'pool'
op|'.'
name|'tags'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'pool'
op|'.'
name|'tags'
op|'.'
name|'update'
op|'('
name|'pool_dict'
op|')'
newline|'\n'
name|'return'
name|'pool'
newline|'\n'
nl|'\n'
comment|'# NOTE(sbauza): Before using objects, pci stats was a list of'
nl|'\n'
comment|"# dictionaries not having tags. For compatibility with other modules, let's"
nl|'\n'
comment|'# create a reversible method'
nl|'\n'
DECL|member|to_dict
dedent|''
name|'def'
name|'to_dict'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pci_pool'
op|'='
name|'base'
op|'.'
name|'obj_to_primitive'
op|'('
name|'self'
op|')'
newline|'\n'
name|'tags'
op|'='
name|'pci_pool'
op|'.'
name|'pop'
op|'('
string|"'tags'"
op|','
name|'None'
op|')'
newline|'\n'
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'tags'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pci_pool'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
dedent|''
name|'return'
name|'pci_pool'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|PciDevicePoolList
dedent|''
dedent|''
name|'class'
name|'PciDevicePoolList'
op|'('
name|'base'
op|'.'
name|'ObjectListBase'
op|','
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial verison'
nl|'\n'
comment|'#              PciDevicePool <= 1.0'
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
string|"'objects'"
op|':'
name|'fields'
op|'.'
name|'ListOfObjectsField'
op|'('
string|"'PciDevicePool'"
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
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
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|from_pci_stats
dedent|''
name|'def'
name|'from_pci_stats'
op|'('
name|'pci_stats'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create and return a PciDevicePoolList from the data stored in the db,\n    which can be either the serialized object, or, prior to the creation of the\n    device pool objects, a simple dict or a list of such dicts.\n    """'
newline|'\n'
name|'pools'
op|'='
name|'None'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'pci_stats'
op|','
name|'six'
op|'.'
name|'string_types'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'pci_stats'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
name|'pci_stats'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'TypeError'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'pci_stats'
op|'='
name|'None'
newline|'\n'
dedent|''
dedent|''
name|'if'
name|'pci_stats'
op|':'
newline|'\n'
comment|'# Check for object-ness, or old-style storage format.'
nl|'\n'
indent|'        '
name|'if'
string|"'nova_object.namespace'"
name|'in'
name|'pci_stats'
op|':'
newline|'\n'
indent|'            '
name|'pools'
op|'='
name|'objects'
op|'.'
name|'PciDevicePoolList'
op|'.'
name|'obj_from_primitive'
op|'('
name|'pci_stats'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# This can be either a dict or a list of dicts'
nl|'\n'
indent|'            '
name|'if'
name|'isinstance'
op|'('
name|'pci_stats'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'pool_list'
op|'='
op|'['
name|'objects'
op|'.'
name|'PciDevicePool'
op|'.'
name|'from_dict'
op|'('
name|'stat'
op|')'
nl|'\n'
name|'for'
name|'stat'
name|'in'
name|'pci_stats'
op|']'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'pool_list'
op|'='
op|'['
name|'objects'
op|'.'
name|'PciDevicePool'
op|'.'
name|'from_dict'
op|'('
name|'pci_stats'
op|')'
op|']'
newline|'\n'
dedent|''
name|'pools'
op|'='
name|'objects'
op|'.'
name|'PciDevicePoolList'
op|'('
name|'objects'
op|'='
name|'pool_list'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'pools'
newline|'\n'
dedent|''
endmarker|''
end_unit
