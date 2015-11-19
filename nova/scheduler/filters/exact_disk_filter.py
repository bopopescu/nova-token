begin_unit
comment|'# Copyright (c) 2014 OpenStack Foundation'
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
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'scheduler'
name|'import'
name|'filters'
newline|'\n'
nl|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
name|'__name__'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|ExactDiskFilter
name|'class'
name|'ExactDiskFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Exact Disk Filter."""'
newline|'\n'
nl|'\n'
op|'@'
name|'filters'
op|'.'
name|'compat_legacy_props'
newline|'\n'
DECL|member|host_passes
name|'def'
name|'host_passes'
op|'('
name|'self'
op|','
name|'host_state'
op|','
name|'filter_properties'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return True if host has the exact amount of disk available."""'
newline|'\n'
name|'instance_type'
op|'='
name|'filter_properties'
op|'.'
name|'get'
op|'('
string|"'instance_type'"
op|')'
newline|'\n'
name|'requested_disk'
op|'='
op|'('
number|'1024'
op|'*'
op|'('
name|'instance_type'
op|'['
string|"'root_gb'"
op|']'
op|'+'
nl|'\n'
name|'instance_type'
op|'['
string|"'ephemeral_gb'"
op|']'
op|')'
op|'+'
nl|'\n'
name|'instance_type'
op|'['
string|"'swap'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'requested_disk'
op|'!='
name|'host_state'
op|'.'
name|'free_disk_mb'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"%(host_state)s does not have exactly "'
nl|'\n'
string|'"%(requested_disk)s MB usable disk, it "'
nl|'\n'
string|'"has %(usable_disk_mb)s."'
op|','
nl|'\n'
op|'{'
string|"'host_state'"
op|':'
name|'host_state'
op|','
nl|'\n'
string|"'requested_disk'"
op|':'
name|'requested_disk'
op|','
nl|'\n'
string|"'usable_disk_mb'"
op|':'
name|'host_state'
op|'.'
name|'free_disk_mb'
op|'}'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
