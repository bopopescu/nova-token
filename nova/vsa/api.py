begin_unit
comment|'# vim: tabstop=4 shiftwidth=4 softtabstop=4'
nl|'\n'
nl|'\n'
comment|'# Copyright (c) 2011 Zadara Storage Inc.'
nl|'\n'
comment|'# Copyright (c) 2011 OpenStack LLC.'
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
string|'"""\nHandles all requests relating to Virtual Storage Arrays (VSAs).\n\nExperimental code. Requires special VSA image.\n\nFor assistance and guidelines pls contact\nZadara Storage Inc & Openstack community\n"""'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
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
name|'import'
name|'rpc'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'compute'
name|'import'
name|'instance_types'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'db'
name|'import'
name|'base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'volume'
name|'import'
name|'volume_types'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|VsaState
name|'class'
name|'VsaState'
op|':'
newline|'\n'
DECL|variable|CREATING
indent|'    '
name|'CREATING'
op|'='
string|"'creating'"
comment|'# VSA creating (not ready yet)'
newline|'\n'
DECL|variable|LAUNCHING
name|'LAUNCHING'
op|'='
string|"'launching'"
comment|'# Launching VCs (all BE volumes were created)'
newline|'\n'
DECL|variable|CREATED
name|'CREATED'
op|'='
string|"'created'"
comment|'# VSA fully created and ready for use'
newline|'\n'
DECL|variable|PARTIAL
name|'PARTIAL'
op|'='
string|"'partial'"
comment|'# Some BE drives were allocated'
newline|'\n'
DECL|variable|FAILED
name|'FAILED'
op|'='
string|"'failed'"
comment|'# Some BE storage allocations failed'
newline|'\n'
DECL|variable|DELETING
name|'DELETING'
op|'='
string|"'deleting'"
comment|'# VSA started the deletion procedure'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|vsa_opts
dedent|''
name|'vsa_opts'
op|'='
op|'['
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vsa_ec2_access_key'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'EC2 access key used by VSA for accessing nova'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vsa_ec2_user_id'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'None'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'User ID used by VSA for accessing nova'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'BoolOpt'
op|'('
string|"'vsa_multi_vol_creation'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
name|'True'
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Ask scheduler to create multiple volumes in one call'"
op|')'
op|','
nl|'\n'
name|'cfg'
op|'.'
name|'StrOpt'
op|'('
string|"'vsa_volume_type_name'"
op|','
nl|'\n'
DECL|variable|default
name|'default'
op|'='
string|"'VSA volume type'"
op|','
nl|'\n'
DECL|variable|help
name|'help'
op|'='
string|"'Name of volume type associated with FE VSA volumes'"
op|')'
op|','
nl|'\n'
op|']'
newline|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'FLAGS'
op|'.'
name|'register_opts'
op|'('
name|'vsa_opts'
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
DECL|class|API
name|'class'
name|'API'
op|'('
name|'base'
op|'.'
name|'Base'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""API for interacting with the VSA manager."""'
newline|'\n'
nl|'\n'
DECL|member|__init__
name|'def'
name|'__init__'
op|'('
name|'self'
op|','
name|'compute_api'
op|'='
name|'None'
op|','
name|'volume_api'
op|'='
name|'None'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute_api'
name|'or'
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
name|'volume_api'
name|'or'
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
name|'super'
op|'('
name|'API'
op|','
name|'self'
op|')'
op|'.'
name|'__init__'
op|'('
op|'**'
name|'kwargs'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_volume_type_correctness
dedent|''
name|'def'
name|'_check_volume_type_correctness'
op|'('
name|'self'
op|','
name|'vol_type'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
op|'('
name|'vol_type'
op|'.'
name|'get'
op|'('
string|"'extra_specs'"
op|')'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'vol_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'get'
op|'('
string|"'type'"
op|')'
op|'!='
string|"'vsa_drive'"
name|'or'
nl|'\n'
name|'vol_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'get'
op|'('
string|"'drive_type'"
op|')'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'vol_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'get'
op|'('
string|"'drive_size'"
op|')'
name|'is'
name|'None'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"invalid drive data"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_default_vsa_instance_type
dedent|''
dedent|''
name|'def'
name|'_get_default_vsa_instance_type'
op|'('
name|'self'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'instance_types'
op|'.'
name|'get_instance_type_by_name'
op|'('
nl|'\n'
name|'FLAGS'
op|'.'
name|'default_vsa_instance_type'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_check_storage_parameters
dedent|''
name|'def'
name|'_check_storage_parameters'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa_name'
op|','
name|'storage'
op|','
nl|'\n'
name|'shared'
op|','
name|'first_index'
op|'='
number|'0'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""\n        Translates storage array of disks to the list of volumes\n        :param storage: List of dictionaries with following keys:\n                        disk_name, num_disks, size\n        :param shared: Specifies if storage is dedicated or shared.\n                       For shared storage disks split into partitions\n        """'
newline|'\n'
name|'volume_params'
op|'='
op|'['
op|']'
newline|'\n'
name|'for'
name|'node'
name|'in'
name|'storage'
op|':'
newline|'\n'
nl|'\n'
indent|'            '
name|'name'
op|'='
name|'node'
op|'.'
name|'get'
op|'('
string|"'drive_name'"
op|','
name|'None'
op|')'
newline|'\n'
name|'num_disks'
op|'='
name|'node'
op|'.'
name|'get'
op|'('
string|"'num_drives'"
op|','
number|'1'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"drive_name not defined"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|'('
name|'reason'
op|'='
name|'msg'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'vol_type'
op|'='
name|'volume_types'
op|'.'
name|'get_volume_type_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'                '
name|'msg'
op|'='
name|'_'
op|'('
string|'"invalid drive type name %s"'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|'('
name|'reason'
op|'='
name|'msg'
op|'%'
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'_check_volume_type_correctness'
op|'('
name|'vol_type'
op|')'
newline|'\n'
nl|'\n'
comment|'# if size field present - override disk size specified in DB'
nl|'\n'
name|'size'
op|'='
name|'int'
op|'('
name|'node'
op|'.'
name|'get'
op|'('
string|"'size'"
op|','
nl|'\n'
name|'vol_type'
op|'['
string|"'extra_specs'"
op|']'
op|'.'
name|'get'
op|'('
string|"'drive_size'"
op|')'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'shared'
op|':'
newline|'\n'
indent|'                '
name|'part_size'
op|'='
name|'FLAGS'
op|'.'
name|'vsa_part_size_gb'
newline|'\n'
name|'total_capacity'
op|'='
name|'num_disks'
op|'*'
name|'size'
newline|'\n'
name|'num_volumes'
op|'='
name|'total_capacity'
op|'/'
name|'part_size'
newline|'\n'
name|'size'
op|'='
name|'part_size'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'num_volumes'
op|'='
name|'num_disks'
newline|'\n'
name|'size'
op|'='
number|'0'
comment|'# special handling for full drives'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'i'
name|'in'
name|'range'
op|'('
name|'num_volumes'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'volume_name'
op|'='
string|'"drive-%03d"'
op|'%'
name|'first_index'
newline|'\n'
name|'first_index'
op|'+='
number|'1'
newline|'\n'
name|'volume_desc'
op|'='
string|"'BE volume for VSA %s type %s'"
op|'%'
op|'('
name|'vsa_name'
op|','
name|'name'
op|')'
newline|'\n'
name|'volume'
op|'='
op|'{'
nl|'\n'
string|"'size'"
op|':'
name|'size'
op|','
nl|'\n'
string|"'name'"
op|':'
name|'volume_name'
op|','
nl|'\n'
string|"'description'"
op|':'
name|'volume_desc'
op|','
nl|'\n'
string|"'volume_type_id'"
op|':'
name|'vol_type'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'volume_params'
op|'.'
name|'append'
op|'('
name|'volume'
op|')'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'volume_params'
newline|'\n'
nl|'\n'
DECL|member|create
dedent|''
name|'def'
name|'create'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'display_name'
op|'='
string|"''"
op|','
name|'display_description'
op|'='
string|"''"
op|','
nl|'\n'
name|'vc_count'
op|'='
number|'1'
op|','
name|'instance_type'
op|'='
name|'None'
op|','
name|'image_name'
op|'='
name|'None'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'None'
op|','
name|'storage'
op|'='
op|'['
op|']'
op|','
name|'shared'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Provision VSA instance with compute instances and volumes\n\n        :param storage: List of dictionaries with following keys:\n                        disk_name, num_disks, size\n        :param shared: Specifies if storage is dedicated or shared.\n                       For shared storage disks split into partitions\n        """'
newline|'\n'
nl|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"*** Experimental VSA code ***"'
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'vc_count'
op|'>'
name|'FLAGS'
op|'.'
name|'max_vcs_in_vsa'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Requested number of VCs (%d) is too high."'
nl|'\n'
string|'" Setting to default"'
op|')'
op|','
name|'vc_count'
op|')'
newline|'\n'
name|'vc_count'
op|'='
name|'FLAGS'
op|'.'
name|'max_vcs_in_vsa'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'instance_type'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'instance_type'
op|'='
name|'self'
op|'.'
name|'_get_default_vsa_instance_type'
op|'('
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'availability_zone'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'availability_zone'
op|'='
name|'FLAGS'
op|'.'
name|'storage_availability_zone'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'storage'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'storage'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'shared'
name|'or'
name|'shared'
op|'=='
string|"'False'"
op|':'
newline|'\n'
indent|'            '
name|'shared'
op|'='
name|'False'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'shared'
op|'='
name|'True'
newline|'\n'
nl|'\n'
comment|'# check if image is ready before starting any work'
nl|'\n'
dedent|''
name|'if'
name|'image_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'image_name'
op|'='
name|'FLAGS'
op|'.'
name|'vc_image_name'
newline|'\n'
nl|'\n'
dedent|''
name|'image_service'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'image_service'
newline|'\n'
name|'vc_image'
op|'='
name|'image_service'
op|'.'
name|'show_by_name'
op|'('
name|'context'
op|','
name|'image_name'
op|')'
newline|'\n'
name|'vc_image_href'
op|'='
name|'vc_image'
op|'['
string|"'id'"
op|']'
newline|'\n'
nl|'\n'
name|'options'
op|'='
op|'{'
nl|'\n'
string|"'display_name'"
op|':'
name|'display_name'
op|','
nl|'\n'
string|"'display_description'"
op|':'
name|'display_description'
op|','
nl|'\n'
string|"'project_id'"
op|':'
name|'context'
op|'.'
name|'project_id'
op|','
nl|'\n'
string|"'availability_zone'"
op|':'
name|'availability_zone'
op|','
nl|'\n'
string|"'instance_type_id'"
op|':'
name|'instance_type'
op|'['
string|"'id'"
op|']'
op|','
nl|'\n'
string|"'image_ref'"
op|':'
name|'vc_image_href'
op|','
nl|'\n'
string|"'vc_count'"
op|':'
name|'vc_count'
op|','
nl|'\n'
string|"'status'"
op|':'
name|'VsaState'
op|'.'
name|'CREATING'
op|','
nl|'\n'
op|'}'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Creating VSA: %s"'
op|')'
op|'%'
name|'options'
op|')'
newline|'\n'
nl|'\n'
comment|'# create DB entry for VSA instance'
nl|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'vsa_create'
op|'('
name|'context'
op|','
name|'options'
op|')'
newline|'\n'
nl|'\n'
name|'vsa_id'
op|'='
name|'vsa_ref'
op|'['
string|"'id'"
op|']'
newline|'\n'
name|'vsa_name'
op|'='
name|'vsa_ref'
op|'['
string|"'name'"
op|']'
newline|'\n'
nl|'\n'
comment|'# check storage parameters'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'volume_params'
op|'='
name|'self'
op|'.'
name|'_check_storage_parameters'
op|'('
name|'context'
op|','
name|'vsa_name'
op|','
nl|'\n'
name|'storage'
op|','
name|'shared'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidVolumeType'
op|':'
newline|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'vsa_destroy'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
comment|'# after creating DB entry, re-check and set some defaults'
nl|'\n'
dedent|''
name|'updates'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'if'
op|'('
name|'not'
name|'hasattr'
op|'('
name|'vsa_ref'
op|','
string|"'display_name'"
op|')'
name|'or'
nl|'\n'
name|'vsa_ref'
op|'.'
name|'display_name'
name|'is'
name|'None'
name|'or'
nl|'\n'
name|'vsa_ref'
op|'.'
name|'display_name'
op|'=='
string|"''"
op|')'
op|':'
newline|'\n'
indent|'            '
name|'updates'
op|'['
string|"'display_name'"
op|']'
op|'='
name|'display_name'
op|'='
name|'vsa_name'
newline|'\n'
dedent|''
name|'updates'
op|'['
string|"'vol_count'"
op|']'
op|'='
name|'len'
op|'('
name|'volume_params'
op|')'
newline|'\n'
name|'vsa_ref'
op|'='
name|'self'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
op|'**'
name|'updates'
op|')'
newline|'\n'
nl|'\n'
comment|'# create volumes'
nl|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'vsa_multi_vol_creation'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'len'
op|'('
name|'volume_params'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'                '
name|'request_spec'
op|'='
op|'{'
nl|'\n'
string|"'num_volumes'"
op|':'
name|'len'
op|'('
name|'volume_params'
op|')'
op|','
nl|'\n'
string|"'vsa_id'"
op|':'
name|'str'
op|'('
name|'vsa_id'
op|')'
op|','
nl|'\n'
string|"'volumes'"
op|':'
name|'volume_params'
op|','
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'scheduler_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"create_volumes"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"topic"'
op|':'
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
nl|'\n'
string|'"request_spec"'
op|':'
name|'request_spec'
op|','
nl|'\n'
string|'"availability_zone"'
op|':'
name|'availability_zone'
op|'}'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# create BE volumes one-by-one'
nl|'\n'
indent|'            '
name|'for'
name|'vol'
name|'in'
name|'volume_params'
op|':'
newline|'\n'
indent|'                '
name|'try'
op|':'
newline|'\n'
indent|'                    '
name|'vol_name'
op|'='
name|'vol'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'vol_size'
op|'='
name|'vol'
op|'['
string|"'size'"
op|']'
newline|'\n'
name|'vol_type_id'
op|'='
name|'vol'
op|'['
string|"'volume_type_id'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)d %(vsa_name)s: Create "'
nl|'\n'
string|'"volume %(vol_name)s, %(vol_size)d GB, "'
nl|'\n'
string|'"type %(vol_type_id)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'vol_type'
op|'='
name|'volume_types'
op|'.'
name|'get_volume_type'
op|'('
name|'context'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'volume_type_id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'vol_ref'
op|'='
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'create'
op|'('
name|'context'
op|','
nl|'\n'
name|'vol_size'
op|','
nl|'\n'
name|'vol_name'
op|','
nl|'\n'
name|'vol'
op|'['
string|"'description'"
op|']'
op|','
nl|'\n'
name|'None'
op|','
nl|'\n'
name|'volume_type'
op|'='
name|'vol_type'
op|','
nl|'\n'
name|'metadata'
op|'='
name|'dict'
op|'('
name|'to_vsa_id'
op|'='
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
op|','
nl|'\n'
name|'availability_zone'
op|'='
name|'availability_zone'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'                    '
name|'self'
op|'.'
name|'update_vsa_status'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
nl|'\n'
name|'status'
op|'='
name|'VsaState'
op|'.'
name|'PARTIAL'
op|')'
newline|'\n'
name|'raise'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'if'
name|'len'
op|'('
name|'volume_params'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
comment|'# No BE volumes - ask VSA manager to start VCs'
nl|'\n'
indent|'            '
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'context'
op|','
nl|'\n'
name|'FLAGS'
op|'.'
name|'vsa_topic'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"create_vsa"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"vsa_id"'
op|':'
name|'str'
op|'('
name|'vsa_id'
op|')'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'vsa_ref'
newline|'\n'
nl|'\n'
DECL|member|update_vsa_status
dedent|''
name|'def'
name|'update_vsa_status'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa_id'
op|','
name|'status'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'updates'
op|'='
name|'dict'
op|'('
name|'status'
op|'='
name|'status'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)d: Update VSA status to %(status)s"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'return'
name|'self'
op|'.'
name|'update'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
op|'**'
name|'updates'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update
dedent|''
name|'def'
name|'update'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa_id'
op|','
op|'**'
name|'kwargs'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Updates the VSA instance in the datastore.\n\n        :param context: The security context\n        :param vsa_id: ID of the VSA instance to update\n        :param kwargs: All additional keyword args are treated\n                       as data fields of the instance to be\n                       updated\n\n        :returns: None\n        """'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)d: Update VSA call"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
name|'updatable_fields'
op|'='
op|'['
string|"'status'"
op|','
string|"'vc_count'"
op|','
string|"'vol_count'"
op|','
nl|'\n'
string|"'display_name'"
op|','
string|"'display_description'"
op|']'
newline|'\n'
name|'changes'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'field'
name|'in'
name|'updatable_fields'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'field'
name|'in'
name|'kwargs'
op|':'
newline|'\n'
indent|'                '
name|'changes'
op|'['
name|'field'
op|']'
op|'='
name|'kwargs'
op|'['
name|'field'
op|']'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'vc_count'
op|'='
name|'kwargs'
op|'.'
name|'get'
op|'('
string|"'vc_count'"
op|','
name|'None'
op|')'
newline|'\n'
name|'if'
name|'vc_count'
name|'is'
name|'not'
name|'None'
op|':'
newline|'\n'
comment|'# VP-TODO(vladimir.p):'
nl|'\n'
comment|'# This request may want to update number of VCs'
nl|'\n'
comment|'# Get number of current VCs and add/delete VCs appropriately'
nl|'\n'
indent|'            '
name|'vsa'
op|'='
name|'self'
op|'.'
name|'get'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
name|'vc_count'
op|'='
name|'int'
op|'('
name|'vc_count'
op|')'
newline|'\n'
name|'if'
name|'vc_count'
op|'>'
name|'FLAGS'
op|'.'
name|'max_vcs_in_vsa'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'warning'
op|'('
name|'_'
op|'('
string|'"Requested number of VCs (%d) is too high."'
nl|'\n'
string|'" Setting to default"'
op|')'
op|','
name|'vc_count'
op|')'
newline|'\n'
name|'vc_count'
op|'='
name|'FLAGS'
op|'.'
name|'max_vcs_in_vsa'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'vsa'
op|'['
string|"'vc_count'"
op|']'
op|'!='
name|'vc_count'
op|':'
newline|'\n'
indent|'                '
name|'self'
op|'.'
name|'update_num_vcs'
op|'('
name|'context'
op|','
name|'vsa'
op|','
name|'vc_count'
op|')'
newline|'\n'
name|'changes'
op|'['
string|"'vc_count'"
op|']'
op|'='
name|'vc_count'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'vsa_update'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
name|'changes'
op|')'
newline|'\n'
nl|'\n'
DECL|member|update_num_vcs
dedent|''
name|'def'
name|'update_num_vcs'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa'
op|','
name|'vc_count'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'vsa_name'
op|'='
name|'vsa'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'old_vc_count'
op|'='
name|'int'
op|'('
name|'vsa'
op|'['
string|"'vc_count'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'vc_count'
op|'>'
name|'old_vc_count'
op|':'
newline|'\n'
indent|'            '
name|'add_cnt'
op|'='
name|'vc_count'
op|'-'
name|'old_vc_count'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Adding %(add_cnt)s VCs to VSA %(vsa_name)s."'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# VP-TODO(vladimir.p): actual code for adding new VCs'
nl|'\n'
nl|'\n'
dedent|''
name|'elif'
name|'vc_count'
op|'<'
name|'old_vc_count'
op|':'
newline|'\n'
indent|'            '
name|'del_cnt'
op|'='
name|'old_vc_count'
op|'-'
name|'vc_count'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"Deleting %(del_cnt)s VCs from VSA %(vsa_name)s."'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
comment|'# VP-TODO(vladimir.p): actual code for deleting extra VCs'
nl|'\n'
nl|'\n'
DECL|member|_force_volume_delete
dedent|''
dedent|''
name|'def'
name|'_force_volume_delete'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Delete a volume, bypassing the check that it must be available."""'
newline|'\n'
name|'host'
op|'='
name|'volume'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'host'
op|':'
newline|'\n'
comment|'# Deleting volume from database and skipping rpc.'
nl|'\n'
indent|'            '
name|'self'
op|'.'
name|'db'
op|'.'
name|'volume_destroy'
op|'('
name|'ctxt'
op|','
name|'volume'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'return'
newline|'\n'
nl|'\n'
dedent|''
name|'rpc'
op|'.'
name|'cast'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'self'
op|'.'
name|'db'
op|'.'
name|'queue_get_for'
op|'('
name|'ctxt'
op|','
name|'FLAGS'
op|'.'
name|'volume_topic'
op|','
name|'host'
op|')'
op|','
nl|'\n'
op|'{'
string|'"method"'
op|':'
string|'"delete_volume"'
op|','
nl|'\n'
string|'"args"'
op|':'
op|'{'
string|'"volume_id"'
op|':'
name|'volume'
op|'['
string|"'id'"
op|']'
op|'}'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete_vsa_volumes
dedent|''
name|'def'
name|'delete_vsa_volumes'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'vsa_id'
op|','
name|'direction'
op|','
nl|'\n'
name|'force_delete'
op|'='
name|'True'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'direction'
op|'=='
string|'"FE"'
op|':'
newline|'\n'
indent|'            '
name|'volumes'
op|'='
name|'self'
op|'.'
name|'get_all_vsa_volumes'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'volumes'
op|'='
name|'self'
op|'.'
name|'get_all_vsa_drives'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'volume'
name|'in'
name|'volumes'
op|':'
newline|'\n'
indent|'            '
name|'try'
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
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)s: Deleting %(direction)s "'
nl|'\n'
string|'"volume %(vol_name)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'volume'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'InvalidVolume'
op|':'
newline|'\n'
indent|'                '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Unable to delete volume %s"'
op|')'
op|','
name|'volume'
op|'['
string|"'name'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'force_delete'
op|':'
newline|'\n'
indent|'                    '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)s: Forced delete. "'
nl|'\n'
string|'"%(direction)s volume %(vol_name)s"'
op|')'
op|','
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'_force_volume_delete'
op|'('
name|'context'
op|','
name|'volume'
op|')'
newline|'\n'
nl|'\n'
DECL|member|delete
dedent|''
dedent|''
dedent|''
dedent|''
name|'def'
name|'delete'
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
string|'"""Terminate a VSA instance."""'
newline|'\n'
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_'
op|'('
string|'"Going to try to terminate VSA ID %s"'
op|')'
op|','
name|'vsa_id'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete all FrontEnd and BackEnd volumes'
nl|'\n'
name|'self'
op|'.'
name|'delete_vsa_volumes'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
string|'"FE"'
op|','
name|'force_delete'
op|'='
name|'True'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'delete_vsa_volumes'
op|'('
name|'context'
op|','
name|'vsa_id'
op|','
string|'"BE"'
op|','
name|'force_delete'
op|'='
name|'True'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete all VC instances'
nl|'\n'
name|'instances'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'metadata'"
op|':'
name|'dict'
op|'('
name|'vsa_id'
op|'='
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
op|'}'
op|')'
newline|'\n'
name|'for'
name|'instance'
name|'in'
name|'instances'
op|':'
newline|'\n'
indent|'            '
name|'name'
op|'='
name|'instance'
op|'['
string|"'name'"
op|']'
newline|'\n'
name|'LOG'
op|'.'
name|'debug'
op|'('
name|'_'
op|'('
string|'"VSA ID %(vsa_id)s: Delete instance %(name)s"'
op|')'
op|','
nl|'\n'
name|'locals'
op|'('
op|')'
op|')'
newline|'\n'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'delete'
op|'('
name|'context'
op|','
name|'instance'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
comment|'# Delete VSA instance'
nl|'\n'
dedent|''
name|'self'
op|'.'
name|'db'
op|'.'
name|'vsa_destroy'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get
dedent|''
name|'def'
name|'get'
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
name|'rv'
op|'='
name|'self'
op|'.'
name|'db'
op|'.'
name|'vsa_get'
op|'('
name|'context'
op|','
name|'vsa_id'
op|')'
newline|'\n'
name|'return'
name|'rv'
newline|'\n'
nl|'\n'
DECL|member|get_all
dedent|''
name|'def'
name|'get_all'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'context'
op|'.'
name|'is_admin'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'vsa_get_all'
op|'('
name|'context'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'db'
op|'.'
name|'vsa_get_all_by_project'
op|'('
name|'context'
op|','
name|'context'
op|'.'
name|'project_id'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_vsa_volume_type
dedent|''
name|'def'
name|'get_vsa_volume_type'
op|'('
name|'self'
op|','
name|'context'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'name'
op|'='
name|'FLAGS'
op|'.'
name|'vsa_volume_type_name'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'vol_type'
op|'='
name|'volume_types'
op|'.'
name|'get_volume_type_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'            '
name|'volume_types'
op|'.'
name|'create'
op|'('
name|'context'
op|','
name|'name'
op|','
nl|'\n'
name|'extra_specs'
op|'='
name|'dict'
op|'('
name|'type'
op|'='
string|"'vsa_volume'"
op|')'
op|')'
newline|'\n'
name|'vol_type'
op|'='
name|'volume_types'
op|'.'
name|'get_volume_type_by_name'
op|'('
name|'context'
op|','
name|'name'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'vol_type'
newline|'\n'
nl|'\n'
DECL|member|get_all_vsa_instances
dedent|''
name|'def'
name|'get_all_vsa_instances'
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
name|'return'
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'metadata'"
op|':'
name|'dict'
op|'('
name|'vsa_id'
op|'='
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_vsa_volumes
dedent|''
name|'def'
name|'get_all_vsa_volumes'
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
name|'return'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'metadata'"
op|':'
name|'dict'
op|'('
name|'from_vsa_id'
op|'='
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
op|'}'
op|')'
newline|'\n'
nl|'\n'
DECL|member|get_all_vsa_drives
dedent|''
name|'def'
name|'get_all_vsa_drives'
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
name|'return'
name|'self'
op|'.'
name|'volume_api'
op|'.'
name|'get_all'
op|'('
name|'context'
op|','
nl|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'metadata'"
op|':'
name|'dict'
op|'('
name|'to_vsa_id'
op|'='
name|'str'
op|'('
name|'vsa_id'
op|')'
op|')'
op|'}'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
