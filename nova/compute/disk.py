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
nl|'\n'
string|'"""\nUtility methods to resize, repartition, and modify disk images.\nIncludes injection of SSH PGP keys into authorized_keys file.\n"""'
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
name|'from'
name|'twisted'
op|'.'
name|'internet'
name|'import'
name|'defer'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
nl|'\n'
nl|'\n'
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
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
name|'local_type'
op|'='
string|"'ext2'"
op|','
name|'execute'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Takes a single partition represented by infile and writes a bootable\n    drive image into outfile.\n\n    The first 63 sectors (0-62) of the resulting image is a master boot record.\n    Infile becomes the first primary partition.\n    If local bytes is specified, a second primary partition is created and\n    formatted as ext2.\n\n    In the diagram below, dashes represent drive sectors.\n    +-----+------. . .-------+------. . .------+\n    | 0  a| b               c|d               e|\n    +-----+------. . .-------+------. . .------+\n    | mbr | primary partiton | local partition |\n    +-----+------. . .-------+------. . .------+\n    """'
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
string|'"Input partition size not evenly divisible by"'
nl|'\n'
string|'" sector size: %d / %d"'
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
string|'"Bytes for local storage not evenly divisible"'
nl|'\n'
string|'" by sector size: %d / %d"'
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
name|'yield'
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
nl|'\n'
comment|'# make mbr partition'
nl|'\n'
name|'yield'
name|'execute'
op|'('
string|"'parted --script %s mklabel msdos'"
op|'%'
name|'outfile'
op|')'
newline|'\n'
nl|'\n'
comment|'# make primary partition'
nl|'\n'
name|'yield'
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
comment|'# make local partition'
nl|'\n'
name|'if'
name|'local_bytes'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'yield'
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
comment|'# copy file into partition'
nl|'\n'
dedent|''
name|'yield'
name|'execute'
op|'('
string|"'dd if=%s of=%s bs=%d seek=%d conv=notrunc,fsync'"
nl|'\n'
op|'%'
op|'('
name|'infile'
op|','
name|'outfile'
op|','
name|'sector_size'
op|','
name|'primary_first'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|function|inject_data
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
op|','
name|'execute'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Injects a ssh key and optionally net data into a disk image.\n\n    it will mount the image as a fully partitioned disk and attempt to inject\n    into the specified partition number.\n\n    If partition is not specified it mounts the image as a single partition.\n\n    """'
newline|'\n'
name|'out'
op|','
name|'err'
op|'='
name|'yield'
name|'execute'
op|'('
string|"'sudo losetup -f --show %s'"
op|'%'
name|'image'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'Error'
op|'('
string|"'Could not attach image to loopback: %s'"
op|'%'
name|'err'
op|')'
newline|'\n'
dedent|''
name|'device'
op|'='
name|'out'
op|'.'
name|'strip'
op|'('
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
name|'yield'
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
string|"'Failed to load partition: %s'"
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
dedent|''
name|'out'
op|','
name|'err'
op|'='
name|'yield'
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
name|'yield'
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
string|"'Failed to mount filesystem: %s'"
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
name|'yield'
name|'_inject_key_into_fs'
op|'('
name|'key'
op|','
name|'tmpdir'
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
indent|'                    '
name|'yield'
name|'_inject_net_into_fs'
op|'('
name|'net'
op|','
name|'tmpdir'
op|','
name|'execute'
op|'='
name|'execute'
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
name|'yield'
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
name|'yield'
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
name|'yield'
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
comment|'# remove loopback'
nl|'\n'
indent|'        '
name|'yield'
name|'execute'
op|'('
string|"'sudo losetup -d %s'"
op|'%'
name|'device'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|function|_inject_key_into_fs
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
name|'sshdir'
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
string|"'root'"
op|')'
op|','
string|"'.ssh'"
op|')'
newline|'\n'
name|'yield'
name|'execute'
op|'('
string|"'sudo mkdir -p %s'"
op|'%'
name|'sshdir'
op|')'
comment|"# existing dir doesn't matter"
newline|'\n'
name|'yield'
name|'execute'
op|'('
string|"'sudo chown root %s'"
op|'%'
name|'sshdir'
op|')'
newline|'\n'
name|'yield'
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
name|'yield'
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
dedent|''
op|'@'
name|'defer'
op|'.'
name|'inlineCallbacks'
newline|'\n'
DECL|function|_inject_net_into_fs
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
name|'netfile'
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
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
nl|'\n'
name|'fs'
op|','
string|"'etc'"
op|')'
op|','
string|"'network'"
op|')'
op|','
string|"'interfaces'"
op|')'
newline|'\n'
name|'yield'
name|'execute'
op|'('
string|"'sudo tee %s'"
op|'%'
name|'netfile'
op|','
name|'net'
op|')'
newline|'\n'
nl|'\n'
dedent|''
endmarker|''
end_unit
