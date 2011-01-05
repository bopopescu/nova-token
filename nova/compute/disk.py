begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright 2010 United States Government as represented by the'
nl|'\n'
comment|'# Administrator of the National Aeronautics and Space Administration.'
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
name|'logging'
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
name|'utils'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'minimum_root_size'"
op|','
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'10'
op|','
nl|'\n'
string|"'minimum size in bytes of root partition'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DEFINE_integer'
op|'('
string|"'block_size'"
op|','
number|'1024'
op|'*'
number|'1024'
op|'*'
number|'256'
op|','
nl|'\n'
string|"'block_size to use for dd'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|partition
name|'def'
name|'partition'
op|'('
name|'infile'
op|','
name|'outfile'
op|','
name|'local_bytes'
op|'='
number|'0'
op|','
name|'resize'
op|'='
name|'True'
op|','
name|'local_type'
op|'='
string|"'ext2'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""\n    Turns a partition (infile) into a bootable drive image (outfile).\n\n    The first 63 sectors (0-62) of the resulting image is a master boot record.\n    Infile becomes the first primary partition.\n    If local bytes is specified, a second primary partition is created and\n    formatted as ext2.\n\n    ::\n\n        In the diagram below, dashes represent drive sectors.\n        +-----+------. . .-------+------. . .------+\n        | 0  a| b               c|d               e|\n        +-----+------. . .-------+------. . .------+\n        | mbr | primary partiton | local partition |\n        +-----+------. . .-------+------. . .------+\n\n    """'
newline|'\n'
name|'sector_size'
op|'='
number|'512'
newline|'\n'
name|'file_size'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'getsize'
op|'('
name|'infile'
op|')'
newline|'\n'
name|'if'
name|'resize'
name|'and'
name|'file_size'
op|'<'
name|'FLAGS'
op|'.'
name|'minimum_root_size'
op|':'
newline|'\n'
indent|'        '
name|'last_sector'
op|'='
name|'FLAGS'
op|'.'
name|'minimum_root_size'
op|'/'
name|'sector_size'
op|'-'
number|'1'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'dd if=/dev/zero of=%s count=1 seek=%d bs=%d'"
nl|'\n'
op|'%'
op|'('
name|'infile'
op|','
name|'last_sector'
op|','
name|'sector_size'
op|')'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'e2fsck -fp %s'"
op|'%'
name|'infile'
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
string|"'resize2fs %s'"
op|'%'
name|'infile'
op|')'
newline|'\n'
name|'file_size'
op|'='
name|'FLAGS'
op|'.'
name|'minimum_root_size'
newline|'\n'
dedent|''
name|'elif'
name|'file_size'
op|'%'
name|'sector_size'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Input partition size not evenly divisible by"'
nl|'\n'
string|'" sector size: %d / %d"'
op|')'
op|','
name|'file_size'
op|','
name|'sector_size'
op|')'
newline|'\n'
dedent|''
name|'primary_sectors'
op|'='
name|'file_size'
op|'/'
name|'sector_size'
newline|'\n'
name|'if'
name|'local_bytes'
op|'%'
name|'sector_size'
op|'!='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'logging'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Bytes for local storage not evenly divisible"'
nl|'\n'
string|'" by sector size: %d / %d"'
op|')'
op|','
name|'local_bytes'
op|','
name|'sector_size'
op|')'
newline|'\n'
dedent|''
name|'local_sectors'
op|'='
name|'local_bytes'
op|'/'
name|'sector_size'
newline|'\n'
nl|'\n'
name|'mbr_last'
op|'='
number|'62'
comment|'# a'
newline|'\n'
name|'primary_first'
op|'='
name|'mbr_last'
op|'+'
number|'1'
comment|'# b'
newline|'\n'
name|'primary_last'
op|'='
name|'primary_first'
op|'+'
name|'primary_sectors'
op|'-'
number|'1'
comment|'# c'
newline|'\n'
name|'local_first'
op|'='
name|'primary_last'
op|'+'
number|'1'
comment|'# d'
newline|'\n'
name|'local_last'
op|'='
name|'local_first'
op|'+'
name|'local_sectors'
op|'-'
number|'1'
comment|'# e'
newline|'\n'
name|'last_sector'
op|'='
name|'local_last'
comment|'# e'
newline|'\n'
nl|'\n'
comment|'# create an empty file'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'dd if=/dev/zero of=%s count=1 seek=%d bs=%d'"
nl|'\n'
op|'%'
op|'('
name|'outfile'
op|','
name|'mbr_last'
op|','
name|'sector_size'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# make mbr partition'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'parted --script %s mklabel msdos'"
op|'%'
name|'outfile'
op|')'
newline|'\n'
nl|'\n'
comment|'# append primary file'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'dd if=%s of=%s bs=%s conv=notrunc,fsync oflag=append'"
nl|'\n'
op|'%'
op|'('
name|'infile'
op|','
name|'outfile'
op|','
name|'FLAGS'
op|'.'
name|'block_size'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# make primary partition'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'parted --script %s mkpart primary %ds %ds'"
nl|'\n'
op|'%'
op|'('
name|'outfile'
op|','
name|'primary_first'
op|','
name|'primary_last'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'local_bytes'
op|'>'
number|'0'
op|':'
newline|'\n'
comment|'# make the file bigger'
nl|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'dd if=/dev/zero of=%s count=1 seek=%d bs=%d'"
nl|'\n'
op|'%'
op|'('
name|'outfile'
op|','
name|'last_sector'
op|','
name|'sector_size'
op|')'
op|')'
newline|'\n'
comment|'# make and format local partition'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'parted --script %s mkpartfs primary %s %ds %ds'"
nl|'\n'
op|'%'
op|'('
name|'outfile'
op|','
name|'local_type'
op|','
name|'local_first'
op|','
name|'local_last'
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
name|'return'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'truncate -s size %s'"
op|'%'
op|'('
name|'image'
op|','
op|')'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|inject_data
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
name|'partition'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Injects a ssh key and optionally net data into a disk image.\n\n    it will mount the image as a fully partitioned disk and attempt to inject\n    into the specified partition number.\n\n    If partition is not specified it mounts the image as a single partition.\n\n    """'
newline|'\n'
name|'device'
op|'='
name|'_link_device'
op|'('
name|'image'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'partition'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# create partition'
nl|'\n'
indent|'            '
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo kpartx -a %s'"
op|'%'
name|'device'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Failed to load partition: %s'"
op|')'
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'mapped_device'
op|'='
string|"'/dev/mapper/%sp%s'"
op|'%'
op|'('
name|'device'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|','
nl|'\n'
name|'partition'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'mapped_device'
op|'='
name|'device'
newline|'\n'
nl|'\n'
comment|"# We can only loopback mount raw images. If the device isn't there,"
nl|'\n'
comment|"# it's normally because it's a .vmdk or a .vdi etc"
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'mapped_device'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|"'Mapped device was not found (we can'"
nl|'\n'
string|"' only inject raw disk images): %s'"
op|'%'
nl|'\n'
name|'mapped_device'
op|')'
newline|'\n'
nl|'\n'
comment|"# Configure ext2fs so that it doesn't auto-check every N boots"
nl|'\n'
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo tune2fs -c 0 -i 0 %s'"
op|'%'
name|'mapped_device'
op|')'
newline|'\n'
nl|'\n'
name|'tmpdir'
op|'='
name|'tempfile'
op|'.'
name|'mkdtemp'
op|'('
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
comment|'# mount loopback to dir'
nl|'\n'
indent|'            '
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
nl|'\n'
string|"'sudo mount %s %s'"
op|'%'
op|'('
name|'mapped_device'
op|','
name|'tmpdir'
op|')'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'Failed to mount filesystem: %s'"
op|')'
nl|'\n'
op|'%'
name|'err'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'key'
op|':'
newline|'\n'
comment|'# inject key file'
nl|'\n'
indent|'                    '
name|'_inject_key_into_fs'
op|'('
name|'key'
op|','
name|'tmpdir'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'net'
op|':'
newline|'\n'
indent|'                    '
name|'_inject_net_into_fs'
op|'('
name|'net'
op|','
name|'tmpdir'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# unmount device'
nl|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo umount %s'"
op|'%'
name|'mapped_device'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# remove temporary directory'
nl|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'rmdir %s'"
op|'%'
name|'tmpdir'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'partition'
name|'is'
name|'None'
op|':'
newline|'\n'
comment|'# remove partitions'
nl|'\n'
indent|'                '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo kpartx -d %s'"
op|'%'
name|'device'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'        '
name|'_unlink_device'
op|'('
name|'image'
op|','
name|'device'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_link_device
dedent|''
dedent|''
name|'def'
name|'_link_device'
op|'('
name|'image'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'use_cow_images'
op|':'
newline|'\n'
indent|'        '
name|'device'
op|'='
name|'_allocate_device'
op|'('
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo qemu-nbd --connect=%s %s'"
op|'%'
op|'('
name|'device'
op|','
name|'image'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo losetup --find --show %s'"
op|'%'
name|'image'
op|')'
newline|'\n'
name|'if'
name|'err'
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
string|"'Could not attach image to loopback: %s'"
op|')'
nl|'\n'
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'out'
op|'.'
name|'strip'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_unlink_device
dedent|''
dedent|''
name|'def'
name|'_unlink_device'
op|'('
name|'image'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'FLAGS'
op|'.'
name|'use_cow_images'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo qemu-nbd --disconnect %s'"
op|'%'
name|'image'
op|')'
newline|'\n'
name|'_free_device'
op|'('
name|'device'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo losetup --detach %s'"
op|'%'
name|'device'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_DEVICES
dedent|''
dedent|''
name|'_DEVICES'
op|'='
op|'['
string|"'/dev/nbd%s'"
op|'%'
name|'i'
name|'for'
name|'i'
name|'in'
name|'xrange'
op|'('
number|'16'
op|')'
op|']'
newline|'\n'
nl|'\n'
DECL|function|_allocate_device
name|'def'
name|'_allocate_device'
op|'('
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): This assumes no other processes are using nbd devices.'
nl|'\n'
comment|'#             It will race cause a race condition if multiple'
nl|'\n'
comment|'#             workers are running on a given machine.'
nl|'\n'
indent|'    '
name|'if'
name|'not'
name|'_DEVICES'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
name|'_'
op|'('
string|"'No free nbd devices'"
op|')'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'_DEVICES'
op|'.'
name|'pop'
op|'('
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_free_device
dedent|''
name|'def'
name|'_free_device'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'_DEVICES'
op|'.'
name|'append'
op|'('
name|'device'
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
string|"'sudo mkdir -p %s'"
op|'%'
name|'sshdir'
op|')'
comment|"# existing dir doesn't matter"
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo chown root %s'"
op|'%'
name|'sshdir'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo chmod 700 %s'"
op|'%'
name|'sshdir'
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
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo tee -a %s'"
op|'%'
name|'keyfile'
op|','
string|"'\\n'"
op|'+'
name|'key'
op|'.'
name|'strip'
op|'('
op|')'
op|'+'
string|"'\\n'"
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
string|"'sudo mkdir -p %s'"
op|'%'
name|'netdir'
op|')'
comment|"# existing dir doesn't matter"
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo chown root:root %s'"
op|'%'
name|'netdir'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'sudo chmod 755 %s'"
op|'%'
name|'netdir'
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
string|"'sudo tee %s'"
op|'%'
name|'netfile'
op|','
name|'net'
op|')'
newline|'\n'
dedent|''
endmarker|''
end_unit
