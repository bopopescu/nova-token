begin_unit
comment|'# Copyright (c) 2012 OpenStack, LLC.'
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
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
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
DECL|variable|disk_allocation_ratio_opt
name|'disk_allocation_ratio_opt'
op|'='
name|'cfg'
op|'.'
name|'FloatOpt'
op|'('
string|'"disk_allocation_ratio"'
op|','
name|'default'
op|'='
number|'1.0'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|'"virtual disk to physical disk allocation ratio"'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opt'
op|'('
name|'disk_allocation_ratio_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|DiskFilter
name|'class'
name|'DiskFilter'
op|'('
name|'filters'
op|'.'
name|'BaseHostFilter'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Disk Filter with over subscription flag"""'
newline|'\n'
nl|'\n'
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
string|'"""Filter based on disk usage"""'
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
newline|'\n'
nl|'\n'
name|'free_disk_mb'
op|'='
name|'host_state'
op|'.'
name|'free_disk_mb'
newline|'\n'
name|'total_usable_disk_mb'
op|'='
name|'host_state'
op|'.'
name|'total_usable_disk_gb'
op|'*'
number|'1024'
newline|'\n'
nl|'\n'
name|'disk_mb_limit'
op|'='
name|'total_usable_disk_mb'
op|'*'
name|'CONF'
op|'.'
name|'disk_allocation_ratio'
newline|'\n'
name|'used_disk_mb'
op|'='
name|'total_usable_disk_mb'
op|'-'
name|'free_disk_mb'
newline|'\n'
name|'usable_disk_mb'
op|'='
name|'disk_mb_limit'
op|'-'
name|'used_disk_mb'
newline|'\n'
nl|'\n'
name|'if'
name|'not'
name|'usable_disk_mb'
op|'>='
name|'requested_disk'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"%(host_state)s does not have %(requested_disk)s MB "'
nl|'\n'
string|'"usable disk, it only has %(usable_disk_mb)s MB usable "'
nl|'\n'
string|'"disk."'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'disk_gb_limit'
op|'='
name|'disk_mb_limit'
op|'/'
number|'1024'
newline|'\n'
name|'host_state'
op|'.'
name|'limits'
op|'['
string|"'disk_gb'"
op|']'
op|'='
name|'disk_gb_limit'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
