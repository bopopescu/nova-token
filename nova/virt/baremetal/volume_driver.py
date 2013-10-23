begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'# coding=utf-8'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2012 NTT DOCOMO, INC.'
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
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo'
op|'.'
name|'config'
name|'import'
name|'cfg'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
name|'as'
name|'nova_context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'network'
newline|'\n'
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
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'processutils'
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
name|'baremetal'
name|'import'
name|'db'
name|'as'
name|'bmdb'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'virt'
op|'.'
name|'libvirt'
name|'import'
name|'utils'
name|'as'
name|'libvirt_utils'
newline|'\n'
nl|'\n'
DECL|variable|opts
name|'opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'use_unsafe_iscsi'"
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
string|"'Do not set this out of dev/test environments. '"
nl|'\n'
string|"'If a node does not have a fixed PXE IP address, '"
nl|'\n'
string|"'volumes are exported with globally opened ACL'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'iscsi_iqn_prefix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'iqn.2010-10.org.openstack.baremetal'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'iSCSI IQN prefix used in baremetal volume connections.'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|baremetal_group
name|'baremetal_group'
op|'='
name|'cfg'
op|'.'
name|'OptGroup'
op|'('
name|'name'
op|'='
string|"'baremetal'"
op|','
nl|'\n'
DECL|variable|title
name|'title'
op|'='
string|"'Baremetal Options'"
op|')'
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
name|'register_group'
op|'('
name|'baremetal_group'
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'register_opts'
op|'('
name|'opts'
op|','
name|'baremetal_group'
op|')'
newline|'\n'
nl|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'host'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'use_ipv6'"
op|','
string|"'nova.netconf'"
op|')'
newline|'\n'
name|'CONF'
op|'.'
name|'import_opt'
op|'('
string|"'libvirt_volume_drivers'"
op|','
string|"'nova.virt.libvirt.driver'"
op|')'
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
DECL|function|_get_baremetal_node_by_instance_uuid
name|'def'
name|'_get_baremetal_node_by_instance_uuid'
op|'('
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'return'
name|'bmdb'
op|'.'
name|'bm_node_get_by_instance_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_create_iscsi_export_tgtadm
dedent|''
name|'def'
name|'_create_iscsi_export_tgtadm'
op|'('
name|'path'
op|','
name|'tid'
op|','
name|'iqn'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tgtadm'"
op|','
string|"'--lld'"
op|','
string|"'iscsi'"
op|','
nl|'\n'
string|"'--mode'"
op|','
string|"'target'"
op|','
nl|'\n'
string|"'--op'"
op|','
string|"'new'"
op|','
nl|'\n'
string|"'--tid'"
op|','
name|'tid'
op|','
nl|'\n'
string|"'--targetname'"
op|','
name|'iqn'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tgtadm'"
op|','
string|"'--lld'"
op|','
string|"'iscsi'"
op|','
nl|'\n'
string|"'--mode'"
op|','
string|"'logicalunit'"
op|','
nl|'\n'
string|"'--op'"
op|','
string|"'new'"
op|','
nl|'\n'
string|"'--tid'"
op|','
name|'tid'
op|','
nl|'\n'
string|"'--lun'"
op|','
string|"'1'"
op|','
nl|'\n'
string|"'--backing-store'"
op|','
name|'path'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_allow_iscsi_tgtadm
dedent|''
name|'def'
name|'_allow_iscsi_tgtadm'
op|'('
name|'tid'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tgtadm'"
op|','
string|"'--lld'"
op|','
string|"'iscsi'"
op|','
nl|'\n'
string|"'--mode'"
op|','
string|"'target'"
op|','
nl|'\n'
string|"'--op'"
op|','
string|"'bind'"
op|','
nl|'\n'
string|"'--tid'"
op|','
name|'tid'
op|','
nl|'\n'
string|"'--initiator-address'"
op|','
name|'address'
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_delete_iscsi_export_tgtadm
dedent|''
name|'def'
name|'_delete_iscsi_export_tgtadm'
op|'('
name|'tid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tgtadm'"
op|','
string|"'--lld'"
op|','
string|"'iscsi'"
op|','
nl|'\n'
string|"'--mode'"
op|','
string|"'logicalunit'"
op|','
nl|'\n'
string|"'--op'"
op|','
string|"'delete'"
op|','
nl|'\n'
string|"'--tid'"
op|','
name|'tid'
op|','
nl|'\n'
string|"'--lun'"
op|','
string|"'1'"
op|','
nl|'\n'
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
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tgtadm'"
op|','
string|"'--lld'"
op|','
string|"'iscsi'"
op|','
nl|'\n'
string|"'--mode'"
op|','
string|"'target'"
op|','
nl|'\n'
string|"'--op'"
op|','
string|"'delete'"
op|','
nl|'\n'
string|"'--tid'"
op|','
name|'tid'
op|','
nl|'\n'
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
op|':'
newline|'\n'
indent|'        '
name|'pass'
newline|'\n'
comment|'# Check if the tid is deleted, that is, check the tid no longer exists.'
nl|'\n'
comment|'# If the tid dose not exist, tgtadm returns with exit_code 22.'
nl|'\n'
comment|'# utils.execute() can check the exit_code if check_exit_code parameter is'
nl|'\n'
comment|'# passed. But, regardless of whether check_exit_code contains 0 or not,'
nl|'\n'
comment|'# if the exit_code is 0, the function dose not report errors. So we have to'
nl|'\n'
comment|'# catch a ProcessExecutionError and test its exit_code is 22.'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tgtadm'"
op|','
string|"'--lld'"
op|','
string|"'iscsi'"
op|','
nl|'\n'
string|"'--mode'"
op|','
string|"'target'"
op|','
nl|'\n'
string|"'--op'"
op|','
string|"'show'"
op|','
nl|'\n'
string|"'--tid'"
op|','
name|'tid'
op|','
nl|'\n'
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
name|'e'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'e'
op|'.'
name|'exit_code'
op|'=='
number|'22'
op|':'
newline|'\n'
comment|'# OK, the tid is deleted'
nl|'\n'
indent|'            '
name|'return'
newline|'\n'
dedent|''
name|'raise'
newline|'\n'
dedent|''
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
nl|'\n'
string|"'baremetal driver was unable to delete tid %s'"
op|')'
op|'%'
name|'tid'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_show_tgtadm
dedent|''
name|'def'
name|'_show_tgtadm'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'out'
op|','
name|'_'
op|'='
name|'utils'
op|'.'
name|'execute'
op|'('
string|"'tgtadm'"
op|','
string|"'--lld'"
op|','
string|"'iscsi'"
op|','
nl|'\n'
string|"'--mode'"
op|','
string|"'target'"
op|','
nl|'\n'
string|"'--op'"
op|','
string|"'show'"
op|','
nl|'\n'
name|'run_as_root'
op|'='
name|'True'
op|')'
newline|'\n'
name|'return'
name|'out'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_list_backingstore_path
dedent|''
name|'def'
name|'_list_backingstore_path'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'out'
op|'='
name|'_show_tgtadm'
op|'('
op|')'
newline|'\n'
name|'l'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'='
name|'re'
op|'.'
name|'search'
op|'('
string|"r'Backing store path: (.*)$'"
op|','
name|'line'
op|')'
newline|'\n'
name|'if'
name|'m'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|"'/'"
name|'in'
name|'m'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'l'
op|'.'
name|'append'
op|'('
name|'m'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'l'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_next_tid
dedent|''
name|'def'
name|'_get_next_tid'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'out'
op|'='
name|'_show_tgtadm'
op|'('
op|')'
newline|'\n'
name|'last_tid'
op|'='
number|'0'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'='
name|'re'
op|'.'
name|'search'
op|'('
string|"r'^Target (\\d+):'"
op|','
name|'line'
op|')'
newline|'\n'
name|'if'
name|'m'
op|':'
newline|'\n'
indent|'            '
name|'tid'
op|'='
name|'int'
op|'('
name|'m'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
name|'if'
name|'last_tid'
op|'<'
name|'tid'
op|':'
newline|'\n'
indent|'                '
name|'last_tid'
op|'='
name|'tid'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'last_tid'
op|'+'
number|'1'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_find_tid
dedent|''
name|'def'
name|'_find_tid'
op|'('
name|'iqn'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'out'
op|'='
name|'_show_tgtadm'
op|'('
op|')'
newline|'\n'
name|'pattern'
op|'='
string|"r'^Target (\\d+): *'"
op|'+'
name|'re'
op|'.'
name|'escape'
op|'('
name|'iqn'
op|')'
newline|'\n'
name|'for'
name|'line'
name|'in'
name|'out'
op|'.'
name|'split'
op|'('
string|"'\\n'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'m'
op|'='
name|'re'
op|'.'
name|'search'
op|'('
name|'pattern'
op|','
name|'line'
op|')'
newline|'\n'
name|'if'
name|'m'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'m'
op|'.'
name|'group'
op|'('
number|'1'
op|')'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_iqn
dedent|''
name|'def'
name|'_get_iqn'
op|'('
name|'instance_name'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'mp'
op|'='
name|'mountpoint'
op|'.'
name|'replace'
op|'('
string|"'/'"
op|','
string|"'-'"
op|')'
op|'.'
name|'strip'
op|'('
string|"'-'"
op|')'
newline|'\n'
name|'iqn'
op|'='
string|"'%s:%s-%s'"
op|'%'
op|'('
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'iscsi_iqn_prefix'
op|','
nl|'\n'
name|'instance_name'
op|','
nl|'\n'
name|'mp'
op|')'
newline|'\n'
name|'return'
name|'iqn'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_get_fixed_ips
dedent|''
name|'def'
name|'_get_fixed_ips'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'context'
op|'='
name|'nova_context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'nw_info'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'ips'
op|'='
name|'nw_info'
op|'.'
name|'fixed_ips'
op|'('
op|')'
newline|'\n'
name|'return'
name|'ips'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VolumeDriver
dedent|''
name|'class'
name|'VolumeDriver'
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
name|'virtapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'VolumeDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'virtapi'
op|'='
name|'virtapi'
newline|'\n'
name|'self'
op|'.'
name|'_initiator'
op|'='
name|'None'
newline|'\n'
nl|'\n'
DECL|member|get_volume_connector
dedent|''
name|'def'
name|'get_volume_connector'
op|'('
name|'self'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'self'
op|'.'
name|'_initiator'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_initiator'
op|'='
name|'libvirt_utils'
op|'.'
name|'get_iscsi_initiator'
op|'('
op|')'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'_initiator'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Could not determine iscsi initiator name '"
nl|'\n'
string|"'for instance %s'"
op|')'
op|'%'
name|'instance'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
op|'{'
nl|'\n'
string|"'ip'"
op|':'
name|'CONF'
op|'.'
name|'my_ip'
op|','
nl|'\n'
string|"'initiator'"
op|':'
name|'self'
op|'.'
name|'_initiator'
op|','
nl|'\n'
string|"'host'"
op|':'
name|'CONF'
op|'.'
name|'host'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|attach_volume
dedent|''
name|'def'
name|'attach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
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
DECL|member|detach_volume
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
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
nl|'\n'
DECL|class|LibvirtVolumeDriver
dedent|''
dedent|''
name|'class'
name|'LibvirtVolumeDriver'
op|'('
name|'VolumeDriver'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""The VolumeDriver delegates to nova.virt.libvirt.volume."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'virtapi'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'LibvirtVolumeDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
name|'virtapi'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_drivers'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'driver_str'
name|'in'
name|'CONF'
op|'.'
name|'libvirt_volume_drivers'
op|':'
newline|'\n'
indent|'            '
name|'driver_type'
op|','
name|'_sep'
op|','
name|'driver'
op|'='
name|'driver_str'
op|'.'
name|'partition'
op|'('
string|"'='"
op|')'
newline|'\n'
name|'driver_class'
op|'='
name|'importutils'
op|'.'
name|'import_class'
op|'('
name|'driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_drivers'
op|'['
name|'driver_type'
op|']'
op|'='
name|'driver_class'
op|'('
name|'self'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_volume_driver_method
dedent|''
dedent|''
name|'def'
name|'_volume_driver_method'
op|'('
name|'self'
op|','
name|'method_name'
op|','
name|'connection_info'
op|','
nl|'\n'
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'driver_type'
op|'='
name|'connection_info'
op|'.'
name|'get'
op|'('
string|"'driver_volume_type'"
op|')'
newline|'\n'
name|'if'
name|'driver_type'
name|'not'
name|'in'
name|'self'
op|'.'
name|'volume_drivers'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'exception'
op|'.'
name|'VolumeDriverNotFound'
op|'('
name|'driver_type'
op|'='
name|'driver_type'
op|')'
newline|'\n'
dedent|''
name|'driver'
op|'='
name|'self'
op|'.'
name|'volume_drivers'
op|'['
name|'driver_type'
op|']'
newline|'\n'
name|'method'
op|'='
name|'getattr'
op|'('
name|'driver'
op|','
name|'method_name'
op|')'
newline|'\n'
name|'return'
name|'method'
op|'('
name|'connection_info'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
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
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'fixed_ips'
op|'='
name|'_get_fixed_ips'
op|'('
name|'instance'
op|')'
newline|'\n'
name|'if'
name|'not'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'CONF'
op|'.'
name|'baremetal'
op|'.'
name|'use_unsafe_iscsi'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'NovaException'
op|'('
name|'_'
op|'('
nl|'\n'
string|"'No fixed PXE IP is associated to %s'"
op|')'
op|'%'
name|'instance'
op|'['
string|"'uuid'"
op|']'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'mount_device'
op|'='
name|'mountpoint'
op|'.'
name|'rpartition'
op|'('
string|'"/"'
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
name|'self'
op|'.'
name|'_volume_driver_method'
op|'('
string|"'connect_volume'"
op|','
nl|'\n'
name|'connection_info'
op|','
nl|'\n'
name|'mount_device'
op|')'
newline|'\n'
name|'device_path'
op|'='
name|'connection_info'
op|'['
string|"'data'"
op|']'
op|'['
string|"'device_path'"
op|']'
newline|'\n'
name|'iqn'
op|'='
name|'_get_iqn'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'tid'
op|'='
name|'_get_next_tid'
op|'('
op|')'
newline|'\n'
name|'_create_iscsi_export_tgtadm'
op|'('
name|'device_path'
op|','
name|'tid'
op|','
name|'iqn'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'            '
name|'for'
name|'ip'
name|'in'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'                '
name|'_allow_iscsi_tgtadm'
op|'('
name|'tid'
op|','
name|'ip'
op|'['
string|"'address'"
op|']'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# NOTE(NTTdocomo): Since nova-compute does not know the'
nl|'\n'
comment|"# instance's initiator ip, it allows any initiators"
nl|'\n'
comment|'# to connect to the volume. This means other bare-metal'
nl|'\n'
comment|'# instances that are not attached the volume can connect'
nl|'\n'
comment|'# to the volume. Do not set CONF.baremetal.use_unsafe_iscsi'
nl|'\n'
comment|'# out of dev/test environments.'
nl|'\n'
comment|'# TODO(NTTdocomo): support CHAP'
nl|'\n'
indent|'            '
name|'_allow_iscsi_tgtadm'
op|'('
name|'tid'
op|','
string|"'ALL'"
op|')'
newline|'\n'
nl|'\n'
DECL|member|detach_volume
dedent|''
dedent|''
name|'def'
name|'detach_volume'
op|'('
name|'self'
op|','
name|'connection_info'
op|','
name|'instance'
op|','
name|'mountpoint'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'mount_device'
op|'='
name|'mountpoint'
op|'.'
name|'rpartition'
op|'('
string|'"/"'
op|')'
op|'['
number|'2'
op|']'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'iqn'
op|'='
name|'_get_iqn'
op|'('
name|'instance'
op|'['
string|"'name'"
op|']'
op|','
name|'mountpoint'
op|')'
newline|'\n'
name|'tid'
op|'='
name|'_find_tid'
op|'('
name|'iqn'
op|')'
newline|'\n'
name|'if'
name|'tid'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'_delete_iscsi_export_tgtadm'
op|'('
name|'tid'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'detach volume could not find tid for %s'"
op|')'
op|'%'
name|'iqn'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'finally'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'_volume_driver_method'
op|'('
string|"'disconnect_volume'"
op|','
nl|'\n'
name|'connection_info'
op|','
nl|'\n'
name|'mount_device'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_block_devices
dedent|''
dedent|''
name|'def'
name|'get_all_block_devices'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Return all block devices in use on this node.\n        """'
newline|'\n'
name|'return'
name|'_list_backingstore_path'
op|'('
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
