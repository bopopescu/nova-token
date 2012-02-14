begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2011, Piston Cloud Computing, Inc.'
nl|'\n'
comment|'#'
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
string|'"""\nUtility methods to resize, repartition, and modify disk images.\n\nIncludes injection of SSH PGP keys into authorized_keys file.\n\n"""'
newline|'\n'
nl|'\n'
name|'import'
name|'json'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'tempfile'
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
name|'import'
name|'log'
name|'as'
name|'logging'
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
name|'guestfs'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
name|'import'
name|'loop'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'disk'
name|'import'
name|'nbd'
newline|'\n'
nl|'\n'
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
DECL|variable|disk_opts
name|'disk_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'injected_network_template'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'utils'
op|'.'
name|'abspath'
op|'('
string|"'virt/interfaces.template'"
op|')'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Template file for injected network'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'ListOpt'
op|'('
string|"'img_handlers'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
string|"'loop'"
op|','
string|"'nbd'"
op|','
string|"'guestfs'"
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Order of methods used to mount disk images'"
op|')'
op|','
nl|'\n'
nl|'\n'
comment|"# NOTE(yamahata): ListOpt won't work because the command may include a"
nl|'\n'
comment|'#                 comma. For example:'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#                 mkfs.ext3 -O dir_index,extent -E stride=8,stripe-width=16'
nl|'\n'
comment|'#                           --label %(fs_label)s %(target)s'
nl|'\n'
comment|'#'
nl|'\n'
comment|'#                 list arguments are comma separated and there is no way to'
nl|'\n'
comment|'#                 escape such commas.'
nl|'\n'
comment|'#'
nl|'\n'
name|'cfg'
op|'.'
name|'MultiStrOpt'
op|'('
string|"'virt_mkfs'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
op|'['
nl|'\n'
string|"'default=mkfs.ext3 -L %(fs_label)s -F %(target)s'"
op|','
nl|'\n'
string|"'linux=mkfs.ext3 -L %(fs_label)s -F %(target)s'"
op|','
nl|'\n'
string|"'windows='"
nl|'\n'
string|"'mkfs.ntfs --fast --label %(fs_label)s %(target)s'"
op|','
nl|'\n'
comment|'# NOTE(yamahata): vfat case'
nl|'\n'
comment|"#'windows=mkfs.vfat -n %(fs_label)s %(target)s',"
nl|'\n'
op|']'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'mkfs commands for ephemeral device. '"
nl|'\n'
string|"'The format is <os_type>=<mkfs command>'"
op|')'
op|','
nl|'\n'
op|']'
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
name|'register_opts'
op|'('
name|'disk_opts'
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_MKFS_COMMAND
name|'_MKFS_COMMAND'
op|'='
op|'{'
op|'}'
newline|'\n'
DECL|variable|_DEFAULT_MKFS_COMMAND
name|'_DEFAULT_MKFS_COMMAND'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
name|'for'
name|'s'
name|'in'
name|'FLAGS'
op|'.'
name|'virt_mkfs'
op|':'
newline|'\n'
comment|"# NOTE(yamahata): mkfs command may includes '=' for its options."
nl|'\n'
comment|"#                 So item.partition('=') doesn't work here"
nl|'\n'
indent|'    '
name|'os_type'
op|','
name|'mkfs_command'
op|'='
name|'s'
op|'.'
name|'split'
op|'('
string|"'='"
op|','
number|'1'
op|')'
newline|'\n'
name|'if'
name|'os_type'
op|':'
newline|'\n'
indent|'        '
name|'_MKFS_COMMAND'
op|'['
name|'os_type'
op|']'
op|'='
name|'mkfs_command'
newline|'\n'
dedent|''
name|'if'
name|'os_type'
op|'=='
string|"'default'"
op|':'
newline|'\n'
DECL|variable|_DEFAULT_MKFS_COMMAND
indent|'        '
name|'_DEFAULT_MKFS_COMMAND'
op|'='
name|'mkfs_command'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mkfs
dedent|''
dedent|''
name|'def'
name|'mkfs'
op|'('
name|'os_type'
op|','
name|'fs_label'
op|','
name|'target'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'mkfs_command'
op|'='
op|'('
name|'_MKFS_COMMAND'
op|'.'
name|'get'
op|'('
name|'os_type'
op|','
name|'_DEFAULT_MKFS_COMMAND'
op|')'
name|'or'
nl|'\n'
string|"''"
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'if'
name|'mkfs_command'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'mkfs_command'
op|'.'
name|'split'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|extend
dedent|''
dedent|''
name|'def'
name|'extend'
op|'('
name|'image'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Increase image to size"""'
newline|'\n'
name|'file_size'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'getsize'
op|'('
name|'image'
op|')'
newline|'\n'
name|'if'
name|'file_size'
op|'>='
name|'size'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'qemu-img'"
op|','
string|"'resize'"
op|','
name|'image'
op|','
name|'size'
op|')'
newline|'\n'
comment|'# NOTE(vish): attempts to resize filesystem'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'e2fsck'"
op|','
string|"'-fp'"
op|','
name|'image'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'resize2fs'"
op|','
name|'image'
op|','
name|'check_exit_code'
op|'='
name|'False'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|bind
dedent|''
name|'def'
name|'bind'
op|'('
name|'src'
op|','
name|'target'
op|','
name|'instance_name'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Bind device to a filesytem"""'
newline|'\n'
name|'if'
name|'src'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'touch'"
op|','
name|'target'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'mount'"
op|','
string|"'-o'"
op|','
string|"'bind'"
op|','
name|'src'
op|','
name|'target'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'s'
op|'='
name|'os'
op|'.'
name|'stat'
op|'('
name|'src'
op|')'
newline|'\n'
name|'cgroup_info'
op|'='
string|'"c %s:%s rwm"'
op|'%'
op|'('
name|'os'
op|'.'
name|'major'
op|'('
name|'s'
op|'.'
name|'st_rdev'
op|')'
op|','
nl|'\n'
name|'os'
op|'.'
name|'minor'
op|'('
name|'s'
op|'.'
name|'st_rdev'
op|')'
op|')'
newline|'\n'
name|'cgroups_path'
op|'='
string|'"/sys/fs/cgroup/devices/sysdefault/libvirt/lxc/%s/devices.allow"'
op|'%'
name|'instance_name'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'echo'"
op|','
string|"'>'"
op|','
name|'cgroup_info'
op|','
name|'cgroups_path'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|unbind
dedent|''
dedent|''
name|'def'
name|'unbind'
op|'('
name|'target'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'target'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'umount'"
op|','
name|'target'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|_DiskImage
dedent|''
dedent|''
name|'class'
name|'_DiskImage'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Provide operations on a disk image file."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'image'
op|','
name|'partition'
op|'='
name|'None'
op|','
name|'use_cow'
op|'='
name|'False'
op|','
name|'mount_dir'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
comment|'# These passed to each mounter'
nl|'\n'
indent|'        '
name|'self'
op|'.'
name|'image'
op|'='
name|'image'
newline|'\n'
name|'self'
op|'.'
name|'partition'
op|'='
name|'partition'
newline|'\n'
name|'self'
op|'.'
name|'mount_dir'
op|'='
name|'mount_dir'
newline|'\n'
nl|'\n'
comment|'# Internal'
nl|'\n'
name|'self'
op|'.'
name|'_mkdir'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'_mounter'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'_errors'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|"# As a performance tweak, don't bother trying to"
nl|'\n'
comment|'# directly loopback mount a cow image.'
nl|'\n'
name|'self'
op|'.'
name|'handlers'
op|'='
name|'FLAGS'
op|'.'
name|'img_handlers'
op|'['
op|':'
op|']'
newline|'\n'
name|'if'
name|'use_cow'
name|'and'
string|"'loop'"
name|'in'
name|'self'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handlers'
op|'.'
name|'remove'
op|'('
string|"'loop'"
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'no capable image handler configured'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'property'
newline|'\n'
DECL|member|errors
name|'def'
name|'errors'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return the collated errors from all operations."""'
newline|'\n'
name|'return'
string|"'\\n--\\n'"
op|'.'
name|'join'
op|'('
op|'['
string|"''"
op|']'
op|'+'
name|'self'
op|'.'
name|'_errors'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_handler_class
name|'def'
name|'_handler_class'
op|'('
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Look up the appropriate class to use based on MODE."""'
newline|'\n'
name|'for'
name|'cls'
name|'in'
op|'('
name|'loop'
op|'.'
name|'Mount'
op|','
name|'nbd'
op|'.'
name|'Mount'
op|','
name|'guestfs'
op|'.'
name|'Mount'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'cls'
op|'.'
name|'mode'
op|'=='
name|'mode'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'cls'
newline|'\n'
dedent|''
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|'"unknown disk image handler: %s"'
op|'%'
name|'mode'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|mount
dedent|''
name|'def'
name|'mount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Mount a disk image, using the object attributes.\n\n        The first supported means provided by the mount classes is used.\n\n        True, or False is returned and the \'errors\' attribute\n        contains any diagnostics.\n        """'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'_mounter'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'image already mounted'"
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'self'
op|'.'
name|'mount_dir'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mount_dir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_mkdir'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'h'
name|'in'
name|'self'
op|'.'
name|'handlers'
op|':'
newline|'\n'
indent|'                '
name|'mounter_cls'
op|'='
name|'self'
op|'.'
name|'_handler_class'
op|'('
name|'h'
op|')'
newline|'\n'
name|'mounter'
op|'='
name|'mounter_cls'
op|'('
name|'image'
op|'='
name|'self'
op|'.'
name|'image'
op|','
nl|'\n'
name|'partition'
op|'='
name|'self'
op|'.'
name|'partition'
op|','
nl|'\n'
name|'mount_dir'
op|'='
name|'self'
op|'.'
name|'mount_dir'
op|')'
newline|'\n'
name|'if'
name|'mounter'
op|'.'
name|'do_mount'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'_mounter'
op|'='
name|'mounter'
newline|'\n'
name|'break'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'mounter'
op|'.'
name|'error'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_errors'
op|'.'
name|'append'
op|'('
name|'mounter'
op|'.'
name|'error'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_mounter'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'umount'
op|'('
op|')'
comment|'# rmdir'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'bool'
op|'('
name|'self'
op|'.'
name|'_mounter'
op|')'
newline|'\n'
nl|'\n'
DECL|member|umount
dedent|''
name|'def'
name|'umount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unmount a disk image from the file system."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_mounter'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'_mounter'
op|'.'
name|'do_umount'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'self'
op|'.'
name|'_mkdir'
op|':'
newline|'\n'
indent|'                '
name|'os'
op|'.'
name|'rmdir'
op|'('
name|'self'
op|'.'
name|'mount_dir'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
comment|'# Public module functions'
nl|'\n'
nl|'\n'
DECL|function|inject_data
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'inject_data'
op|'('
name|'image'
op|','
name|'key'
op|'='
name|'None'
op|','
name|'net'
op|'='
name|'None'
op|','
name|'metadata'
op|'='
name|'None'
op|','
nl|'\n'
name|'partition'
op|'='
name|'None'
op|','
name|'use_cow'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Injects a ssh key and optionally net data into a disk image.\n\n    it will mount the image as a fully partitioned disk and attempt to inject\n    into the specified partition number.\n\n    If partition is not specified it mounts the image as a single partition.\n\n    """'
newline|'\n'
name|'img'
op|'='
name|'_DiskImage'
op|'('
name|'image'
op|'='
name|'image'
op|','
name|'partition'
op|'='
name|'partition'
op|','
name|'use_cow'
op|'='
name|'use_cow'
op|')'
newline|'\n'
name|'if'
name|'img'
op|'.'
name|'mount'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'inject_data_into_fs'
op|'('
name|'img'
op|'.'
name|'mount_dir'
op|','
name|'key'
op|','
name|'net'
op|','
name|'metadata'
op|','
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'img'
op|'.'
name|'umount'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'img'
op|'.'
name|'errors'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|inject_files
dedent|''
dedent|''
name|'def'
name|'inject_files'
op|'('
name|'image'
op|','
name|'files'
op|','
name|'partition'
op|'='
name|'None'
op|','
name|'use_cow'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Injects arbitrary files into a disk image"""'
newline|'\n'
name|'img'
op|'='
name|'_DiskImage'
op|'('
name|'image'
op|'='
name|'image'
op|','
name|'partition'
op|'='
name|'partition'
op|','
name|'use_cow'
op|'='
name|'use_cow'
op|')'
newline|'\n'
name|'if'
name|'img'
op|'.'
name|'mount'
op|'('
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'for'
op|'('
name|'path'
op|','
name|'contents'
op|')'
name|'in'
name|'files'
op|':'
newline|'\n'
indent|'                '
name|'_inject_file_into_fs'
op|'('
name|'img'
op|'.'
name|'mount_dir'
op|','
name|'path'
op|','
name|'contents'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'img'
op|'.'
name|'umount'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'img'
op|'.'
name|'errors'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|setup_container
dedent|''
dedent|''
name|'def'
name|'setup_container'
op|'('
name|'image'
op|','
name|'container_dir'
op|'='
name|'None'
op|','
name|'use_cow'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Setup the LXC container.\n\n    It will mount the loopback image to the container directory in order\n    to create the root filesystem for the container.\n\n    LXC does not support qcow2 images yet.\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'img'
op|'='
name|'_DiskImage'
op|'('
name|'image'
op|'='
name|'image'
op|','
name|'use_cow'
op|'='
name|'use_cow'
op|','
name|'mount_dir'
op|'='
name|'container_dir'
op|')'
newline|'\n'
name|'if'
name|'img'
op|'.'
name|'mount'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'img'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'img'
op|'.'
name|'errors'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exn'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to mount filesystem: %s'"
op|')'
op|','
name|'exn'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|destroy_container
dedent|''
dedent|''
name|'def'
name|'destroy_container'
op|'('
name|'img'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Destroy the container once it terminates.\n\n    It will umount the container that is mounted,\n    and delete any  linked devices.\n\n    LXC does not support qcow2 images yet.\n    """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'img'
op|':'
newline|'\n'
indent|'            '
name|'img'
op|'.'
name|'umount'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'Exception'
op|','
name|'exn'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to remove container: %s'"
op|')'
op|','
name|'exn'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|inject_data_into_fs
dedent|''
dedent|''
name|'def'
name|'inject_data_into_fs'
op|'('
name|'fs'
op|','
name|'key'
op|','
name|'net'
op|','
name|'metadata'
op|','
name|'execute'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Injects data into a filesystem already mounted by the caller.\n    Virt connections can call this directly if they mount their fs\n    in a different way to inject_data\n    """'
newline|'\n'
name|'if'
name|'key'
op|':'
newline|'\n'
indent|'        '
name|'_inject_key_into_fs'
op|'('
name|'key'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'net'
op|':'
newline|'\n'
indent|'        '
name|'_inject_net_into_fs'
op|'('
name|'net'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'metadata'
op|':'
newline|'\n'
indent|'        '
name|'_inject_metadata_into_fs'
op|'('
name|'metadata'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'execute'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_inject_file_into_fs
dedent|''
dedent|''
name|'def'
name|'_inject_file_into_fs'
op|'('
name|'fs'
op|','
name|'path'
op|','
name|'contents'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'absolute_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fs'
op|','
name|'path'
op|'.'
name|'lstrip'
op|'('
string|"'/'"
op|')'
op|')'
newline|'\n'
name|'parent_dir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'dirname'
op|'('
name|'absolute_path'
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
name|'parent_dir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tee'"
op|','
name|'absolute_path'
op|','
name|'process_input'
op|'='
name|'contents'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_inject_metadata_into_fs
dedent|''
name|'def'
name|'_inject_metadata_into_fs'
op|'('
name|'metadata'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'metadata_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fs'
op|','
string|'"meta.js"'
op|')'
newline|'\n'
name|'metadata'
op|'='
name|'dict'
op|'('
op|'['
op|'('
name|'m'
op|'.'
name|'key'
op|','
name|'m'
op|'.'
name|'value'
op|')'
name|'for'
name|'m'
name|'in'
name|'metadata'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tee'"
op|','
name|'metadata_path'
op|','
nl|'\n'
name|'process_input'
op|'='
name|'json'
op|'.'
name|'dumps'
op|'('
name|'metadata'
op|')'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_inject_key_into_fs
dedent|''
name|'def'
name|'_inject_key_into_fs'
op|'('
name|'key'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Add the given public ssh key to root\'s authorized_keys.\n\n    key is an ssh key string.\n    fs is the path to the base of the filesystem into which to inject the key.\n    """'
newline|'\n'
name|'sshdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fs'
op|','
string|"'root'"
op|','
string|"'.ssh'"
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
name|'sshdir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'chown'"
op|','
string|"'root'"
op|','
name|'sshdir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'chmod'"
op|','
string|"'700'"
op|','
name|'sshdir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'keyfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'sshdir'
op|','
string|"'authorized_keys'"
op|')'
newline|'\n'
name|'key_data'
op|'='
op|'['
nl|'\n'
string|"'\\n'"
op|','
nl|'\n'
string|"'# The following ssh key was injected by Nova'"
op|','
nl|'\n'
string|"'\\n'"
op|','
nl|'\n'
name|'key'
op|'.'
name|'strip'
op|'('
op|')'
op|','
nl|'\n'
string|"'\\n'"
op|','
nl|'\n'
op|']'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tee'"
op|','
string|"'-a'"
op|','
name|'keyfile'
op|','
nl|'\n'
name|'process_input'
op|'='
string|"''"
op|'.'
name|'join'
op|'('
name|'key_data'
op|')'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_inject_net_into_fs
dedent|''
name|'def'
name|'_inject_net_into_fs'
op|'('
name|'net'
op|','
name|'fs'
op|','
name|'execute'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Inject /etc/network/interfaces into the filesystem rooted at fs.\n\n    net is the contents of /etc/network/interfaces.\n    """'
newline|'\n'
name|'netdir'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'fs'
op|','
string|"'etc'"
op|')'
op|','
string|"'network'"
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
name|'netdir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'chown'"
op|','
string|"'root:root'"
op|','
name|'netdir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'chmod'"
op|','
number|'755'
op|','
name|'netdir'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'netfile'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
name|'netdir'
op|','
string|"'interfaces'"
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tee'"
op|','
name|'netfile'
op|','
name|'process_input'
op|'='
name|'net'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
