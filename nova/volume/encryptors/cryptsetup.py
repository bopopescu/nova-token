begin_unit
comment|'# Copyright (c) 2013 The Johns Hopkins University/Applied Physics Laboratory'
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
nl|'\n'
name|'import'
name|'binascii'
newline|'\n'
name|'import'
name|'os'
newline|'\n'
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
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'encryptors'
name|'import'
name|'base'
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
nl|'\n'
DECL|class|CryptsetupEncryptor
name|'class'
name|'CryptsetupEncryptor'
op|'('
name|'base'
op|'.'
name|'VolumeEncryptor'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""A VolumeEncryptor based on dm-crypt.\n\n    This VolumeEncryptor uses dm-crypt to encrypt the specified volume.\n    """'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'CryptsetupEncryptor'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'connection_info'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# Fail if no device_path was set when connecting the volume, e.g. in'
nl|'\n'
comment|'# the case of libvirt network volume drivers.'
nl|'\n'
name|'data'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'data'
op|'.'
name|'get'
op|'('
string|"'device_path'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'volume_id'
op|'='
name|'data'
op|'.'
name|'get'
op|'('
string|"'volume_id'"
op|')'
name|'or'
name|'connection_info'
op|'.'
name|'get'
op|'('
string|"'serial'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'VolumeEncryptionNotSupported'
op|'('
nl|'\n'
name|'volume_id'
op|'='
name|'volume_id'
op|','
nl|'\n'
name|'volume_type'
op|'='
name|'connection_info'
op|'['
string|"'driver_volume_type'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|"# the device's path as given to libvirt -- e.g., /dev/disk/by-path/..."
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'symlink_path'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
newline|'\n'
nl|'\n'
comment|'# a unique name for the volume -- e.g., the iSCSI participant name'
nl|'\n'
name|'self'
op|'.'
name|'dev_name'
op|'='
name|'self'
op|'.'
name|'symlink_path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
newline|'\n'
comment|"# the device's actual path on the compute host -- e.g., /dev/sd_"
nl|'\n'
name|'self'
op|'.'
name|'dev_path'
op|'='
name|'os'
op|'.'
name|'path'
op|'.'
name|'realpath'
op|'('
name|'self'
op|'.'
name|'symlink_path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_passphrase
dedent|''
name|'def'
name|'_get_passphrase'
op|'('
name|'self'
op|','
name|'key'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Convert raw key to string."""'
newline|'\n'
name|'return'
name|'binascii'
op|'.'
name|'hexlify'
op|'('
name|'key'
op|')'
op|'.'
name|'decode'
op|'('
string|"'utf-8'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|_open_volume
dedent|''
name|'def'
name|'_open_volume'
op|'('
name|'self'
op|','
name|'passphrase'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Opens the LUKS partition on the volume using the specified\n        passphrase.\n\n        :param passphrase: the passphrase used to access the volume\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"opening encrypted volume %s"'
op|','
name|'self'
op|'.'
name|'dev_path'
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(joel-coffman): cryptsetup will strip trailing newlines from'
nl|'\n'
comment|'# input specified on stdin unless --key-file=- is specified.'
nl|'\n'
name|'cmd'
op|'='
op|'['
string|'"cryptsetup"'
op|','
string|'"create"'
op|','
string|'"--key-file=-"'
op|']'
newline|'\n'
nl|'\n'
name|'cipher'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"cipher"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'cipher'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'.'
name|'extend'
op|'('
op|'['
string|'"--cipher"'
op|','
name|'cipher'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'key_size'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|'"key_size"'
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'key_size'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'cmd'
op|'.'
name|'extend'
op|'('
op|'['
string|'"--key-size"'
op|','
name|'key_size'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'cmd'
op|'.'
name|'extend'
op|'('
op|'['
name|'self'
op|'.'
name|'dev_name'
op|','
name|'self'
op|'.'
name|'dev_path'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'cmd'
op|','
name|'process_input'
op|'='
name|'passphrase'
op|','
nl|'\n'
name|'check_exit_code'
op|'='
name|'True'
op|','
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'context'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Shadows the device and passes an unencrypted version to the\n        instance.\n\n        Transparent disk encryption is achieved by mounting the volume via\n        dm-crypt and passing the resulting device to the instance. The\n        instance is unaware of the underlying encryption due to modifying the\n        original symbolic link to refer to the device mounted by dm-crypt.\n        """'
newline|'\n'
nl|'\n'
name|'key'
op|'='
name|'self'
op|'.'
name|'_get_key'
op|'('
name|'context'
op|')'
op|'.'
name|'get_encoded'
op|'('
op|')'
newline|'\n'
name|'passphrase'
op|'='
name|'self'
op|'.'
name|'_get_passphrase'
op|'('
name|'key'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'_open_volume'
op|'('
name|'passphrase'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
comment|'# modify the original symbolic link to refer to the decrypted device'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'ln'"
op|','
string|"'--symbolic'"
op|','
string|"'--force'"
op|','
nl|'\n'
string|"'/dev/mapper/%s'"
op|'%'
name|'self'
op|'.'
name|'dev_name'
op|','
name|'self'
op|'.'
name|'symlink_path'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'check_exit_code'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_close_volume
dedent|''
name|'def'
name|'_close_volume'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Closes the device (effectively removes the dm-crypt mapping)."""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"closing encrypted volume %s"'
op|','
name|'self'
op|'.'
name|'dev_path'
op|')'
newline|'\n'
comment|'# cryptsetup returns 4 when attempting to destroy a non-active'
nl|'\n'
comment|'# dm-crypt device. We are going to ignore this error code to make'
nl|'\n'
comment|'# nova deleting that instance successfully.'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'cryptsetup'"
op|','
string|"'remove'"
op|','
name|'self'
op|'.'
name|'dev_name'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|','
name|'check_exit_code'
op|'='
op|'['
number|'0'
op|','
number|'4'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Removes the dm-crypt mapping for the device."""'
newline|'\n'
name|'self'
op|'.'
name|'_close_volume'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
