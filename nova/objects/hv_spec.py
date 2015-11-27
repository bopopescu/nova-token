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
name|'from'
name|'oslo_utils'
name|'import'
name|'versionutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'hv_type'
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
op|'@'
name|'base'
op|'.'
name|'NovaObjectRegistry'
op|'.'
name|'register'
newline|'\n'
DECL|class|HVSpec
name|'class'
name|'HVSpec'
op|'('
name|'base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
comment|'# Version 1.0: Initial version'
nl|'\n'
comment|"# Version 1.1: Added 'vz' hypervisor"
nl|'\n'
comment|"# Version 1.2: Added 'lxd' hypervisor"
nl|'\n'
DECL|variable|VERSION
indent|'    '
name|'VERSION'
op|'='
string|"'1.2'"
newline|'\n'
nl|'\n'
DECL|variable|fields
name|'fields'
op|'='
op|'{'
nl|'\n'
string|"'arch'"
op|':'
name|'fields'
op|'.'
name|'ArchitectureField'
op|'('
op|')'
op|','
nl|'\n'
string|"'hv_type'"
op|':'
name|'fields'
op|'.'
name|'HVTypeField'
op|'('
op|')'
op|','
nl|'\n'
string|"'vm_mode'"
op|':'
name|'fields'
op|'.'
name|'VMModeField'
op|'('
op|')'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
comment|'# NOTE(pmurray): for backward compatibility, the supported instance'
nl|'\n'
comment|'# data is stored in the database as a list.'
nl|'\n'
op|'@'
name|'classmethod'
newline|'\n'
DECL|member|from_list
name|'def'
name|'from_list'
op|'('
name|'cls'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'cls'
op|'('
name|'arch'
op|'='
name|'data'
op|'['
number|'0'
op|']'
op|','
nl|'\n'
name|'hv_type'
op|'='
name|'data'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
name|'vm_mode'
op|'='
name|'data'
op|'['
number|'2'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|to_list
dedent|''
name|'def'
name|'to_list'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
op|'['
name|'self'
op|'.'
name|'arch'
op|','
name|'self'
op|'.'
name|'hv_type'
op|','
name|'self'
op|'.'
name|'vm_mode'
op|']'
newline|'\n'
nl|'\n'
DECL|member|obj_make_compatible
dedent|''
name|'def'
name|'obj_make_compatible'
op|'('
name|'self'
op|','
name|'primitive'
op|','
name|'target_version'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'HVSpec'
op|','
name|'self'
op|')'
op|'.'
name|'obj_make_compatible'
op|'('
name|'primitive'
op|','
name|'target_version'
op|')'
newline|'\n'
name|'target_version'
op|'='
name|'versionutils'
op|'.'
name|'convert_version_to_tuple'
op|'('
name|'target_version'
op|')'
newline|'\n'
name|'if'
op|'('
name|'target_version'
op|'<'
op|'('
number|'1'
op|','
number|'1'
op|')'
name|'and'
string|"'hv_type'"
name|'in'
name|'primitive'
name|'and'
nl|'\n'
name|'hv_type'
op|'.'
name|'VIRTUOZZO'
op|'=='
name|'primitive'
op|'['
string|"'hv_type'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'primitive'
op|'['
string|"'hv_type'"
op|']'
op|'='
name|'hv_type'
op|'.'
name|'PARALLELS'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
