begin_unit
comment|'# Copyright 2012 Grid Dynamics'
nl|'\n'
comment|'# Copyright 2013 Inktank Storage, Inc.'
nl|'\n'
comment|'# Copyright 2014 Mirantis, Inc.'
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
name|'urllib'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'    '
name|'import'
name|'rados'
newline|'\n'
name|'import'
name|'rbd'
newline|'\n'
dedent|''
name|'except'
name|'ImportError'
op|':'
newline|'\n'
DECL|variable|rados
indent|'    '
name|'rados'
op|'='
name|'None'
newline|'\n'
DECL|variable|rbd
name|'rbd'
op|'='
name|'None'
newline|'\n'
nl|'\n'
dedent|''
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_serialization'
name|'import'
name|'jsonutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'excutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'units'
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
name|'_LE'
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
nl|'\n'
DECL|class|RBDVolumeProxy
name|'class'
name|'RBDVolumeProxy'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Context manager for dealing with an existing rbd volume.\n\n    This handles connecting to rados and opening an ioctx automatically, and\n    otherwise acts like a librbd Image object.\n\n    The underlying librados client and ioctx can be accessed as the attributes\n    \'client\' and \'ioctx\'.\n    """'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'driver'
op|','
name|'name'
op|','
name|'pool'
op|'='
name|'None'
op|','
name|'snapshot'
op|'='
name|'None'
op|','
nl|'\n'
name|'read_only'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'client'
op|','
name|'ioctx'
op|'='
name|'driver'
op|'.'
name|'_connect_to_rados'
op|'('
name|'pool'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'snap_name'
op|'='
name|'snapshot'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
name|'if'
name|'snapshot'
name|'else'
name|'None'
newline|'\n'
name|'self'
op|'.'
name|'volume'
op|'='
name|'rbd'
op|'.'
name|'Image'
op|'('
name|'ioctx'
op|','
name|'name'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
op|','
nl|'\n'
name|'snapshot'
op|'='
name|'snap_name'
op|','
nl|'\n'
name|'read_only'
op|'='
name|'read_only'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rbd'
op|'.'
name|'ImageNotFound'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|'"rbd image %s does not exist"'
op|','
name|'name'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'_disconnect_from_rados'
op|'('
name|'client'
op|','
name|'ioctx'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'rbd'
op|'.'
name|'Error'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'excutils'
op|'.'
name|'save_and_reraise_exception'
op|'('
op|')'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_LE'
op|'('
string|'"error opening rbd image %s"'
op|')'
op|','
name|'name'
op|')'
newline|'\n'
name|'driver'
op|'.'
name|'_disconnect_from_rados'
op|'('
name|'client'
op|','
name|'ioctx'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'client'
op|'='
name|'client'
newline|'\n'
name|'self'
op|'.'
name|'ioctx'
op|'='
name|'ioctx'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'type_'
op|','
name|'value'
op|','
name|'traceback'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'volume'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_disconnect_from_rados'
op|'('
name|'self'
op|'.'
name|'client'
op|','
name|'self'
op|'.'
name|'ioctx'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__getattr__
dedent|''
dedent|''
name|'def'
name|'__getattr__'
op|'('
name|'self'
op|','
name|'attrib'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'getattr'
op|'('
name|'self'
op|'.'
name|'volume'
op|','
name|'attrib'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RADOSClient
dedent|''
dedent|''
name|'class'
name|'RADOSClient'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Context manager to simplify error handling for connecting to ceph."""'
newline|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'driver'
op|','
name|'pool'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'driver'
op|'='
name|'driver'
newline|'\n'
name|'self'
op|'.'
name|'cluster'
op|','
name|'self'
op|'.'
name|'ioctx'
op|'='
name|'driver'
op|'.'
name|'_connect_to_rados'
op|'('
name|'pool'
op|')'
newline|'\n'
nl|'\n'
DECL|member|__enter__
dedent|''
name|'def'
name|'__enter__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'self'
newline|'\n'
nl|'\n'
DECL|member|__exit__
dedent|''
name|'def'
name|'__exit__'
op|'('
name|'self'
op|','
name|'type_'
op|','
name|'value'
op|','
name|'traceback'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'_disconnect_from_rados'
op|'('
name|'self'
op|'.'
name|'cluster'
op|','
name|'self'
op|'.'
name|'ioctx'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|RBDDriver
dedent|''
dedent|''
name|'class'
name|'RBDDriver'
op|'('
name|'object'
op|')'
op|':'
newline|'\n'
nl|'\n'
DECL|member|__init__
indent|'    '
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'pool'
op|','
name|'ceph_conf'
op|','
name|'rbd_user'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'pool'
op|'='
name|'pool'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
newline|'\n'
comment|'# NOTE(angdraug): rados.Rados fails to connect if ceph_conf is None:'
nl|'\n'
comment|'# https://github.com/ceph/ceph/pull/1787'
nl|'\n'
name|'self'
op|'.'
name|'ceph_conf'
op|'='
name|'ceph_conf'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
name|'if'
name|'ceph_conf'
name|'else'
string|"''"
newline|'\n'
name|'self'
op|'.'
name|'rbd_user'
op|'='
name|'rbd_user'
op|'.'
name|'encode'
op|'('
string|"'utf8'"
op|')'
name|'if'
name|'rbd_user'
name|'else'
name|'None'
newline|'\n'
name|'if'
name|'rbd'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'RuntimeError'
op|'('
name|'_'
op|'('
string|"'rbd python libraries not found'"
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_connect_to_rados
dedent|''
dedent|''
name|'def'
name|'_connect_to_rados'
op|'('
name|'self'
op|','
name|'pool'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'client'
op|'='
name|'rados'
op|'.'
name|'Rados'
op|'('
name|'rados_id'
op|'='
name|'self'
op|'.'
name|'rbd_user'
op|','
nl|'\n'
name|'conffile'
op|'='
name|'self'
op|'.'
name|'ceph_conf'
op|')'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'client'
op|'.'
name|'connect'
op|'('
op|')'
newline|'\n'
name|'pool_to_open'
op|'='
name|'pool'
name|'or'
name|'self'
op|'.'
name|'pool'
newline|'\n'
name|'ioctx'
op|'='
name|'client'
op|'.'
name|'open_ioctx'
op|'('
name|'pool_to_open'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
op|')'
newline|'\n'
name|'return'
name|'client'
op|','
name|'ioctx'
newline|'\n'
dedent|''
name|'except'
name|'rados'
op|'.'
name|'Error'
op|':'
newline|'\n'
comment|'# shutdown cannot raise an exception'
nl|'\n'
indent|'            '
name|'client'
op|'.'
name|'shutdown'
op|'('
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|_disconnect_from_rados
dedent|''
dedent|''
name|'def'
name|'_disconnect_from_rados'
op|'('
name|'self'
op|','
name|'client'
op|','
name|'ioctx'
op|')'
op|':'
newline|'\n'
comment|'# closing an ioctx cannot raise an exception'
nl|'\n'
indent|'        '
name|'ioctx'
op|'.'
name|'close'
op|'('
op|')'
newline|'\n'
name|'client'
op|'.'
name|'shutdown'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|supports_layering
dedent|''
name|'def'
name|'supports_layering'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'hasattr'
op|'('
name|'rbd'
op|','
string|"'RBD_FEATURE_LAYERING'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|ceph_args
dedent|''
name|'def'
name|'ceph_args'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""List of command line parameters to be passed to ceph commands to\n           reflect RBDDriver configuration such as RBD user name and location\n           of ceph.conf.\n        """'
newline|'\n'
name|'args'
op|'='
op|'['
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'rbd_user'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'extend'
op|'('
op|'['
string|"'--id'"
op|','
name|'self'
op|'.'
name|'rbd_user'
op|']'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'ceph_conf'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'.'
name|'extend'
op|'('
op|'['
string|"'--conf'"
op|','
name|'self'
op|'.'
name|'ceph_conf'
op|']'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'args'
newline|'\n'
nl|'\n'
DECL|member|get_mon_addrs
dedent|''
name|'def'
name|'get_mon_addrs'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'args'
op|'='
op|'['
string|"'ceph'"
op|','
string|"'mon'"
op|','
string|"'dump'"
op|','
string|"'--format=json'"
op|']'
op|'+'
name|'self'
op|'.'
name|'ceph_args'
op|'('
op|')'
newline|'\n'
name|'out'
op|','
name|'_'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
op|'*'
name|'args'
op|')'
newline|'\n'
name|'lines'
op|'='
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
newline|'\n'
name|'if'
name|'lines'
op|'['
number|'0'
op|']'
op|'.'
name|'startswith'
op|'('
string|"'dumped monmap epoch'"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'lines'
op|'='
name|'lines'
op|'['
number|'1'
op|':'
op|']'
newline|'\n'
dedent|''
name|'monmap'
op|'='
name|'jsonutils'
op|'.'
name|'loads'
op|'('
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'lines'
op|')'
op|')'
newline|'\n'
name|'addrs'
op|'='
op|'['
name|'mon'
op|'['
string|"'addr'"
op|']'
name|'for'
name|'mon'
name|'in'
name|'monmap'
op|'['
string|"'mons'"
op|']'
op|']'
newline|'\n'
name|'hosts'
op|'='
op|'['
op|']'
newline|'\n'
name|'ports'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'addr'
name|'in'
name|'addrs'
op|':'
newline|'\n'
indent|'            '
name|'host_port'
op|'='
name|'addr'
op|'['
op|':'
name|'addr'
op|'.'
name|'rindex'
op|'('
string|"'/'"
op|')'
op|']'
newline|'\n'
name|'host'
op|','
name|'port'
op|'='
name|'host_port'
op|'.'
name|'rsplit'
op|'('
string|"':'"
op|','
number|'1'
op|')'
newline|'\n'
name|'hosts'
op|'.'
name|'append'
op|'('
name|'host'
op|'.'
name|'strip'
op|'('
string|"'[]'"
op|')'
op|')'
newline|'\n'
name|'ports'
op|'.'
name|'append'
op|'('
name|'port'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'hosts'
op|','
name|'ports'
newline|'\n'
nl|'\n'
DECL|member|parse_url
dedent|''
name|'def'
name|'parse_url'
op|'('
name|'self'
op|','
name|'url'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'prefix'
op|'='
string|"'rbd://'"
newline|'\n'
name|'if'
name|'not'
name|'url'
op|'.'
name|'startswith'
op|'('
name|'prefix'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'reason'
op|'='
name|'_'
op|'('
string|"'Not stored in rbd'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'url'
op|','
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
dedent|''
name|'pieces'
op|'='
name|'map'
op|'('
name|'urllib'
op|'.'
name|'unquote'
op|','
name|'url'
op|'['
name|'len'
op|'('
name|'prefix'
op|')'
op|':'
op|']'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
op|')'
newline|'\n'
name|'if'
string|"''"
name|'in'
name|'pieces'
op|':'
newline|'\n'
indent|'            '
name|'reason'
op|'='
name|'_'
op|'('
string|"'Blank components'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'url'
op|','
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'pieces'
op|')'
op|'!='
number|'4'
op|':'
newline|'\n'
indent|'            '
name|'reason'
op|'='
name|'_'
op|'('
string|"'Not an rbd snapshot'"
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'ImageUnacceptable'
op|'('
name|'image_id'
op|'='
name|'url'
op|','
name|'reason'
op|'='
name|'reason'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'pieces'
newline|'\n'
nl|'\n'
DECL|member|_get_fsid
dedent|''
name|'def'
name|'_get_fsid'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'RADOSClient'
op|'('
name|'self'
op|')'
name|'as'
name|'client'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'client'
op|'.'
name|'cluster'
op|'.'
name|'get_fsid'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|is_cloneable
dedent|''
dedent|''
name|'def'
name|'is_cloneable'
op|'('
name|'self'
op|','
name|'image_location'
op|','
name|'image_meta'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'url'
op|'='
name|'image_location'
op|'['
string|"'url'"
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'fsid'
op|','
name|'pool'
op|','
name|'image'
op|','
name|'snapshot'
op|'='
name|'self'
op|'.'
name|'parse_url'
op|'('
name|'url'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'ImageUnacceptable'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'not cloneable: %s'"
op|','
name|'e'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'self'
op|'.'
name|'_get_fsid'
op|'('
op|')'
op|'!='
name|'fsid'
op|':'
newline|'\n'
indent|'            '
name|'reason'
op|'='
string|"'%s is in a different ceph cluster'"
op|'%'
name|'url'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'reason'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'image_meta'
op|'['
string|"'disk_format'"
op|']'
op|'!='
string|"'raw'"
op|':'
newline|'\n'
indent|'            '
name|'reason'
op|'='
op|'('
string|'"rbd image clone requires image format to be "'
nl|'\n'
string|'"\'raw\' but image {0} is \'{1}\'"'
op|')'
op|'.'
name|'format'
op|'('
nl|'\n'
name|'url'
op|','
name|'image_meta'
op|'['
string|"'disk_format'"
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'reason'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
comment|'# check that we can read the image'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'exists'
op|'('
name|'image'
op|','
name|'pool'
op|'='
name|'pool'
op|','
name|'snapshot'
op|'='
name|'snapshot'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'rbd'
op|'.'
name|'Error'
name|'as'
name|'e'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'Unable to open image %(loc)s: %(err)s'"
op|'%'
nl|'\n'
name|'dict'
op|'('
name|'loc'
op|'='
name|'url'
op|','
name|'err'
op|'='
name|'e'
op|')'
op|')'
newline|'\n'
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|clone
dedent|''
dedent|''
name|'def'
name|'clone'
op|'('
name|'self'
op|','
name|'image_location'
op|','
name|'dest_name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'_fsid'
op|','
name|'pool'
op|','
name|'image'
op|','
name|'snapshot'
op|'='
name|'self'
op|'.'
name|'parse_url'
op|'('
nl|'\n'
name|'image_location'
op|'['
string|"'url'"
op|']'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'cloning %(pool)s/%(img)s@%(snap)s'"
op|'%'
nl|'\n'
name|'dict'
op|'('
name|'pool'
op|'='
name|'pool'
op|','
name|'img'
op|'='
name|'image'
op|','
name|'snap'
op|'='
name|'snapshot'
op|')'
op|')'
newline|'\n'
name|'with'
name|'RADOSClient'
op|'('
name|'self'
op|','
name|'str'
op|'('
name|'pool'
op|')'
op|')'
name|'as'
name|'src_client'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'RADOSClient'
op|'('
name|'self'
op|')'
name|'as'
name|'dest_client'
op|':'
newline|'\n'
indent|'                '
name|'rbd'
op|'.'
name|'RBD'
op|'('
op|')'
op|'.'
name|'clone'
op|'('
name|'src_client'
op|'.'
name|'ioctx'
op|','
nl|'\n'
name|'image'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
op|','
nl|'\n'
name|'snapshot'
op|'.'
name|'encode'
op|'('
string|"'utf-8'"
op|')'
op|','
nl|'\n'
name|'dest_client'
op|'.'
name|'ioctx'
op|','
nl|'\n'
name|'dest_name'
op|','
nl|'\n'
name|'features'
op|'='
name|'rbd'
op|'.'
name|'RBD_FEATURE_LAYERING'
op|')'
newline|'\n'
nl|'\n'
DECL|member|size
dedent|''
dedent|''
dedent|''
name|'def'
name|'size'
op|'('
name|'self'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'RBDVolumeProxy'
op|'('
name|'self'
op|','
name|'name'
op|')'
name|'as'
name|'vol'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'vol'
op|'.'
name|'size'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|resize
dedent|''
dedent|''
name|'def'
name|'resize'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'size'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Resize RBD volume.\n\n        :name: Name of RBD object\n        :size: New size in bytes\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
string|"'resizing rbd image %s to %d'"
op|','
name|'name'
op|','
name|'size'
op|')'
newline|'\n'
name|'with'
name|'RBDVolumeProxy'
op|'('
name|'self'
op|','
name|'name'
op|')'
name|'as'
name|'vol'
op|':'
newline|'\n'
indent|'            '
name|'vol'
op|'.'
name|'resize'
op|'('
name|'size'
op|')'
newline|'\n'
nl|'\n'
DECL|member|exists
dedent|''
dedent|''
name|'def'
name|'exists'
op|'('
name|'self'
op|','
name|'name'
op|','
name|'pool'
op|'='
name|'None'
op|','
name|'snapshot'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'with'
name|'RBDVolumeProxy'
op|'('
name|'self'
op|','
name|'name'
op|','
nl|'\n'
name|'pool'
op|'='
name|'pool'
op|','
nl|'\n'
name|'snapshot'
op|'='
name|'snapshot'
op|','
nl|'\n'
name|'read_only'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'True'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'rbd'
op|'.'
name|'ImageNotFound'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'False'
newline|'\n'
nl|'\n'
DECL|member|import_image
dedent|''
dedent|''
name|'def'
name|'import_image'
op|'('
name|'self'
op|','
name|'base'
op|','
name|'name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Import RBD volume from image file.\n\n        Uses the command line import instead of librbd since rbd import\n        command detects zeroes to preserve sparseness in the image.\n\n        :base: Path to image file\n        :name: Name of RBD volume\n        """'
newline|'\n'
name|'args'
op|'='
op|'['
string|"'--pool'"
op|','
name|'self'
op|'.'
name|'pool'
op|','
name|'base'
op|','
name|'name'
op|']'
newline|'\n'
name|'if'
name|'self'
op|'.'
name|'supports_layering'
op|'('
op|')'
op|':'
newline|'\n'
indent|'            '
name|'args'
op|'+='
op|'['
string|"'--new-format'"
op|']'
newline|'\n'
dedent|''
name|'args'
op|'+='
name|'self'
op|'.'
name|'ceph_args'
op|'('
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'rbd'"
op|','
string|"'import'"
op|','
op|'*'
name|'args'
op|')'
newline|'\n'
nl|'\n'
DECL|member|cleanup_volumes
dedent|''
name|'def'
name|'cleanup_volumes'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'RADOSClient'
op|'('
name|'self'
op|','
name|'self'
op|'.'
name|'pool'
op|')'
name|'as'
name|'client'
op|':'
newline|'\n'
nl|'\n'
DECL|function|belongs_to_instance
indent|'            '
name|'def'
name|'belongs_to_instance'
op|'('
name|'disk'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'disk'
op|'.'
name|'startswith'
op|'('
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'volumes'
op|'='
name|'rbd'
op|'.'
name|'RBD'
op|'('
op|')'
op|'.'
name|'list'
op|'('
name|'client'
op|'.'
name|'ioctx'
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'filter'
op|'('
name|'belongs_to_instance'
op|','
name|'volumes'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'rbd'
op|'.'
name|'RBD'
op|'('
op|')'
op|'.'
name|'remove'
op|'('
name|'client'
op|'.'
name|'ioctx'
op|','
name|'volume'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'rbd'
op|'.'
name|'ImageNotFound'
op|','
name|'rbd'
op|'.'
name|'ImageHasSnapshots'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_LW'
op|'('
string|"'rbd remove %(volume)s in pool %(pool)s '"
nl|'\n'
string|"'failed'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'volume'"
op|':'
name|'volume'
op|','
string|"'pool'"
op|':'
name|'self'
op|'.'
name|'pool'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_pool_info
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'get_pool_info'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'with'
name|'RADOSClient'
op|'('
name|'self'
op|')'
name|'as'
name|'client'
op|':'
newline|'\n'
indent|'            '
name|'stats'
op|'='
name|'client'
op|'.'
name|'cluster'
op|'.'
name|'get_cluster_stats'
op|'('
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'total'"
op|':'
name|'stats'
op|'['
string|"'kb'"
op|']'
op|'*'
name|'units'
op|'.'
name|'Ki'
op|','
nl|'\n'
string|"'free'"
op|':'
name|'stats'
op|'['
string|"'kb_avail'"
op|']'
op|'*'
name|'units'
op|'.'
name|'Ki'
op|','
nl|'\n'
string|"'used'"
op|':'
name|'stats'
op|'['
string|"'kb_used'"
op|']'
op|'*'
name|'units'
op|'.'
name|'Ki'
op|'}'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
