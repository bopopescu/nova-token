begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'#    Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'#    Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'#    All Rights Reserved.'
nl|'\n'
comment|'#    Copyright (c) 2010 Citrix Systems, Inc.'
nl|'\n'
comment|'#    Copyright (c) 2011 Piston Cloud Computing, Inc'
nl|'\n'
comment|'#    Copyright (c) 2011 OpenStack LLC'
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
name|'os'
newline|'\n'
name|'import'
name|'random'
newline|'\n'
name|'import'
name|'shutil'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'flags'
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
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
name|'import'
name|'api'
name|'as'
name|'disk'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
name|'import'
name|'images'
newline|'\n'
nl|'\n'
nl|'\n'
name|'qemu_img_opt'
op|'='
DECL|variable|qemu_img_opt
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'qemu_img'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'qemu-img'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'binary to use for qemu-img commands'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'add_option'
op|'('
name|'qemu_img_opt'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|execute
name|'def'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_image
dedent|''
name|'def'
name|'create_image'
op|'('
name|'disk_format'
op|','
name|'path'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a disk image\n\n    :param disk_format: Disk image format (as known by qemu-img)\n    :param path: Desired location of the disk image\n    :param size: Desired size of disk image. May be given as an int or\n                 a string. If given as an int, it will be interpreted\n                 as bytes. If it\'s a string, it should consist of a number\n                 followed by an optional prefix (\'k\' for kilobytes, \'m\'\n                 for megabytes, \'g\' for gigabytes, \'t\' for terabytes). If no\n                 prefix is given, it will be interpreted as bytes.\n    """'
newline|'\n'
name|'execute'
op|'('
name|'FLAGS'
op|'.'
name|'qemu_img'
op|','
string|"'create'"
op|','
string|"'-f'"
op|','
name|'disk_format'
op|','
name|'path'
op|','
name|'size'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|create_cow_image
dedent|''
name|'def'
name|'create_cow_image'
op|'('
name|'backing_file'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create COW image\n\n    Creates a COW image with the given backing file\n\n    :param backing_file: Existing image on which to base the COW image\n    :param path: Desired location of the COW image\n    """'
newline|'\n'
name|'execute'
op|'('
name|'FLAGS'
op|'.'
name|'qemu_img'
op|','
string|"'create'"
op|','
string|"'-f'"
op|','
string|"'qcow2'"
op|','
string|"'-o'"
op|','
nl|'\n'
string|"'cluster_size=2M,backing_file=%s'"
op|'%'
name|'backing_file'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_size
dedent|''
name|'def'
name|'get_disk_size'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the (virtual) size of a disk image\n\n    :param path: Path to the disk image\n    :returns: Size (in bytes) of the given disk image as it would be seen\n              by a virtual machine.\n    """'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'execute'
op|'('
name|'FLAGS'
op|'.'
name|'qemu_img'
op|','
string|"'info'"
op|','
name|'path'
op|')'
newline|'\n'
name|'size'
op|'='
op|'['
name|'i'
op|'.'
name|'split'
op|'('
string|"'('"
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'split'
op|'('
op|')'
op|'['
number|'0'
op|']'
name|'for'
name|'i'
name|'in'
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
nl|'\n'
name|'if'
name|'i'
op|'.'
name|'strip'
op|'('
op|')'
op|'.'
name|'find'
op|'('
string|"'virtual size'"
op|')'
op|'>='
number|'0'
op|']'
newline|'\n'
name|'return'
name|'int'
op|'('
name|'size'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_disk_backing_file
dedent|''
name|'def'
name|'get_disk_backing_file'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the backing file of a disk image\n\n    :param path: Path to the disk image\n    :returns: a path to the image\'s backing store\n    """'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'execute'
op|'('
name|'FLAGS'
op|'.'
name|'qemu_img'
op|','
string|"'info'"
op|','
name|'path'
op|')'
newline|'\n'
name|'backing_file'
op|'='
op|'['
name|'i'
op|'.'
name|'split'
op|'('
string|"'actual path:'"
op|')'
op|'['
number|'1'
op|']'
op|'.'
name|'strip'
op|'('
op|')'
op|'['
op|':'
op|'-'
number|'1'
op|']'
nl|'\n'
name|'for'
name|'i'
name|'in'
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
name|'if'
number|'0'
op|'<='
name|'i'
op|'.'
name|'find'
op|'('
string|"'backing file'"
op|')'
op|']'
newline|'\n'
name|'backing_file'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'backing_file'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'return'
name|'backing_file'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|copy_image
dedent|''
name|'def'
name|'copy_image'
op|'('
name|'src'
op|','
name|'dest'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Copy a disk image\n\n    :param src: Source image\n    :param dest: Destination path\n    """'
newline|'\n'
comment|'# We shell out to cp because that will intelligently copy'
nl|'\n'
comment|'# sparse files.  I.E. holes will not be written to DEST,'
nl|'\n'
comment|'# rather recreated efficiently.  In addition, since'
nl|'\n'
comment|'# coreutils 8.11, holes can be read efficiently too.'
nl|'\n'
name|'execute'
op|'('
string|"'cp'"
op|','
name|'src'
op|','
name|'dest'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkfs
dedent|''
name|'def'
name|'mkfs'
op|'('
name|'fs'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Format a file or block device\n\n    :param fs: Filesystem type (examples include \'swap\', \'ext3\', \'ext4\'\n               \'btrfs\', etc.)\n    :param path: Path to file or block device to format\n    """'
newline|'\n'
name|'if'
name|'fs'
op|'=='
string|"'swap'"
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
string|"'mkswap'"
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'execute'
op|'('
string|"'mkfs'"
op|','
string|"'-t'"
op|','
name|'fs'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ensure_tree
dedent|''
dedent|''
name|'def'
name|'ensure_tree'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Create a directory (and any ancestor directories required)\n\n    :param path: Directory to create\n    """'
newline|'\n'
name|'execute'
op|'('
string|"'mkdir'"
op|','
string|"'-p'"
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|write_to_file
dedent|''
name|'def'
name|'write_to_file'
op|'('
name|'path'
op|','
name|'contents'
op|','
name|'umask'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Write the given contents to a file\n\n    :param path: Destination file\n    :param contents: Desired contents of the file\n    :param umask: Umask to set when creating this file (will be reset)\n    """'
newline|'\n'
name|'if'
name|'umask'
op|':'
newline|'\n'
indent|'        '
name|'saved_umask'
op|'='
name|'os'
op|'.'
name|'umask'
op|'('
name|'umask'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|"'w'"
op|')'
name|'as'
name|'f'
op|':'
newline|'\n'
indent|'            '
name|'f'
op|'.'
name|'write'
op|'('
name|'contents'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'umask'
op|':'
newline|'\n'
indent|'            '
name|'os'
op|'.'
name|'umask'
op|'('
name|'saved_umask'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|chown
dedent|''
dedent|''
dedent|''
name|'def'
name|'chown'
op|'('
name|'path'
op|','
name|'owner'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Change ownership of file or directory\n\n    :param path: File or directory whose ownership to change\n    :param owner: Desired new owner (given as uid or username)\n    """'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'chown'"
op|','
name|'owner'
op|','
name|'path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extract_snapshot
dedent|''
name|'def'
name|'extract_snapshot'
op|'('
name|'disk_path'
op|','
name|'source_fmt'
op|','
name|'snapshot_name'
op|','
name|'out_path'
op|','
name|'dest_fmt'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Extract a named snapshot from a disk image\n\n    :param disk_path: Path to disk image\n    :param snapshot_name: Name of snapshot in disk image\n    :param out_path: Desired path of extracted snapshot\n    """'
newline|'\n'
name|'qemu_img_cmd'
op|'='
op|'('
name|'FLAGS'
op|'.'
name|'qemu_img'
op|','
nl|'\n'
string|"'convert'"
op|','
nl|'\n'
string|"'-f'"
op|','
nl|'\n'
name|'source_fmt'
op|','
nl|'\n'
string|"'-O'"
op|','
nl|'\n'
name|'dest_fmt'
op|','
nl|'\n'
string|"'-s'"
op|','
nl|'\n'
name|'snapshot_name'
op|','
nl|'\n'
name|'disk_path'
op|','
nl|'\n'
name|'out_path'
op|')'
newline|'\n'
name|'execute'
op|'('
op|'*'
name|'qemu_img_cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|load_file
dedent|''
name|'def'
name|'load_file'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Read contents of file\n\n    :param path: File to read\n    """'
newline|'\n'
name|'with'
name|'open'
op|'('
name|'path'
op|','
string|"'r+'"
op|')'
name|'as'
name|'fp'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'fp'
op|'.'
name|'read'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_open
dedent|''
dedent|''
name|'def'
name|'file_open'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Open file\n\n    see built-in file() documentation for more details\n\n    Note: The reason this is kept in a separate module is to easily\n          be able to provide a stub module that doesn\'t alter system\n          state at all (for unit tests)\n    """'
newline|'\n'
name|'return'
name|'file'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|file_delete
dedent|''
name|'def'
name|'file_delete'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Delete (unlink) file\n\n    Note: The reason this is kept in a separate module is to easily\n          be able to provide a stub module that doesn\'t alter system\n          state at all (for unit tests)\n    """'
newline|'\n'
name|'return'
name|'os'
op|'.'
name|'unlink'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_open_port
dedent|''
name|'def'
name|'get_open_port'
op|'('
name|'start_port'
op|','
name|'end_port'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Find an available port\n\n    :param start_port: Start of acceptable port range\n    :param end_port: End of acceptable port range\n    """'
newline|'\n'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'0'
op|','
number|'100'
op|')'
op|':'
comment|"# don't loop forever"
newline|'\n'
indent|'        '
name|'port'
op|'='
name|'random'
op|'.'
name|'randint'
op|'('
name|'start_port'
op|','
name|'end_port'
op|')'
newline|'\n'
comment|'# netcat will exit with 0 only if the port is in use,'
nl|'\n'
comment|'# so a nonzero return value implies it is unused'
nl|'\n'
name|'cmd'
op|'='
string|"'netcat'"
op|','
string|"'0.0.0.0'"
op|','
name|'port'
op|','
string|"'-w'"
op|','
string|"'1'"
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'stdout'
op|','
name|'stderr'
op|'='
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'process_input'
op|'='
string|"''"
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
name|'port'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'Exception'
op|'('
name|'_'
op|'('
string|"'Unable to find an open port'"
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|run_ajaxterm
dedent|''
name|'def'
name|'run_ajaxterm'
op|'('
name|'cmd'
op|','
name|'token'
op|','
name|'port'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Run ajaxterm\n\n    :param cmd: Command to connect to\n    :param token: Token to require for authentication\n    :param port: Port to run on\n    """'
newline|'\n'
name|'cmd'
op|'='
op|'['
string|"'%s/tools/ajaxterm/ajaxterm.py'"
op|'%'
name|'utils'
op|'.'
name|'novadir'
op|'('
op|')'
op|','
nl|'\n'
string|"'--command'"
op|','
name|'cmd'
op|','
string|"'-t'"
op|','
name|'token'
op|','
string|"'-p'"
op|','
name|'port'
op|']'
newline|'\n'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_fs_info
dedent|''
name|'def'
name|'get_fs_info'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get free/used/total space info for a filesystem\n\n    :param path: Any dirent on the filesystem\n    :returns: A dict containing:\n\n             :free: How much space is free (in bytes)\n             :used: How much space is used (in bytes)\n             :total: How big the filesystem is (in bytes)\n    """'
newline|'\n'
name|'hddinfo'
op|'='
name|'os'
op|'.'
name|'statvfs'
op|'('
name|'path'
op|')'
newline|'\n'
name|'total'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
name|'hddinfo'
op|'.'
name|'f_blocks'
newline|'\n'
name|'free'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
name|'hddinfo'
op|'.'
name|'f_bavail'
newline|'\n'
name|'used'
op|'='
name|'hddinfo'
op|'.'
name|'f_frsize'
op|'*'
op|'('
name|'hddinfo'
op|'.'
name|'f_blocks'
op|'-'
name|'hddinfo'
op|'.'
name|'f_bfree'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'total'"
op|':'
name|'total'
op|','
nl|'\n'
string|"'free'"
op|':'
name|'free'
op|','
nl|'\n'
string|"'used'"
op|':'
name|'used'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|fetch_image
dedent|''
name|'def'
name|'fetch_image'
op|'('
name|'context'
op|','
name|'target'
op|','
name|'image_id'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Grab image"""'
newline|'\n'
name|'images'
op|'.'
name|'fetch'
op|'('
name|'context'
op|','
name|'image_id'
op|','
name|'target'
op|','
name|'user_id'
op|','
name|'project_id'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
