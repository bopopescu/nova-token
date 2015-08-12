begin_unit
comment|'# Copyright 2011 OpenStack Foundation'
nl|'\n'
comment|'# (c) Copyright 2013 Hewlett-Packard Development Company, L.P.'
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
string|'"""Volume drivers for libvirt."""'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'config'
name|'as'
name|'vconfig'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'utils'
name|'as'
name|'libvirt_utils'
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
DECL|variable|volume_opts
name|'volume_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'qemu_allowed_storage_drivers'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Protocols listed here will be accessed directly '"
nl|'\n'
string|"'from QEMU. Currently supported protocols: [gluster]'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'cfg'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'volume_opts'
op|','
string|"'libvirt'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtBaseVolumeDriver
name|'class'
name|'LibvirtBaseVolumeDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Base class for volume drivers."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|','
name|'is_block_dev'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'connection'
op|'='
name|'connection'
newline|'\n'
name|'self'
op|'.'
name|'is_block_dev'
op|'='
name|'is_block_dev'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'disk_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns xml for libvirt."""'
newline|'\n'
name|'conf'
op|'='
name|'vconfig'
op|'.'
name|'LibvirtConfigGuestDisk'
op|'('
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'driver_name'
op|'='
name|'libvirt_utils'
op|'.'
name|'pick_disk_driver_name'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'connection'
op|'.'
name|'_host'
op|'.'
name|'get_version'
op|'('
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'is_block_dev'
nl|'\n'
op|')'
newline|'\n'
nl|'\n'
name|'conf'
op|'.'
name|'source_device'
op|'='
name|'disk_info'
op|'['
string|"'type'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'driver_format'
op|'='
string|'"raw"'
newline|'\n'
name|'conf'
op|'.'
name|'driver_cache'
op|'='
string|'"none"'
newline|'\n'
name|'conf'
op|'.'
name|'target_dev'
op|'='
name|'disk_info'
op|'['
string|"'dev'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'target_bus'
op|'='
name|'disk_info'
op|'['
string|"'bus'"
op|']'
newline|'\n'
name|'conf'
op|'.'
name|'serial'
op|'='
name|'connection_info'
op|'.'
name|'get'
op|'('
string|"'serial'"
op|')'
newline|'\n'
nl|'\n'
comment|'# Support for block size tuning'
nl|'\n'
name|'data'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
string|"'data'"
name|'in'
name|'connection_info'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'logical_block_size'"
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'logical_block_size'
op|'='
name|'data'
op|'['
string|"'logical_block_size'"
op|']'
newline|'\n'
dedent|''
name|'if'
string|"'physical_block_size'"
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'            '
name|'conf'
op|'.'
name|'physical_block_size'
op|'='
name|'data'
op|'['
string|"'physical_block_size'"
op|']'
newline|'\n'
nl|'\n'
comment|'# Extract rate_limit control parameters'
nl|'\n'
dedent|''
name|'if'
string|"'qos_specs'"
name|'in'
name|'data'
name|'and'
name|'data'
op|'['
string|"'qos_specs'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'tune_opts'
op|'='
op|'['
string|"'total_bytes_sec'"
op|','
string|"'read_bytes_sec'"
op|','
nl|'\n'
string|"'write_bytes_sec'"
op|','
string|"'total_iops_sec'"
op|','
nl|'\n'
string|"'read_iops_sec'"
op|','
string|"'write_iops_sec'"
op|']'
newline|'\n'
name|'specs'
op|'='
name|'data'
op|'['
string|"'qos_specs'"
op|']'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'specs'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'for'
name|'k'
op|','
name|'v'
name|'in'
name|'six'
op|'.'
name|'iteritems'
op|'('
name|'specs'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
name|'k'
name|'in'
name|'tune_opts'
op|':'
newline|'\n'
indent|'                        '
name|'new_key'
op|'='
string|"'disk_'"
op|'+'
name|'k'
newline|'\n'
name|'setattr'
op|'('
name|'conf'
op|','
name|'new_key'
op|','
name|'v'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|"'Unknown content in connection_info/'"
nl|'\n'
string|"'qos_specs: %s'"
op|')'
op|','
name|'specs'
op|')'
newline|'\n'
nl|'\n'
comment|'# Extract access_mode control parameters'
nl|'\n'
dedent|''
dedent|''
name|'if'
string|"'access_mode'"
name|'in'
name|'data'
name|'and'
name|'data'
op|'['
string|"'access_mode'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'access_mode'
op|'='
name|'data'
op|'['
string|"'access_mode'"
op|']'
newline|'\n'
name|'if'
name|'access_mode'
name|'in'
op|'('
string|"'ro'"
op|','
string|"'rw'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'conf'
op|'.'
name|'readonly'
op|'='
name|'access_mode'
op|'=='
string|"'ro'"
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|"'Unknown content in '"
nl|'\n'
string|"'connection_info/access_mode: %s'"
op|')'
op|','
nl|'\n'
name|'access_mode'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolumeAccessMode'
op|'('
nl|'\n'
name|'access_mode'
op|'='
name|'access_mode'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
DECL|member|connect_volume
dedent|''
name|'def'
name|'connect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'disk_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Connect the volume. Returns xml for libvirt."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|disconnect_volume
dedent|''
name|'def'
name|'disconnect_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'disk_dev'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disconnect the volume."""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtVolumeDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtVolumeDriver'
op|'('
name|'LibvirtBaseVolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Class for volumes backed by local file."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LibvirtVolumeDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|','
name|'is_block_dev'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'disk_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns xml for libvirt."""'
newline|'\n'
name|'conf'
op|'='
name|'super'
op|'('
name|'LibvirtVolumeDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'disk_info'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'source_type'
op|'='
string|'"block"'
newline|'\n'
name|'conf'
op|'.'
name|'source_path'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
newline|'\n'
name|'return'
name|'conf'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|LibvirtFakeVolumeDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtFakeVolumeDriver'
op|'('
name|'LibvirtBaseVolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Driver to attach fake volumes to libvirt."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LibvirtFakeVolumeDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection'
op|','
name|'is_block_dev'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_config
dedent|''
name|'def'
name|'get_config'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'disk_info'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Returns xml for libvirt."""'
newline|'\n'
name|'conf'
op|'='
name|'super'
op|'('
name|'LibvirtFakeVolumeDriver'
op|','
nl|'\n'
name|'self'
op|')'
op|'.'
name|'get_config'
op|'('
name|'connection_info'
op|','
name|'disk_info'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'source_type'
op|'='
string|'"network"'
newline|'\n'
name|'conf'
op|'.'
name|'source_protocol'
op|'='
string|'"fake"'
newline|'\n'
name|'conf'
op|'.'
name|'source_name'
op|'='
string|'"fake"'
newline|'\n'
name|'return'
name|'conf'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit