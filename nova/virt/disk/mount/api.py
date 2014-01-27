begin_unit
comment|'# Copyright 2011 Red Hat, Inc.'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Licensed under the Apache License, Version 2.0 (the "License"); you may'
nl|'\n'
comment|'# not use this file except in compliance with the License. You may obtain'
nl|'\n'
comment|'# a copy of the License at'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# http://www.apache.org/licenses/LICENSE-2.0'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Unless required by applicable law or agreed to in writing, software'
nl|'\n'
comment|'# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT'
nl|'\n'
comment|'# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the'
nl|'\n'
comment|'# License for the specific language governing permissions and limitations'
nl|'\n'
comment|'# under the License.'
nl|'\n'
string|'"""Support for mounting virtual image files."""'
newline|'\n'
nl|'\n'
name|'import'
name|'os'
newline|'\n'
name|'import'
name|'time'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
op|'.'
name|'gettextutils'
name|'import'
name|'_'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'importutils'
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
DECL|variable|MAX_DEVICE_WAIT
name|'MAX_DEVICE_WAIT'
op|'='
number|'30'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Mount
name|'class'
name|'Mount'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Standard mounting operations, that can be overridden by subclasses.\n\n    The basic device operations provided are get, map and mount,\n    to be called in that order.\n    """'
newline|'\n'
nl|'\n'
DECL|variable|mode
name|'mode'
op|'='
name|'None'
comment|'# to be overridden in subclasses'
newline|'\n'
nl|'\n'
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|instance_for_format
name|'def'
name|'instance_for_format'
op|'('
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|','
name|'imgfmt'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Instance for format imgfile=%(imgfile)s "'
nl|'\n'
string|'"mountdir=%(mountdir)s partition=%(partition)s "'
nl|'\n'
string|'"imgfmt=%(imgfmt)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'imgfile'"
op|':'
name|'imgfile'
op|','
string|"'mountdir'"
op|':'
name|'mountdir'
op|','
nl|'\n'
string|"'partition'"
op|':'
name|'partition'
op|','
string|"'imgfmt'"
op|':'
name|'imgfmt'
op|'}'
op|')'
newline|'\n'
name|'if'
name|'imgfmt'
op|'=='
string|'"raw"'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Using LoopMount"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
string|'"nova.virt.disk.mount.loop.LoopMount"'
op|','
nl|'\n'
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Using NbdMount"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
string|'"nova.virt.disk.mount.nbd.NbdMount"'
op|','
nl|'\n'
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|instance_for_device
name|'def'
name|'instance_for_device'
op|'('
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|','
name|'device'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Instance for device imgfile=%(imgfile)s "'
nl|'\n'
string|'"mountdir=%(mountdir)s partition=%(partition)s "'
nl|'\n'
string|'"device=%(device)s"'
op|')'
op|','
nl|'\n'
op|'{'
string|"'imgfile'"
op|':'
name|'imgfile'
op|','
string|"'mountdir'"
op|':'
name|'mountdir'
op|','
nl|'\n'
string|"'partition'"
op|':'
name|'partition'
op|','
string|"'device'"
op|':'
name|'device'
op|'}'
op|')'
newline|'\n'
name|'if'
string|'"loop"'
name|'in'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Using LoopMount"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
string|'"nova.virt.disk.mount.loop.LoopMount"'
op|','
nl|'\n'
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|','
name|'device'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Using NbdMount"'
op|')'
op|')'
newline|'\n'
name|'return'
name|'importutils'
op|'.'
name|'import_object'
op|'('
nl|'\n'
string|'"nova.virt.disk.mount.nbd.NbdMount"'
op|','
nl|'\n'
name|'imgfile'
op|','
name|'mountdir'
op|','
name|'partition'
op|','
name|'device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__init__
dedent|''
dedent|''
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'image'
op|','
name|'mount_dir'
op|','
name|'partition'
op|'='
name|'None'
op|','
name|'device'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
comment|'# Input'
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
comment|'# Output'
nl|'\n'
name|'self'
op|'.'
name|'error'
op|'='
string|'""'
newline|'\n'
nl|'\n'
comment|'# Internal'
nl|'\n'
name|'self'
op|'.'
name|'linked'
op|'='
name|'self'
op|'.'
name|'mapped'
op|'='
name|'self'
op|'.'
name|'mounted'
op|'='
name|'self'
op|'.'
name|'automapped'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'self'
op|'.'
name|'mapped_device'
op|'='
name|'device'
newline|'\n'
nl|'\n'
comment|'# Reset to mounted dir if possible'
nl|'\n'
name|'self'
op|'.'
name|'reset_dev'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|reset_dev
dedent|''
name|'def'
name|'reset_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Reset device paths to allow unmounting."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'linked'
op|'='
name|'self'
op|'.'
name|'mapped'
op|'='
name|'self'
op|'.'
name|'mounted'
op|'='
name|'True'
newline|'\n'
nl|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'device'
newline|'\n'
name|'if'
name|'os'
op|'.'
name|'path'
op|'.'
name|'isabs'
op|'('
name|'device'
op|')'
name|'and'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'device'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'device'
op|'.'
name|'startswith'
op|'('
string|"'/dev/mapper/'"
op|')'
op|':'
newline|'\n'
indent|'                '
name|'device'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'device'
op|')'
newline|'\n'
name|'device'
op|','
name|'self'
op|'.'
name|'partition'
op|'='
name|'device'
op|'.'
name|'rsplit'
op|'('
string|"'p'"
op|','
number|'1'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'join'
op|'('
string|"'/dev'"
op|','
name|'device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_dev
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Make the image available as a block device in the file system."""'
newline|'\n'
name|'self'
op|'.'
name|'device'
op|'='
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'linked'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_get_dev_retry_helper
dedent|''
name|'def'
name|'_get_dev_retry_helper'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Some implementations need to retry their get_dev."""'
newline|'\n'
comment|'# NOTE(mikal): This method helps implement retries. The implementation'
nl|'\n'
comment|'# simply calls _get_dev_retry_helper from their get_dev, and implements'
nl|'\n'
comment|'# _inner_get_dev with their device acquisition logic. The NBD'
nl|'\n'
comment|'# implementation has an example.'
nl|'\n'
name|'start_time'
op|'='
name|'time'
op|'.'
name|'time'
op|'('
op|')'
newline|'\n'
name|'device'
op|'='
name|'self'
op|'.'
name|'_inner_get_dev'
op|'('
op|')'
newline|'\n'
name|'while'
name|'not'
name|'device'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|"'Device allocation failed. Will retry in 2 seconds.'"
op|')'
op|')'
newline|'\n'
name|'time'
op|'.'
name|'sleep'
op|'('
number|'2'
op|')'
newline|'\n'
name|'if'
name|'time'
op|'.'
name|'time'
op|'('
op|')'
op|'-'
name|'start_time'
op|'>'
name|'MAX_DEVICE_WAIT'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Device allocation failed after repeated retries.'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'device'
op|'='
name|'self'
op|'.'
name|'_inner_get_dev'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|_inner_get_dev
dedent|''
name|'def'
name|'_inner_get_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'NotImplementedError'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|unget_dev
dedent|''
name|'def'
name|'unget_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Release the block device from the file system namespace."""'
newline|'\n'
name|'self'
op|'.'
name|'linked'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|map_dev
dedent|''
name|'def'
name|'map_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Map partitions of the device to the file system namespace."""'
newline|'\n'
name|'assert'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'self'
op|'.'
name|'device'
op|')'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Map dev %s"'
op|')'
op|','
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'automapped_path'
op|'='
string|"'/dev/%sp%s'"
op|'%'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'self'
op|'.'
name|'device'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'partition'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'partition'
op|'=='
op|'-'
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'error'
op|'='
name|'_'
op|'('
string|"'partition search unsupported with %s'"
op|')'
op|'%'
name|'self'
op|'.'
name|'mode'
newline|'\n'
dedent|''
name|'elif'
name|'self'
op|'.'
name|'partition'
name|'and'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'automapped_path'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'map_path'
op|'='
string|"'/dev/mapper/%sp%s'"
op|'%'
op|'('
name|'os'
op|'.'
name|'path'
op|'.'
name|'basename'
op|'('
name|'self'
op|'.'
name|'device'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'partition'
op|')'
newline|'\n'
name|'assert'
op|'('
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'map_path'
op|')'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note kpartx can output warnings to stderr and succeed'
nl|'\n'
comment|'# Also it can output failures to stderr and "succeed"'
nl|'\n'
comment|'# So we just go on the existence of the mapped device'
nl|'\n'
name|'_out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'trycmd'
op|'('
string|"'kpartx'"
op|','
string|"'-a'"
op|','
name|'self'
op|'.'
name|'device'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'discard_warnings'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Note kpartx does nothing when presented with a raw image,'
nl|'\n'
comment|'# so given we only use it when we expect a partitioned image, fail'
nl|'\n'
name|'if'
name|'not'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'map_path'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'err'
op|':'
newline|'\n'
indent|'                    '
name|'err'
op|'='
name|'_'
op|'('
string|"'partition %s not found'"
op|')'
op|'%'
name|'self'
op|'.'
name|'partition'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'error'
op|'='
name|'_'
op|'('
string|"'Failed to map partitions: %s'"
op|')'
op|'%'
name|'err'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'mapped_device'
op|'='
name|'map_path'
newline|'\n'
name|'self'
op|'.'
name|'mapped'
op|'='
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'elif'
name|'self'
op|'.'
name|'partition'
name|'and'
name|'os'
op|'.'
name|'path'
op|'.'
name|'exists'
op|'('
name|'automapped_path'
op|')'
op|':'
newline|'\n'
comment|"# Note auto mapping can be enabled with the 'max_part' option"
nl|'\n'
comment|'# to the nbd or loop kernel modules. Beware of possible races'
nl|'\n'
comment|'# in the partition scanning for _loop_ devices though'
nl|'\n'
comment|'# (details in bug 1024586), which are currently uncatered for.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'mapped_device'
op|'='
name|'automapped_path'
newline|'\n'
name|'self'
op|'.'
name|'mapped'
op|'='
name|'True'
newline|'\n'
name|'self'
op|'.'
name|'automapped'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'mapped_device'
op|'='
name|'self'
op|'.'
name|'device'
newline|'\n'
name|'self'
op|'.'
name|'mapped'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'mapped'
newline|'\n'
nl|'\n'
DECL|member|unmap_dev
dedent|''
name|'def'
name|'unmap_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Remove partitions of the device from the file system namespace."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'mapped'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Unmap dev %s"'
op|')'
op|','
name|'self'
op|'.'
name|'device'
op|')'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'partition'
name|'and'
name|'not'
name|'self'
op|'.'
name|'automapped'
op|':'
newline|'\n'
indent|'            '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'kpartx'"
op|','
string|"'-d'"
op|','
name|'self'
op|'.'
name|'device'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'mapped'
op|'='
name|'False'
newline|'\n'
name|'self'
op|'.'
name|'automapped'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|mnt_dev
dedent|''
name|'def'
name|'mnt_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Mount the device into the file system."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Mount %(dev)s on %(dir)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'dev'"
op|':'
name|'self'
op|'.'
name|'mapped_device'
op|','
string|"'dir'"
op|':'
name|'self'
op|'.'
name|'mount_dir'
op|'}'
op|')'
newline|'\n'
name|'_out'
op|','
name|'err'
op|'='
name|'utils'
op|'.'
name|'trycmd'
op|'('
string|"'mount'"
op|','
name|'self'
op|'.'
name|'mapped_device'
op|','
name|'self'
op|'.'
name|'mount_dir'
op|','
nl|'\n'
name|'discard_warnings'
op|'='
name|'True'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'if'
name|'err'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'error'
op|'='
name|'_'
op|'('
string|"'Failed to mount filesystem: %s'"
op|')'
op|'%'
name|'err'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'self'
op|'.'
name|'error'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'mounted'
op|'='
name|'True'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
DECL|member|unmnt_dev
dedent|''
name|'def'
name|'unmnt_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Unmount the device from the file system."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'mounted'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'flush_dev'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Umount %s"'
op|')'
op|'%'
name|'self'
op|'.'
name|'mapped_device'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'umount'"
op|','
name|'self'
op|'.'
name|'mapped_device'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'mounted'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|member|flush_dev
dedent|''
name|'def'
name|'flush_dev'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
nl|'\n'
DECL|member|do_mount
dedent|''
name|'def'
name|'do_mount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the get, map and mnt operations."""'
newline|'\n'
name|'status'
op|'='
name|'False'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'status'
op|'='
name|'self'
op|'.'
name|'get_dev'
op|'('
op|')'
name|'and'
name|'self'
op|'.'
name|'map_dev'
op|'('
op|')'
name|'and'
name|'self'
op|'.'
name|'mnt_dev'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'status'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Fail to mount, tearing back down"'
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'do_teardown'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'status'
newline|'\n'
nl|'\n'
DECL|member|do_umount
dedent|''
name|'def'
name|'do_umount'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the unmnt operation."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'mounted'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unmnt_dev'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|do_teardown
dedent|''
dedent|''
name|'def'
name|'do_teardown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Call the umnt, unmap, and unget operations."""'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'mounted'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unmnt_dev'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'mapped'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unmap_dev'
op|'('
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'linked'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'unget_dev'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
