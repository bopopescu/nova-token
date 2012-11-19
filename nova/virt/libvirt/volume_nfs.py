begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 NetApp, Inc.'
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
string|'"""Volume driver for using NFS as volumes storage. Nova compute part."""'
newline|'\n'
nl|'\n'
name|'import'
name|'ctypes'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'config'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'volume'
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
name|'StrOpt'
op|'('
string|"'nfs_mount_point_base'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'$state_path/mnt'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Base dir where nfs expected to be mounted on compute'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
DECL|variable|CONF
name|'CONF'
op|'='
name|'config'
op|'.'
name|'CONF'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'volume_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NfsVolumeDriver
name|'class'
name|'NfsVolumeDriver'
op|'('
name|'volume'
op|'.'
name|'LibvirtVolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""" Class implements libvirt part of volume driver for NFS\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create back-end to nfs and check connection"""'
newline|'\n'
name|'super'
op|'('
name|'NfsVolumeDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
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
name|'mount_device'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Connect the volume. Returns xml for libvirt."""'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_ensure_mounted'
op|'('
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'export'"
op|']'
op|')'
newline|'\n'
name|'path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'path'
op|','
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
op|'='
name|'path'
newline|'\n'
name|'conf'
op|'='
name|'super'
op|'('
name|'NfsVolumeDriver'
op|','
name|'self'
op|')'
op|'.'
name|'connect_volume'
op|'('
name|'connection_info'
op|','
nl|'\n'
name|'mount_device'
op|')'
newline|'\n'
name|'conf'
op|'.'
name|'source_type'
op|'='
string|"'file'"
newline|'\n'
name|'return'
name|'conf'
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
name|'mount_device'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Disconnect the volume"""'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|_ensure_mounted
dedent|''
name|'def'
name|'_ensure_mounted'
op|'('
name|'self'
op|','
name|'nfs_export'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        @type nfs_export: string\n        """'
newline|'\n'
name|'mount_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'CONF'
op|'.'
name|'nfs_mount_point_base'
op|','
nl|'\n'
name|'self'
op|'.'
name|'get_hash_str'
op|'('
name|'nfs_export'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_mount_nfs'
op|'('
name|'mount_path'
op|','
name|'nfs_export'
op|','
name|'ensure'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'mount_path'
newline|'\n'
nl|'\n'
DECL|member|_mount_nfs
dedent|''
name|'def'
name|'_mount_nfs'
op|'('
name|'self'
op|','
name|'mount_path'
op|','
name|'nfs_share'
op|','
name|'ensure'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Mount nfs export to mount path"""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_path_exists'
op|'('
name|'mount_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'mount_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'mount'"
op|','
string|"'-t'"
op|','
string|"'nfs'"
op|','
name|'nfs_share'
op|','
name|'mount_path'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'ensure'
name|'and'
string|"'already mounted'"
name|'in'
name|'exc'
op|'.'
name|'message'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"%s is already mounted"'
op|')'
op|','
name|'nfs_share'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|get_hash_str
name|'def'
name|'get_hash_str'
op|'('
name|'base_str'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""returns string that represents hash of base_str (in a hex format)"""'
newline|'\n'
name|'return'
name|'str'
op|'('
name|'ctypes'
op|'.'
name|'c_uint64'
op|'('
name|'hash'
op|'('
name|'base_str'
op|')'
op|')'
op|'.'
name|'value'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_path_exists
name|'def'
name|'_path_exists'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Check path """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'stat'"
op|','
name|'path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ProcessExecutionError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
