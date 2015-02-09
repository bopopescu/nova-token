begin_unit
comment|'# Copyright (c) 2015 Quobyte Inc.'
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
name|'os'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_concurrency'
name|'import'
name|'processutils'
newline|'\n'
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
name|'as'
name|'nova_exception'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'i18n'
name|'import'
name|'_'
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
name|'_LI'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'fileutils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'utils'
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
DECL|variable|SOURCE_PROTOCOL
name|'SOURCE_PROTOCOL'
op|'='
string|"'quobyte'"
newline|'\n'
DECL|variable|SOURCE_TYPE
name|'SOURCE_TYPE'
op|'='
string|"'file'"
newline|'\n'
DECL|variable|DRIVER_CACHE
name|'DRIVER_CACHE'
op|'='
string|"'none'"
newline|'\n'
DECL|variable|DRIVER_IO
name|'DRIVER_IO'
op|'='
string|"'native'"
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|mount_volume
name|'def'
name|'mount_volume'
op|'('
name|'volume'
op|','
name|'mnt_base'
op|','
name|'configfile'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wraps execute calls for mounting a Quobyte volume"""'
newline|'\n'
name|'fileutils'
op|'.'
name|'ensure_tree'
op|'('
name|'mnt_base'
op|')'
newline|'\n'
nl|'\n'
name|'command'
op|'='
op|'['
string|"'mount.quobyte'"
op|','
name|'volume'
op|','
name|'mnt_base'
op|']'
newline|'\n'
name|'if'
name|'configfile'
op|':'
newline|'\n'
indent|'        '
name|'command'
op|'.'
name|'extend'
op|'('
op|'['
string|"'-c'"
op|','
name|'configfile'
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Mounting volume %s at mount point %s ...'"
op|','
nl|'\n'
name|'volume'
op|','
nl|'\n'
name|'mnt_base'
op|')'
newline|'\n'
comment|'# Run mount command but do not fail on already mounted exit code'
nl|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'command'
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
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|"'Mounted volume: %s'"
op|')'
op|','
name|'volume'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|umount_volume
dedent|''
name|'def'
name|'umount_volume'
op|'('
name|'mnt_base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wraps execute calls for unmouting a Quobyte volume"""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'umount.quobyte'"
op|','
name|'mnt_base'
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
name|'exc'
op|'.'
name|'message'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_LE'
op|'('
string|'"The Quobyte volume at %s is still in use."'
op|')'
op|','
nl|'\n'
name|'mnt_base'
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
string|'"Couldn\'t unmount the Quobyte Volume at %s"'
op|')'
op|','
nl|'\n'
name|'mnt_base'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|validate_volume
dedent|''
dedent|''
dedent|''
name|'def'
name|'validate_volume'
op|'('
name|'mnt_base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Wraps execute calls for checking validity of a Quobyte volume"""'
newline|'\n'
name|'command'
op|'='
op|'['
string|"'getfattr'"
op|','
string|'"-n"'
op|','
string|'"quobyte.info"'
op|','
name|'mnt_base'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'command'
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
name|'msg'
op|'='
op|'('
name|'_'
op|'('
string|'"The mount %(mount_path)s is not a valid"'
nl|'\n'
string|'" Quobyte volume. Error: %(exc)s"'
op|')'
nl|'\n'
op|'%'
op|'{'
string|"'mount_path'"
op|':'
name|'mnt_base'
op|','
string|"'exc'"
op|':'
name|'exc'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'nova_exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'os'
op|'.'
name|'access'
op|'('
name|'mnt_base'
op|','
name|'os'
op|'.'
name|'W_OK'
op|'|'
name|'os'
op|'.'
name|'X_OK'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
op|'('
name|'_LE'
op|'('
string|'"Volume is not writable. Please broaden the file"'
nl|'\n'
string|'" permissions. Mount: %s"'
op|')'
op|'%'
name|'mnt_base'
op|')'
newline|'\n'
name|'raise'
name|'nova_exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
