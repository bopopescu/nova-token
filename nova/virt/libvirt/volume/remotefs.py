begin_unit
comment|'# Copyright 2014 Cloudbase Solutions Srl'
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
name|'abc'
newline|'\n'
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tempfile'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
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
name|'from'
name|'oslo_utils'
name|'import'
name|'importutils'
newline|'\n'
name|'import'
name|'six'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_LE'
op|','
name|'_LW'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|libvirt_opts
name|'libvirt_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'remote_filesystem_transport'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'ssh'"
op|','
nl|'\n'
DECL|variable|choices
name|'choices'
op|'='
op|'('
string|"'ssh'"
op|','
string|"'rsync'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use ssh or rsync transport for creating, copying, '"
nl|'\n'
string|"'removing files on the remote host.'"
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
name|'libvirt_opts'
op|','
string|"'libvirt'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mount_share
name|'def'
name|'mount_share'
op|'('
name|'mount_path'
op|','
name|'export_path'
op|','
nl|'\n'
name|'export_type'
op|','
name|'options'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Mount a remote export to mount_path.\n\n    :param mount_path: place where the remote export will be mounted\n    :param export_path: path of the export to be mounted\n    :export_type: remote export type (e.g. cifs, nfs, etc.)\n    :options: A list containing mount options\n    """'
newline|'\n'
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
name|'mount_cmd'
op|'='
op|'['
string|"'mount'"
op|','
string|"'-t'"
op|','
name|'export_type'
op|']'
newline|'\n'
name|'if'
name|'options'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'mount_cmd'
op|'.'
name|'extend'
op|'('
name|'options'
op|')'
newline|'\n'
dedent|''
name|'mount_cmd'
op|'.'
name|'extend'
op|'('
op|'['
name|'export_path'
op|','
name|'mount_path'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'mount_cmd'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'Device or resource busy'"
name|'in'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"%s is already mounted"'
op|')'
op|','
name|'export_path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unmount_share
dedent|''
dedent|''
dedent|''
name|'def'
name|'unmount_share'
op|'('
name|'mount_path'
op|','
name|'export_path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Unmount a remote share.\n\n    :param mount_path: remote export mount point\n    :param export_path: path of the remote export to be unmounted\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'umount'"
op|','
name|'mount_path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|','
nl|'\n'
name|'attempts'
op|'='
number|'3'
op|','
name|'delay_on_retry'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'processutils'
op|'.'
name|'ProcessExecutionError'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'        '
name|'if'
string|"'target is busy'"
name|'in'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'exc'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"The share %s is still in use."'
op|','
name|'export_path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"Couldn\'t unmount the share %s"'
op|')'
op|','
nl|'\n'
name|'export_path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RemoteFilesystem
dedent|''
dedent|''
dedent|''
name|'class'
name|'RemoteFilesystem'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Represents actions that can be taken on a remote host\'s filesystem."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'transport'
op|'='
name|'CONF'
op|'.'
name|'libvirt'
op|'.'
name|'remote_filesystem_transport'
newline|'\n'
name|'cls_name'
op|'='
string|"'.'"
op|'.'
name|'join'
op|'('
op|'['
name|'__name__'
op|','
name|'transport'
op|'.'
name|'capitalize'
op|'('
op|')'
op|']'
op|')'
newline|'\n'
name|'cls_name'
op|'+='
string|"'Driver'"
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'='
name|'importutils'
op|'.'
name|'import_object'
op|'('
name|'cls_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_file
dedent|''
name|'def'
name|'create_file'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating file %s on remote host %s"'
op|','
name|'dst_path'
op|','
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_file'
op|'('
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_file
dedent|''
name|'def'
name|'remove_file'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Removing file %s on remote host %s"'
op|','
name|'dst_path'
op|','
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'remove_file'
op|'('
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_dir
dedent|''
name|'def'
name|'create_dir'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Creating directory %s on remote host %s"'
op|','
name|'dst_path'
op|','
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'create_dir'
op|'('
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_dir
dedent|''
name|'def'
name|'remove_dir'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Removing directory %s on remote host %s"'
op|','
name|'dst_path'
op|','
name|'host'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'remove_dir'
op|'('
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|copy_file
dedent|''
name|'def'
name|'copy_file'
op|'('
name|'self'
op|','
name|'src'
op|','
name|'dst'
op|','
name|'on_execute'
op|'='
name|'None'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'None'
op|','
name|'compression'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Copying file %s to %s"'
op|','
name|'src'
op|','
name|'dst'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'driver'
op|'.'
name|'copy_file'
op|'('
name|'src'
op|','
name|'dst'
op|','
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|','
nl|'\n'
name|'compression'
op|'='
name|'compression'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'six'
op|'.'
name|'add_metaclass'
op|'('
name|'abc'
op|'.'
name|'ABCMeta'
op|')'
newline|'\n'
DECL|class|RemoteFilesystemDriver
name|'class'
name|'RemoteFilesystemDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|create_file
name|'def'
name|'create_file'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create file on the remote system.\n\n        :param host: Remote host\n        :param dst_path: Destination path\n        :param on_execute: Callback method to store pid of process in cache\n        :param on_completion: Callback method to remove pid of process from\n                              cache\n        """'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|remove_file
name|'def'
name|'remove_file'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes a file on a remote host.\n\n        :param host: Remote host\n        :param dst_path: Destination path\n        :param on_execute: Callback method to store pid of process in cache\n        :param on_completion: Callback method to remove pid of process from\n                              cache\n        """'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|create_dir
name|'def'
name|'create_dir'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create directory on the remote system.\n\n        :param host: Remote host\n        :param dst_path: Destination path\n        :param on_execute: Callback method to store pid of process in cache\n        :param on_completion: Callback method to remove pid of process from\n                              cache\n        """'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|remove_dir
name|'def'
name|'remove_dir'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes a directory on a remote host.\n\n        :param host: Remote host\n        :param dst_path: Destination path\n        :param on_execute: Callback method to store pid of process in cache\n        :param on_completion: Callback method to remove pid of process from\n                              cache\n        """'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'abc'
op|'.'
name|'abstractmethod'
newline|'\n'
DECL|member|copy_file
name|'def'
name|'copy_file'
op|'('
name|'self'
op|','
name|'src'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Copy file to/from remote host.\n\n        Remote address must be specified in format:\n            REM_HOST_IP_ADDRESS:REM_HOST_PATH\n        For example:\n            192.168.1.10:/home/file\n\n        :param src: Source address\n        :param dst: Destination path\n        :param on_execute: Callback method to store pid of process in cache\n        :param on_completion: Callback method to remove pid of process from\n        """'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|SshDriver
dedent|''
dedent|''
name|'class'
name|'SshDriver'
op|'('
name|'RemoteFilesystemDriver'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|create_file
indent|'    '
name|'def'
name|'create_file'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'ssh_execute'
op|'('
name|'host'
op|','
string|"'touch'"
op|','
name|'dst_path'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_file
dedent|''
name|'def'
name|'remove_file'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'ssh_execute'
op|'('
name|'host'
op|','
string|"'rm'"
op|','
name|'dst'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_dir
dedent|''
name|'def'
name|'create_dir'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'ssh_execute'
op|'('
name|'host'
op|','
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'dst_path'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_dir
dedent|''
name|'def'
name|'remove_dir'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'ssh_execute'
op|'('
name|'host'
op|','
string|"'rm'"
op|','
string|"'-rf'"
op|','
name|'dst'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|copy_file
dedent|''
name|'def'
name|'copy_file'
op|'('
name|'self'
op|','
name|'src'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|','
name|'compression'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'scp'"
op|','
name|'src'
op|','
name|'dst'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_tmp_dir
dedent|''
dedent|''
name|'def'
name|'create_tmp_dir'
op|'('
name|'function'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Creates temporary directory for rsync purposes.\n    Removes created directory in the end.\n    """'
newline|'\n'
nl|'\n'
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'function'
op|')'
newline|'\n'
DECL|function|decorated_function
name|'def'
name|'decorated_function'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# Create directory'
nl|'\n'
indent|'        '
name|'tmp_dir_path'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'kwargs'
op|'['
string|"'tmp_dir_path'"
op|']'
op|'='
name|'tmp_dir_path'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'function'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# Remove directory'
nl|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'rm'"
op|','
string|"'-rf'"
op|','
name|'tmp_dir_path'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'decorated_function'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RsyncDriver
dedent|''
name|'class'
name|'RsyncDriver'
op|'('
name|'RemoteFilesystemDriver'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'create_tmp_dir'
newline|'\n'
DECL|member|create_file
name|'def'
name|'create_file'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dir_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'dst_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create target dir inside temporary directory'
nl|'\n'
name|'local_tmp_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'kwargs'
op|'['
string|"'tmp_dir_path'"
op|']'
op|','
nl|'\n'
name|'dir_path'
op|'.'
name|'strip'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'sep'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'local_tmp_dir'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create file in directory'
nl|'\n'
name|'file_name'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'dst_path'
op|')'
op|')'
newline|'\n'
name|'local_tmp_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'local_tmp_dir'
op|','
name|'file_name'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'touch'"
op|','
name|'local_tmp_file'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
name|'RsyncDriver'
op|'.'
name|'_synchronize_object'
op|'('
name|'kwargs'
op|'['
string|"'tmp_dir_path'"
op|']'
op|','
nl|'\n'
name|'host'
op|','
name|'dst_path'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'create_tmp_dir'
newline|'\n'
DECL|member|remove_file
name|'def'
name|'remove_file'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|'# Delete file'
nl|'\n'
indent|'        '
name|'RsyncDriver'
op|'.'
name|'_remove_object'
op|'('
name|'kwargs'
op|'['
string|"'tmp_dir_path'"
op|']'
op|','
name|'host'
op|','
name|'dst'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'create_tmp_dir'
newline|'\n'
DECL|member|create_dir
name|'def'
name|'create_dir'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst_path'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'dir_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'dst_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# Create target dir inside temporary directory'
nl|'\n'
name|'local_tmp_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'kwargs'
op|'['
string|"'tmp_dir_path'"
op|']'
op|','
nl|'\n'
name|'dir_path'
op|'.'
name|'strip'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'sep'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'local_tmp_dir'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
name|'RsyncDriver'
op|'.'
name|'_synchronize_object'
op|'('
name|'kwargs'
op|'['
string|"'tmp_dir_path'"
op|']'
op|','
nl|'\n'
name|'host'
op|','
name|'dst_path'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'create_tmp_dir'
newline|'\n'
DECL|member|remove_dir
name|'def'
name|'remove_dir'
op|'('
name|'self'
op|','
name|'host'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
comment|"# Remove remote directory's content"
nl|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'rsync'"
op|','
string|"'--archive'"
op|','
string|"'--delete-excluded'"
op|','
nl|'\n'
name|'kwargs'
op|'['
string|"'tmp_dir_path'"
op|']'
op|'+'
name|'os'
op|'.'
name|'path'
op|'.'
name|'sep'
op|','
nl|'\n'
string|"'%s:%s'"
op|'%'
op|'('
name|'host'
op|','
name|'dst'
op|')'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete empty directory'
nl|'\n'
name|'RsyncDriver'
op|'.'
name|'_remove_object'
op|'('
name|'kwargs'
op|'['
string|"'tmp_dir_path'"
op|']'
op|','
name|'host'
op|','
name|'dst'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
nl|'\n'
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_remove_object
name|'def'
name|'_remove_object'
op|'('
name|'src'
op|','
name|'host'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes a file or empty directory on a remote host.\n\n        :param src: Empty directory used for rsync purposes\n        :param host: Remote host\n        :param dst: Destination path\n        :param on_execute: Callback method to store pid of process in cache\n        :param on_completion: Callback method to remove pid of process from\n                              cache\n        """'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'rsync'"
op|','
string|"'--archive'"
op|','
string|"'--delete'"
op|','
nl|'\n'
string|"'--include'"
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'dst'
op|')'
op|')'
op|','
nl|'\n'
string|"'--exclude'"
op|','
string|"'*'"
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'src'
op|')'
op|'+'
name|'os'
op|'.'
name|'path'
op|'.'
name|'sep'
op|','
nl|'\n'
string|"'%s:%s'"
op|'%'
op|'('
name|'host'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'dst'
op|')'
op|')'
op|')'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_synchronize_object
name|'def'
name|'_synchronize_object'
op|'('
name|'src'
op|','
name|'host'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Creates a file or empty directory on a remote host.\n\n        :param src: Empty directory used for rsync purposes\n        :param host: Remote host\n        :param dst: Destination path\n        :param on_execute: Callback method to store pid of process in cache\n        :param on_completion: Callback method to remove pid of process from\n                              cache\n        """'
newline|'\n'
nl|'\n'
comment|'# For creating path on the remote host rsync --relative path must'
nl|'\n'
comment|'# be used. With a modern rsync on the sending side (beginning with'
nl|'\n'
comment|'# 2.6.7), you can insert a dot and a slash into the source path,'
nl|'\n'
comment|'# like this:'
nl|'\n'
comment|'#   rsync -avR /foo/./bar/baz.c remote:/tmp/'
nl|'\n'
comment|'# That would create /tmp/bar/baz.c on the remote machine.'
nl|'\n'
comment|'# (Note that the dot must be followed by a slash, so "/foo/."'
nl|'\n'
comment|'# would not be abbreviated.)'
nl|'\n'
name|'relative_tmp_file_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'src'
op|','
string|"'./'"
op|','
nl|'\n'
name|'os'
op|'.'
name|'path'
op|'.'
name|'normpath'
op|'('
name|'dst'
op|')'
op|'.'
name|'strip'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'sep'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Do relative rsync local directory with remote root directory'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'rsync'"
op|','
string|"'--archive'"
op|','
string|"'--relative'"
op|','
string|"'--no-implied-dirs'"
op|','
nl|'\n'
name|'relative_tmp_file_path'
op|','
string|"'%s:%s'"
op|'%'
op|'('
name|'host'
op|','
name|'os'
op|'.'
name|'path'
op|'.'
name|'sep'
op|')'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
nl|'\n'
DECL|member|copy_file
dedent|''
name|'def'
name|'copy_file'
op|'('
name|'self'
op|','
name|'src'
op|','
name|'dst'
op|','
name|'on_execute'
op|','
name|'on_completion'
op|','
name|'compression'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
string|"'rsync'"
op|','
string|"'--sparse'"
op|','
name|'src'
op|','
name|'dst'
op|']'
newline|'\n'
name|'if'
name|'compression'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'append'
op|'('
string|"'--compress'"
op|')'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
nl|'\n'
name|'on_execute'
op|'='
name|'on_execute'
op|','
name|'on_completion'
op|'='
name|'on_completion'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
