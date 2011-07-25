begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Zadara Storage Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack LLC.'
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
string|'"""\nHandles all processes relating to Virtual Storage Arrays (VSA).\n\n**Related Flags**\n\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'manager'
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
name|'from'
name|'nova'
name|'import'
name|'exception'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'vsa'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'vsa'
op|'.'
name|'api'
name|'import'
name|'VsaState'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
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
name|'DEFINE_string'
op|'('
string|"'vsa_driver'"
op|','
string|"'nova.vsa.connection.get_connection'"
op|','
nl|'\n'
string|"'Driver to use for controlling VSAs'"
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
string|"'nova.vsa.manager'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VsaManager
name|'class'
name|'VsaManager'
op|'('
name|'manager'
op|'.'
name|'SchedulerDependentManager'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Manages Virtual Storage Arrays (VSAs)."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'vsa_driver'
op|'='
name|'None'
op|','
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'not'
name|'vsa_driver'
op|':'
newline|'\n'
indent|'            '
name|'vsa_driver'
op|'='
name|'FLAGS'
op|'.'
name|'vsa_driver'
newline|'\n'
dedent|''
name|'self'
op|'.'
name|'driver'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'vsa_driver'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_manager'
op|'='
name|'utils'
op|'.'
name|'import_object'
op|'('
name|'FLAGS'
op|'.'
name|'compute_manager'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'='
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'='
name|'vsa'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'super'
op|'('
name|'VsaManager'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'*'
name|'args'
op|','
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|init_host
dedent|''
name|'def'
name|'init_host'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'driver'
op|'.'
name|'init_host'
op|'('
name|'host'
op|'='
name|'self'
op|'.'
name|'host'
op|')'
newline|'\n'
name|'super'
op|'('
name|'VsaManager'
op|','
name|'self'
op|')'
op|'.'
name|'init_host'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
op|')'
newline|'\n'
DECL|member|create_vsa
name|'def'
name|'create_vsa'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa_id'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Called by API if there were no BE volumes assigned"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Create call received for VSA %s"'
op|')'
op|','
name|'vsa_id'
op|')'
newline|'\n'
nl|'\n'
name|'vsa_id'
op|'='
name|'int'
op|'('
name|'vsa_id'
op|')'
comment|'# just in case'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vsa'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Failed to find VSA %(vsa_id)d"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_start_vcs'
op|'('
name|'context'
op|','
name|'vsa'
op|')'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'exception'
op|'.'
name|'wrap_exception'
op|'('
op|')'
newline|'\n'
DECL|member|vsa_volume_created
name|'def'
name|'vsa_volume_created'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vol_id'
op|','
name|'vsa_id'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Callback for volume creations"""'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)s: Volume %(vol_id)s created. "'
string|'"Status %(status)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'vsa_id'
op|'='
name|'int'
op|'('
name|'vsa_id'
op|')'
comment|'# just in case'
newline|'\n'
nl|'\n'
comment|'# Get all volumes for this VSA'
nl|'\n'
comment|'# check if any of them still in creating phase'
nl|'\n'
name|'volumes'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_get_all_assigned_to_vsa'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'volume'
op|'['
string|"'status'"
op|']'
op|'=='
string|"'creating'"
op|':'
newline|'\n'
indent|'                '
name|'vol_name'
op|'='
name|'volume'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vol_disp_name'
op|'='
name|'volume'
op|'['
string|"'display_name'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Volume %(vol_name)s (%(vol_disp_name)s) still "'
string|'"in creating phase - wait"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vsa'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Failed to find VSA %(vsa_id)d"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'volumes'
op|')'
op|'!='
name|'vsa'
op|'['
string|"'vol_count'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'cvol_real'
op|'='
name|'len'
op|'('
name|'volumes'
op|')'
newline|'\n'
name|'cvol_exp'
op|'='
name|'vsa'
op|'['
string|"'vol_count'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)d: Not all volumes are created "'
string|'"(%(cvol_real)d of %(cvol_exp)d)"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
comment|'# all volumes created (successfully or not)'
nl|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'_start_vcs'
op|'('
name|'context'
op|','
name|'vsa'
op|','
name|'volumes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_start_vcs
dedent|''
name|'def'
name|'_start_vcs'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa'
op|','
name|'volumes'
op|'='
op|'['
op|']'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Start VCs for VSA """'
newline|'\n'
nl|'\n'
name|'vsa_id'
op|'='
name|'vsa'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'if'
name|'vsa'
op|'['
string|"'status'"
op|']'
op|'=='
name|'VsaState'
op|'.'
name|'CREATING'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'update_vsa_status'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
nl|'\n'
name|'VsaState'
op|'.'
name|'LAUNCHING'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
newline|'\n'
nl|'\n'
comment|'# in _separate_ loop go over all volumes and mark as "attached"'
nl|'\n'
dedent|''
name|'has_failed_volumes'
op|'='
name|'False'
newline|'\n'
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'vol_name'
op|'='
name|'volume'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vol_disp_name'
op|'='
name|'volume'
op|'['
string|"'display_name'"
op|']'
newline|'\n'
name|'status'
op|'='
name|'volume'
op|'['
string|"'status'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)d: Volume %(vol_name)s "'
string|'"(%(vol_disp_name)s) is in %(status)s state"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'if'
name|'status'
op|'=='
string|"'available'"
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
comment|"# self.volume_api.update(context, volume['id'],"
nl|'\n'
comment|'#                   dict(attach_status="attached"))'
nl|'\n'
indent|'                    '
name|'pass'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
name|'as'
name|'ex'
op|':'
newline|'\n'
indent|'                    '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Failed to update attach status for volume "'
nl|'\n'
string|'"%(vol_name)s. %(ex)s"'
op|')'
op|'%'
name|'locals'
op|'('
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'has_failed_volumes'
op|'='
name|'True'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'has_failed_volumes'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)d: Delete all BE volumes"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'delete_be_volumes'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
name|'force_delete'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'update_vsa_status'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
name|'VsaState'
op|'.'
name|'FAILED'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
comment|'# create user-data record for VC'
nl|'\n'
dedent|''
name|'storage_data'
op|'='
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'generate_user_data'
op|'('
name|'context'
op|','
name|'vsa'
op|','
name|'volumes'
op|')'
newline|'\n'
nl|'\n'
name|'instance_type'
op|'='
name|'instance_types'
op|'.'
name|'get_instance_type'
op|'('
nl|'\n'
name|'vsa'
op|'['
string|"'instance_type_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# now start the VC instance'
nl|'\n'
nl|'\n'
name|'vc_count'
op|'='
name|'vsa'
op|'['
string|"'vc_count'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)d: Start %(vc_count)d instances"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'vc_instances'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'create'
op|'('
name|'context'
op|','
nl|'\n'
name|'instance_type'
op|','
comment|"# vsa['vsa_instance_type'],"
nl|'\n'
name|'vsa'
op|'['
string|"'image_ref'"
op|']'
op|','
nl|'\n'
name|'min_count'
op|'='
number|'1'
op|','
nl|'\n'
name|'max_count'
op|'='
name|'vc_count'
op|','
nl|'\n'
name|'display_name'
op|'='
string|"'vc-'"
op|'+'
name|'vsa'
op|'['
string|"'display_name'"
op|']'
op|','
nl|'\n'
name|'display_description'
op|'='
string|"'VC for VSA '"
op|'+'
name|'vsa'
op|'['
string|"'display_name'"
op|']'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'vsa'
op|'['
string|"'availability_zone'"
op|']'
op|','
nl|'\n'
name|'user_data'
op|'='
name|'storage_data'
op|','
nl|'\n'
name|'vsa_id'
op|'='
name|'vsa_id'
op|')'
newline|'\n'
nl|'\n'
name|'self'
op|'.'
name|'vsa_api'
op|'.'
name|'update_vsa_status'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
name|'VsaState'
op|'.'
name|'CREATED'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
