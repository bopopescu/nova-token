begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
comment|'#'
nl|'\n'
comment|'# Copyright 2011 Nexenta Systems, Inc.'
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
string|'"""\n:mod:`nexenta.volume` -- Driver to store volumes on Nexenta Appliance\n=====================================================================\n\n.. automodule:: nexenta.volume\n.. moduleauthor:: Yuriy Taraday <yorik.sar@gmail.com>\n"""'
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
op|'.'
name|'volume'
name|'import'
name|'driver'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'nexenta'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
op|'.'
name|'nexenta'
name|'import'
name|'jsonrpc'
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
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
nl|'\n'
DECL|variable|nexenta_opts
name|'nexenta_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nexenta_host'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IP address of Nexenta SA'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'nexenta_rest_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'2000'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'HTTP port to connect to Nexenta REST API server'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nexenta_rest_protocol'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'auto'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Use http or https for REST connection (default auto)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nexenta_user'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'admin'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'User name to connect to Nexenta SA'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nexenta_password'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nexenta'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Password to connect to Nexenta SA'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'IntOpt'
op|'('
string|"'nexenta_iscsi_target_portal_port'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
number|'3260'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Nexenta target portal port'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nexenta_volume'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'pool on SA that will hold all volumes'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nexenta_target_prefix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'iqn.1986-03.com.sun:02:nova-'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'IQN prefix for iSCSI targets'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nexenta_target_group_prefix'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'nova/'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'prefix for iSCSI target groups on SA'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'nexenta_blocksize'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"''"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'block size for volumes (blank=default,8KB)'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'nexenta_sparse'"
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
string|"'flag to create sparse volumes'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'nexenta_opts'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|NexentaDriver
name|'class'
name|'NexentaDriver'
op|'('
name|'driver'
op|'.'
name|'ISCSIDriver'
op|')'
op|':'
comment|'# pylint: disable=R0921'
newline|'\n'
indent|'    '
string|'"""Executes volume driver commands on Nexenta Appliance."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'super'
op|'('
name|'NexentaDriver'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|')'
newline|'\n'
nl|'\n'
DECL|member|do_setup
dedent|''
name|'def'
name|'do_setup'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'protocol'
op|'='
name|'FLAGS'
op|'.'
name|'nexenta_rest_protocol'
newline|'\n'
name|'auto'
op|'='
name|'protocol'
op|'=='
string|"'auto'"
newline|'\n'
name|'if'
name|'auto'
op|':'
newline|'\n'
indent|'            '
name|'protocol'
op|'='
string|"'http'"
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'nms'
op|'='
name|'jsonrpc'
op|'.'
name|'NexentaJSONProxy'
op|'('
nl|'\n'
string|"'%s://%s:%s/rest/nms/'"
op|'%'
op|'('
name|'protocol'
op|','
name|'FLAGS'
op|'.'
name|'nexenta_host'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'nexenta_rest_port'
op|')'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'nexenta_user'
op|','
name|'FLAGS'
op|'.'
name|'nexenta_password'
op|','
name|'auto'
op|'='
name|'auto'
op|')'
newline|'\n'
nl|'\n'
DECL|member|check_for_setup_error
dedent|''
name|'def'
name|'check_for_setup_error'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Verify that the volume for our zvols exists.\n\n        :raise: :py:exc:`LookupError`\n        """'
newline|'\n'
name|'if'
name|'not'
name|'self'
op|'.'
name|'nms'
op|'.'
name|'volume'
op|'.'
name|'object_exists'
op|'('
name|'FLAGS'
op|'.'
name|'nexenta_volume'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'LookupError'
op|'('
name|'_'
op|'('
string|'"Volume %s does not exist in Nexenta SA"'
op|')'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'nexenta_volume'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_zvol_name
name|'def'
name|'_get_zvol_name'
op|'('
name|'volume_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return zvol name that corresponds given volume name."""'
newline|'\n'
name|'return'
string|"'%s/%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'nexenta_volume'
op|','
name|'volume_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_target_name
name|'def'
name|'_get_target_name'
op|'('
name|'volume_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return iSCSI target name to access volume."""'
newline|'\n'
name|'return'
string|"'%s%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'nexenta_target_prefix'
op|','
name|'volume_name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'staticmethod'
newline|'\n'
DECL|member|_get_target_group_name
name|'def'
name|'_get_target_group_name'
op|'('
name|'volume_name'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return Nexenta iSCSI target group name for volume."""'
newline|'\n'
name|'return'
string|"'%s%s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'nexenta_target_group_prefix'
op|','
name|'volume_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume
dedent|''
name|'def'
name|'create_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create a zvol on appliance.\n\n        :param volume: volume reference\n        """'
newline|'\n'
name|'self'
op|'.'
name|'nms'
op|'.'
name|'zvol'
op|'.'
name|'create'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_zvol_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
op|','
nl|'\n'
string|"'%sG'"
op|'%'
op|'('
name|'volume'
op|'['
string|"'size'"
op|']'
op|','
op|')'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'nexenta_blocksize'
op|','
name|'FLAGS'
op|'.'
name|'nexenta_sparse'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_volume
dedent|''
name|'def'
name|'delete_volume'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy a zvol on appliance.\n\n        :param volume: volume reference\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'zvol'
op|'.'
name|'destroy'
op|'('
name|'self'
op|'.'
name|'_get_zvol_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
op|','
string|"''"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|'"zvol has children"'
name|'in'
name|'exc'
op|'.'
name|'args'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'VolumeIsBusy'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|create_snapshot
dedent|''
dedent|''
dedent|''
name|'def'
name|'create_snapshot'
op|'('
name|'self'
op|','
name|'snapshot'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create snapshot of existing zvol on appliance.\n\n        :param snapshot: shapshot reference\n        """'
newline|'\n'
name|'self'
op|'.'
name|'nms'
op|'.'
name|'zvol'
op|'.'
name|'create_snapshot'
op|'('
nl|'\n'
name|'self'
op|'.'
name|'_get_zvol_name'
op|'('
name|'snapshot'
op|'['
string|"'volume_name'"
op|']'
op|')'
op|','
nl|'\n'
name|'snapshot'
op|'['
string|"'name'"
op|']'
op|','
string|"''"
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_volume_from_snapshot
dedent|''
name|'def'
name|'create_volume_from_snapshot'
op|'('
name|'self'
op|','
name|'volume'
op|','
name|'snapshot'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create new volume from other\'s snapshot on appliance.\n\n        :param volume: reference of volume to be created\n        :param snapshot: reference of source snapshot\n        """'
newline|'\n'
name|'self'
op|'.'
name|'nms'
op|'.'
name|'zvol'
op|'.'
name|'clone'
op|'('
nl|'\n'
string|"'%s@%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'_get_zvol_name'
op|'('
name|'snapshot'
op|'['
string|"'volume_name'"
op|']'
op|')'
op|','
nl|'\n'
name|'snapshot'
op|'['
string|"'name'"
op|']'
op|')'
op|','
nl|'\n'
name|'self'
op|'.'
name|'_get_zvol_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_snapshot
dedent|''
name|'def'
name|'delete_snapshot'
op|'('
name|'self'
op|','
name|'snapshot'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete volume\'s snapshot on appliance.\n\n        :param snapshot: shapshot reference\n        """'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'snapshot'
op|'.'
name|'destroy'
op|'('
nl|'\n'
string|"'%s@%s'"
op|'%'
op|'('
name|'self'
op|'.'
name|'_get_zvol_name'
op|'('
name|'snapshot'
op|'['
string|"'volume_name'"
op|']'
op|')'
op|','
nl|'\n'
name|'snapshot'
op|'['
string|"'name'"
op|']'
op|')'
op|','
nl|'\n'
string|"''"
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
string|'"snapshot has dependent clones"'
name|'in'
name|'exc'
op|'.'
name|'args'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
name|'exception'
op|'.'
name|'SnapshotIsBusy'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
nl|'\n'
DECL|member|local_path
dedent|''
dedent|''
dedent|''
name|'def'
name|'local_path'
op|'('
name|'self'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Return local path to existing local volume.\n\n        We never have local volumes, so it raises NotImplementedError.\n\n        :raise: :py:exc:`NotImplementedError`\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|'"Call to local_path should not happen."'
nl|'\n'
string|'" Verify that use_local_volumes flag is turned off."'
op|')'
op|')'
newline|'\n'
name|'raise'
name|'NotImplementedError'
newline|'\n'
nl|'\n'
DECL|member|_do_export
dedent|''
name|'def'
name|'_do_export'
op|'('
name|'self'
op|','
name|'_ctx'
op|','
name|'volume'
op|','
name|'ensure'
op|'='
name|'False'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Do all steps to get zvol exported as LUN 0 at separate target.\n\n        :param volume: reference of volume to be exported\n        :param ensure: if True, ignore errors caused by already existing\n            resources\n        :return: iscsiadm-formatted provider location string\n        """'
newline|'\n'
name|'zvol_name'
op|'='
name|'self'
op|'.'
name|'_get_zvol_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'target_name'
op|'='
name|'self'
op|'.'
name|'_get_target_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'target_group_name'
op|'='
name|'self'
op|'.'
name|'_get_target_group_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'iscsitarget'
op|'.'
name|'create_target'
op|'('
op|'{'
string|"'target_name'"
op|':'
name|'target_name'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'ensure'
name|'or'
string|"'already configured'"
name|'not'
name|'in'
name|'exc'
op|'.'
name|'args'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'\'Ignored target creation error "%s"\''
nl|'\n'
string|"' while ensuring export'"
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'stmf'
op|'.'
name|'create_targetgroup'
op|'('
name|'target_group_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'ensure'
name|'or'
string|"'already exists'"
name|'not'
name|'in'
name|'exc'
op|'.'
name|'args'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'\'Ignored target group creation error "%s"\''
nl|'\n'
string|"' while ensuring export'"
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'stmf'
op|'.'
name|'add_targetgroup_member'
op|'('
name|'target_group_name'
op|','
nl|'\n'
name|'target_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'ensure'
name|'or'
string|"'already exists'"
name|'not'
name|'in'
name|'exc'
op|'.'
name|'args'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'\'Ignored target group member addition error "%s"\''
nl|'\n'
string|"' while ensuring export'"
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'scsidisk'
op|'.'
name|'create_lu'
op|'('
name|'zvol_name'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'ensure'
name|'or'
string|"'in use'"
name|'not'
name|'in'
name|'exc'
op|'.'
name|'args'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'\'Ignored LU creation error "%s"\''
nl|'\n'
string|"' while ensuring export'"
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'scsidisk'
op|'.'
name|'add_lun_mapping_entry'
op|'('
name|'zvol_name'
op|','
op|'{'
nl|'\n'
string|"'target_group'"
op|':'
name|'target_group_name'
op|','
nl|'\n'
string|"'lun'"
op|':'
string|"'0'"
op|'}'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'not'
name|'ensure'
name|'or'
string|"'view entry exists'"
name|'not'
name|'in'
name|'exc'
op|'.'
name|'args'
op|'['
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                '
name|'raise'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'\'Ignored LUN mapping entry addition error "%s"\''
nl|'\n'
string|"' while ensuring export'"
op|')'
op|','
name|'exc'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
string|"'%s:%s,1 %s'"
op|'%'
op|'('
name|'FLAGS'
op|'.'
name|'nexenta_host'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'nexenta_iscsi_target_portal_port'
op|','
nl|'\n'
name|'target_name'
op|')'
newline|'\n'
nl|'\n'
DECL|member|create_export
dedent|''
name|'def'
name|'create_export'
op|'('
name|'self'
op|','
name|'_ctx'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Create new export for zvol.\n\n        :param volume: reference of volume to be exported\n        :return: iscsiadm-formatted provider location string\n        """'
newline|'\n'
name|'loc'
op|'='
name|'self'
op|'.'
name|'_do_export'
op|'('
name|'_ctx'
op|','
name|'volume'
op|','
name|'ensure'
op|'='
name|'False'
op|')'
newline|'\n'
name|'return'
op|'{'
string|"'provider_location'"
op|':'
name|'loc'
op|'}'
newline|'\n'
nl|'\n'
DECL|member|ensure_export
dedent|''
name|'def'
name|'ensure_export'
op|'('
name|'self'
op|','
name|'_ctx'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Recreate parts of export if necessary.\n\n        :param volume: reference of volume to be exported\n        """'
newline|'\n'
name|'self'
op|'.'
name|'_do_export'
op|'('
name|'_ctx'
op|','
name|'volume'
op|','
name|'ensure'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
DECL|member|remove_export
dedent|''
name|'def'
name|'remove_export'
op|'('
name|'self'
op|','
name|'_ctx'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Destroy all resources created to export zvol.\n\n        :param volume: reference of volume to be unexported\n        """'
newline|'\n'
name|'zvol_name'
op|'='
name|'self'
op|'.'
name|'_get_zvol_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'target_name'
op|'='
name|'self'
op|'.'
name|'_get_target_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'target_group_name'
op|'='
name|'self'
op|'.'
name|'_get_target_group_name'
op|'('
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'nms'
op|'.'
name|'scsidisk'
op|'.'
name|'delete_lu'
op|'('
name|'zvol_name'
op|')'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'stmf'
op|'.'
name|'destroy_targetgroup'
op|'('
name|'target_group_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# We assume that target group is already gone'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Got error trying to destroy target group'"
nl|'\n'
string|"' %(target_group)s, assuming it is already gone: %(exc)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'target_group'"
op|':'
name|'target_group_name'
op|','
string|"'exc'"
op|':'
name|'exc'
op|'}'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'nms'
op|'.'
name|'iscsitarget'
op|'.'
name|'delete_target'
op|'('
name|'target_name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'nexenta'
op|'.'
name|'NexentaException'
name|'as'
name|'exc'
op|':'
newline|'\n'
comment|'# We assume that target is gone as well'
nl|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warn'
op|'('
name|'_'
op|'('
string|"'Got error trying to delete target %(target)s,'"
nl|'\n'
string|"' assuming it is already gone: %(exc)s'"
op|')'
op|','
nl|'\n'
op|'{'
string|"'target'"
op|':'
name|'target_name'
op|','
string|"'exc'"
op|':'
name|'exc'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
dedent|''
endmarker|''
end_unit
