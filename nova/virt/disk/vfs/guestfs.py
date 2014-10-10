begin_unit
comment|'# Copyright 2012 Red Hat, Inc.'
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
nl|'\n'
name|'from'
name|'eventlet'
name|'import'
name|'tpool'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
name|'from'
name|'oslo'
op|'.'
name|'utils'
name|'import'
name|'importutils'
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
name|'_'
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
op|'.'
name|'virt'
op|'.'
name|'disk'
op|'.'
name|'vfs'
name|'import'
name|'api'
name|'as'
name|'vfs'
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
DECL|variable|guestfs
name|'guestfs'
op|'='
name|'None'
newline|'\n'
DECL|variable|forceTCG
name|'forceTCG'
op|'='
name|'False'
newline|'\n'
nl|'\n'
DECL|variable|guestfs_opts
name|'guestfs_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'debug'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'False'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Enable guestfs debug'"
op|')'
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
name|'guestfs_opts'
op|','
name|'group'
op|'='
string|"'guestfs'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|force_tcg
name|'def'
name|'force_tcg'
op|'('
name|'force'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Prevent libguestfs trying to use KVM acceleration\n\n    It is a good idea to call this if it is known that\n    KVM is not desired, even if technically available.\n    """'
newline|'\n'
nl|'\n'
name|'global'
name|'forceTCG'
newline|'\n'
name|'forceTCG'
op|'='
name|'force'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VFSGuestFS
dedent|''
name|'class'
name|'VFSGuestFS'
op|'('
name|'vfs'
op|'.'
name|'VFS'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
string|'"""This class implements a VFS module that uses the libguestfs APIs\n    to access the disk image. The disk image is never mapped into\n    the host filesystem, thus avoiding any potential for symlink\n    attacks from the guest filesystem.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'imgfile'
op|','
name|'imgfmt'
op|'='
string|"'raw'"
op|','
name|'partition'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VFSGuestFS'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'imgfile'
op|','
name|'imgfmt'
op|','
name|'partition'
op|')'
newline|'\n'
nl|'\n'
name|'global'
name|'guestfs'
newline|'\n'
name|'if'
name|'guestfs'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'guestfs'
op|'='
name|'importutils'
op|'.'
name|'import_module'
op|'('
string|"'guestfs'"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"libguestfs is not installed (%s)"'
op|')'
op|'%'
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'handle'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|inspect_capabilities
dedent|''
name|'def'
name|'inspect_capabilities'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Determines whether guestfs is well configured."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'g'
op|'='
name|'guestfs'
op|'.'
name|'GuestFS'
op|'('
op|')'
newline|'\n'
name|'g'
op|'.'
name|'add_drive'
op|'('
string|'"/dev/null"'
op|')'
comment|'# sic'
newline|'\n'
name|'g'
op|'.'
name|'launch'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"libguestfs installed but not usable (%s)"'
op|')'
op|'%'
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|configure_debug
dedent|''
name|'def'
name|'configure_debug'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Configures guestfs to be verbose."""'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'handle'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_LW'
op|'('
string|'"Please consider to execute setup before trying "'
nl|'\n'
string|'"to configure debug log message."'
op|')'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
DECL|function|log_callback
indent|'            '
name|'def'
name|'log_callback'
op|'('
name|'ev'
op|','
name|'eh'
op|','
name|'buf'
op|','
name|'array'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'ev'
op|'=='
name|'guestfs'
op|'.'
name|'EVENT_APPLIANCE'
op|':'
newline|'\n'
indent|'                    '
name|'buf'
op|'='
name|'buf'
op|'.'
name|'rstrip'
op|'('
op|')'
newline|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"event=%(event)s eh=%(eh)d buf=\'%(buf)s\' "'
nl|'\n'
string|'"array=%(array)s"'
op|','
op|'{'
nl|'\n'
string|'"event"'
op|':'
name|'guestfs'
op|'.'
name|'event_to_string'
op|'('
name|'ev'
op|')'
op|','
nl|'\n'
string|'"eh"'
op|':'
name|'eh'
op|','
string|'"buf"'
op|':'
name|'buf'
op|','
string|'"array"'
op|':'
name|'array'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'events'
op|'='
op|'('
name|'guestfs'
op|'.'
name|'EVENT_APPLIANCE'
op|'|'
name|'guestfs'
op|'.'
name|'EVENT_LIBRARY'
nl|'\n'
op|'|'
name|'guestfs'
op|'.'
name|'EVENT_WARNING'
op|'|'
name|'guestfs'
op|'.'
name|'EVENT_TRACE'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'set_trace'
op|'('
name|'True'
op|')'
comment|'# just traces libguestfs API calls'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'set_verbose'
op|'('
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'set_event_callback'
op|'('
name|'log_callback'
op|','
name|'events'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_os
dedent|''
dedent|''
name|'def'
name|'setup_os'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
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
name|'setup_os_inspect'
op|'('
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'setup_os_static'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_os_static
dedent|''
dedent|''
name|'def'
name|'setup_os_static'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Mount guest OS image %(imgfile)s partition %(part)s"'
op|','
nl|'\n'
op|'{'
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|','
string|"'part'"
op|':'
name|'str'
op|'('
name|'self'
op|'.'
name|'partition'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'self'
op|'.'
name|'partition'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'mount_options'
op|'('
string|'""'
op|','
string|'"/dev/sda%d"'
op|'%'
name|'self'
op|'.'
name|'partition'
op|','
string|'"/"'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'mount_options'
op|'('
string|'""'
op|','
string|'"/dev/sda"'
op|','
string|'"/"'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_os_inspect
dedent|''
dedent|''
name|'def'
name|'setup_os_inspect'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Inspecting guest OS image %s"'
op|','
name|'self'
op|'.'
name|'imgfile'
op|')'
newline|'\n'
name|'roots'
op|'='
name|'self'
op|'.'
name|'handle'
op|'.'
name|'inspect_os'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'roots'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
string|'"No operating system found in %s"'
op|')'
nl|'\n'
op|'%'
name|'self'
op|'.'
name|'imgfile'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'roots'
op|')'
op|'!='
number|'1'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Multi-boot OS %(roots)s"'
op|','
op|'{'
string|"'roots'"
op|':'
name|'str'
op|'('
name|'roots'
op|')'
op|'}'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Multi-boot operating system found in %s"'
op|')'
op|'%'
nl|'\n'
name|'self'
op|'.'
name|'imgfile'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'setup_os_root'
op|'('
name|'roots'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup_os_root
dedent|''
name|'def'
name|'setup_os_root'
op|'('
name|'self'
op|','
name|'root'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Inspecting guest OS root filesystem %s"'
op|','
name|'root'
op|')'
newline|'\n'
name|'mounts'
op|'='
name|'self'
op|'.'
name|'handle'
op|'.'
name|'inspect_get_mountpoints'
op|'('
name|'root'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'mounts'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"No mount points found in %(root)s of %(imgfile)s"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'root'"
op|':'
name|'root'
op|','
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|'}'
op|')'
newline|'\n'
nl|'\n'
comment|'# the root directory must be mounted first'
nl|'\n'
dedent|''
name|'mounts'
op|'.'
name|'sort'
op|'('
name|'key'
op|'='
name|'lambda'
name|'mount'
op|':'
name|'mount'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'root_mounted'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'mount'
name|'in'
name|'mounts'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Mounting %(dev)s at %(dir)s"'
op|','
nl|'\n'
op|'{'
string|"'dev'"
op|':'
name|'mount'
op|'['
number|'1'
op|']'
op|','
string|"'dir'"
op|':'
name|'mount'
op|'['
number|'0'
op|']'
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'mount_options'
op|'('
string|'""'
op|','
name|'mount'
op|'['
number|'1'
op|']'
op|','
name|'mount'
op|'['
number|'0'
op|']'
op|')'
newline|'\n'
name|'root_mounted'
op|'='
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Error mounting %(device)s to %(dir)s in image"'
nl|'\n'
string|'" %(imgfile)s with libguestfs (%(e)s)"'
op|')'
op|'%'
op|'{'
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|','
string|"'device'"
op|':'
name|'mount'
op|'['
number|'1'
op|']'
op|','
nl|'\n'
string|"'dir'"
op|':'
name|'mount'
op|'['
number|'0'
op|']'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
newline|'\n'
name|'if'
name|'root_mounted'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|setup
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'setup'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Setting up appliance for %(imgfile)s %(imgfmt)s"'
op|','
nl|'\n'
op|'{'
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|','
string|"'imgfmt'"
op|':'
name|'self'
op|'.'
name|'imgfmt'
op|'}'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'='
name|'tpool'
op|'.'
name|'Proxy'
op|'('
nl|'\n'
name|'guestfs'
op|'.'
name|'GuestFS'
op|'('
name|'python_return_dict'
op|'='
name|'False'
op|','
nl|'\n'
name|'close_on_exit'
op|'='
name|'False'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'TypeError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'if'
op|'('
string|"'close_on_exit'"
name|'in'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|')'
name|'or'
nl|'\n'
string|"'python_return_dict'"
name|'in'
name|'six'
op|'.'
name|'text_type'
op|'('
name|'e'
op|')'
op|')'
op|':'
newline|'\n'
comment|"# NOTE(russellb) In case we're not using a version of"
nl|'\n'
comment|'# libguestfs new enough to support parameters close_on_exit'
nl|'\n'
comment|'# and python_return_dict which were added in libguestfs 1.20.'
nl|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'='
name|'tpool'
op|'.'
name|'Proxy'
op|'('
name|'guestfs'
op|'.'
name|'GuestFS'
op|'('
op|')'
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
name|'if'
name|'CONF'
op|'.'
name|'guestfs'
op|'.'
name|'debug'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'configure_debug'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'forceTCG'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'set_backend_settings'
op|'('
string|'"force_tcg"'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'AttributeError'
name|'as'
name|'ex'
op|':'
newline|'\n'
comment|"# set_backend_settings method doesn't exist in older"
nl|'\n'
comment|'# libguestfs versions, so nothing we can do but ignore'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|'"Unable to force TCG mode, libguestfs too old? %s"'
op|')'
op|','
nl|'\n'
name|'ex'
op|')'
newline|'\n'
name|'pass'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'add_drive_opts'
op|'('
name|'self'
op|'.'
name|'imgfile'
op|','
name|'format'
op|'='
name|'self'
op|'.'
name|'imgfmt'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'launch'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'setup_os'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'aug_init'
op|'('
string|'"/"'
op|','
number|'0'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
name|'as'
name|'e'
op|':'
newline|'\n'
comment|'# explicitly teardown instead of implicit close()'
nl|'\n'
comment|'# to prevent orphaned VMs in cases when an implicit'
nl|'\n'
comment|'# close() is not enough'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
nl|'\n'
name|'_'
op|'('
string|'"Error mounting %(imgfile)s with libguestfs (%(e)s)"'
op|')'
op|'%'
nl|'\n'
op|'{'
string|"'imgfile'"
op|':'
name|'self'
op|'.'
name|'imgfile'
op|','
string|"'e'"
op|':'
name|'e'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
comment|'# explicitly teardown instead of implicit close()'
nl|'\n'
comment|'# to prevent orphaned VMs in cases when an implicit'
nl|'\n'
comment|'# close() is not enough'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'teardown'
op|'('
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|teardown
dedent|''
dedent|''
name|'def'
name|'teardown'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Tearing down appliance"'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'aug_close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to close augeas %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'shutdown'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# Older libguestfs versions haven't an explicit shutdown"
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to shutdown appliance %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'AttributeError'
op|':'
newline|'\n'
comment|"# Older libguestfs versions haven't an explicit close"
nl|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|'"Failed to close guest handle %s"'
op|')'
op|','
name|'e'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
comment|'# dereference object and implicitly close()'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_canonicalize_path
name|'def'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'path'
op|'['
number|'0'
op|']'
op|'!='
string|"'/'"
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'/'"
op|'+'
name|'path'
newline|'\n'
dedent|''
name|'return'
name|'path'
newline|'\n'
nl|'\n'
DECL|member|make_path
dedent|''
name|'def'
name|'make_path'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Make directory path=%s"'
op|','
name|'path'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'mkdir_p'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|append_file
dedent|''
name|'def'
name|'append_file'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'content'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Append file path=%s"'
op|','
name|'path'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'write_append'
op|'('
name|'path'
op|','
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|replace_file
dedent|''
name|'def'
name|'replace_file'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'content'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Replace file path=%s"'
op|','
name|'path'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'write'
op|'('
name|'path'
op|','
name|'content'
op|')'
newline|'\n'
nl|'\n'
DECL|member|read_file
dedent|''
name|'def'
name|'read_file'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Read file path=%s"'
op|','
name|'path'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'read_file'
op|'('
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|has_file
dedent|''
name|'def'
name|'has_file'
op|'('
name|'self'
op|','
name|'path'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Has file path=%s"'
op|','
name|'path'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'handle'
op|'.'
name|'stat'
op|'('
name|'path'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'except'
name|'RuntimeError'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|set_permissions
dedent|''
dedent|''
name|'def'
name|'set_permissions'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'mode'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Set permissions path=%(path)s mode=%(mode)s"'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
string|"'mode'"
op|':'
name|'mode'
op|'}'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'chmod'
op|'('
name|'mode'
op|','
name|'path'
op|')'
newline|'\n'
nl|'\n'
DECL|member|set_ownership
dedent|''
name|'def'
name|'set_ownership'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'user'
op|','
name|'group'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"Set ownership path=%(path)s "'
nl|'\n'
string|'"user=%(user)s group=%(group)s"'
op|','
nl|'\n'
op|'{'
string|"'path'"
op|':'
name|'path'
op|','
string|"'user'"
op|':'
name|'user'
op|','
string|"'group'"
op|':'
name|'group'
op|'}'
op|')'
newline|'\n'
name|'path'
op|'='
name|'self'
op|'.'
name|'_canonicalize_path'
op|'('
name|'path'
op|')'
newline|'\n'
name|'uid'
op|'='
op|'-'
number|'1'
newline|'\n'
name|'gid'
op|'='
op|'-'
number|'1'
newline|'\n'
nl|'\n'
name|'if'
name|'user'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'uid'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'handle'
op|'.'
name|'aug_get'
op|'('
nl|'\n'
string|'"/files/etc/passwd/"'
op|'+'
name|'user'
op|'+'
string|'"/uid"'
op|')'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'group'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'gid'
op|'='
name|'int'
op|'('
name|'self'
op|'.'
name|'handle'
op|'.'
name|'aug_get'
op|'('
nl|'\n'
string|'"/files/etc/group/"'
op|'+'
name|'group'
op|'+'
string|'"/gid"'
op|')'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"chown uid=%(uid)d gid=%(gid)s"'
op|','
nl|'\n'
op|'{'
string|"'uid'"
op|':'
name|'uid'
op|','
string|"'gid'"
op|':'
name|'gid'
op|'}'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'handle'
op|'.'
name|'chown'
op|'('
name|'uid'
op|','
name|'gid'
op|','
name|'path'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
