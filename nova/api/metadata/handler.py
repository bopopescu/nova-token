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
string|'"""Metadata request handler."""'
newline|'\n'
nl|'\n'
name|'import'
name|'base64'
newline|'\n'
nl|'\n'
name|'import'
name|'webob'
op|'.'
name|'dec'
newline|'\n'
name|'import'
name|'webob'
op|'.'
name|'exc'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
op|'.'
name|'api'
op|'.'
name|'ec2'
name|'import'
name|'ec2utils'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'block_device'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'compute'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'db'
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
name|'import'
name|'network'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'volume'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'wsgi'
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
string|"'nova.api.metadata'"
op|')'
newline|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'use_forwarded_for'"
op|','
string|"'nova.api.auth'"
op|')'
newline|'\n'
name|'flags'
op|'.'
name|'DECLARE'
op|'('
string|"'dhcp_domain'"
op|','
string|"'nova.network.manager'"
op|')'
newline|'\n'
nl|'\n'
DECL|variable|_DEFAULT_MAPPINGS
name|'_DEFAULT_MAPPINGS'
op|'='
op|'{'
string|"'ami'"
op|':'
string|"'sda1'"
op|','
nl|'\n'
string|"'ephemeral0'"
op|':'
string|"'sda2'"
op|','
nl|'\n'
string|"'root'"
op|':'
name|'block_device'
op|'.'
name|'DEFAULT_ROOT_DEV_NAME'
op|','
nl|'\n'
string|"'swap'"
op|':'
string|"'sda3'"
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|Versions
name|'class'
name|'Versions'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
nl|'\n'
indent|'    '
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
string|'"""Respond to a request for all versions."""'
newline|'\n'
comment|'# available api versions'
nl|'\n'
name|'versions'
op|'='
op|'['
nl|'\n'
string|"'1.0'"
op|','
nl|'\n'
string|"'2007-01-19'"
op|','
nl|'\n'
string|"'2007-03-01'"
op|','
nl|'\n'
string|"'2007-08-29'"
op|','
nl|'\n'
string|"'2007-10-10'"
op|','
nl|'\n'
string|"'2007-12-15'"
op|','
nl|'\n'
string|"'2008-02-01'"
op|','
nl|'\n'
string|"'2008-09-01'"
op|','
nl|'\n'
string|"'2009-04-04'"
op|','
nl|'\n'
op|']'
newline|'\n'
name|'return'
string|"''"
op|'.'
name|'join'
op|'('
string|"'%s\\n'"
op|'%'
name|'v'
name|'for'
name|'v'
name|'in'
name|'versions'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|class|MetadataRequestHandler
dedent|''
dedent|''
name|'class'
name|'MetadataRequestHandler'
op|'('
name|'wsgi'
op|'.'
name|'Application'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Serve metadata."""'
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
name|'self'
op|'.'
name|'compute_api'
op|'='
name|'compute'
op|'.'
name|'API'
op|'('
nl|'\n'
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
op|','
nl|'\n'
name|'volume_api'
op|'='
name|'volume'
op|'.'
name|'API'
op|'('
op|')'
op|')'
newline|'\n'
nl|'\n'
DECL|member|_get_mpi_data
dedent|''
name|'def'
name|'_get_mpi_data'
op|'('
name|'self'
op|','
name|'context'
op|','
name|'project_id'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'result'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'project_id'"
op|':'
name|'project_id'
op|','
string|"'deleted'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'for'
name|'instance'
name|'in'
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
name|'search_opts'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'ip_info'
op|'='
name|'ec2utils'
op|'.'
name|'get_ip_info_for_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
comment|'# only look at ipv4 addresses'
nl|'\n'
name|'fixed_ips'
op|'='
name|'ip_info'
op|'['
string|"'fixed_ips'"
op|']'
newline|'\n'
name|'if'
name|'fixed_ips'
op|':'
newline|'\n'
indent|'                '
name|'line'
op|'='
string|"'%s slots=%d'"
op|'%'
op|'('
name|'fixed_ips'
op|'['
number|'0'
op|']'
op|','
name|'instance'
op|'['
string|"'vcpus'"
op|']'
op|')'
newline|'\n'
name|'key'
op|'='
name|'str'
op|'('
name|'instance'
op|'['
string|"'key_name'"
op|']'
op|')'
newline|'\n'
name|'if'
name|'key'
name|'in'
name|'result'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'['
name|'key'
op|']'
op|'.'
name|'append'
op|'('
name|'line'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                    '
name|'result'
op|'['
name|'key'
op|']'
op|'='
op|'['
name|'line'
op|']'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'result'
newline|'\n'
nl|'\n'
DECL|member|_format_instance_mapping
dedent|''
name|'def'
name|'_format_instance_mapping'
op|'('
name|'self'
op|','
name|'ctxt'
op|','
name|'instance_ref'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'root_device_name'
op|'='
name|'instance_ref'
op|'['
string|"'root_device_name'"
op|']'
newline|'\n'
name|'if'
name|'root_device_name'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'_DEFAULT_MAPPINGS'
newline|'\n'
nl|'\n'
dedent|''
name|'mappings'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'mappings'
op|'['
string|"'ami'"
op|']'
op|'='
name|'block_device'
op|'.'
name|'strip_dev'
op|'('
name|'root_device_name'
op|')'
newline|'\n'
name|'mappings'
op|'['
string|"'root'"
op|']'
op|'='
name|'root_device_name'
newline|'\n'
name|'default_local_device'
op|'='
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'default_local_device'"
op|')'
newline|'\n'
name|'if'
name|'default_local_device'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'['
string|"'ephemeral0'"
op|']'
op|'='
name|'default_local_device'
newline|'\n'
dedent|''
name|'default_swap_device'
op|'='
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'default_swap_device'"
op|')'
newline|'\n'
name|'if'
name|'default_swap_device'
op|':'
newline|'\n'
indent|'            '
name|'mappings'
op|'['
string|"'swap'"
op|']'
op|'='
name|'default_swap_device'
newline|'\n'
dedent|''
name|'ebs_devices'
op|'='
op|'['
op|']'
newline|'\n'
nl|'\n'
comment|"# 'ephemeralN', 'swap' and ebs"
nl|'\n'
name|'for'
name|'bdm'
name|'in'
name|'db'
op|'.'
name|'block_device_mapping_get_all_by_instance'
op|'('
nl|'\n'
name|'ctxt'
op|','
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'bdm'
op|'['
string|"'no_device'"
op|']'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
comment|'# ebs volume case'
nl|'\n'
dedent|''
name|'if'
op|'('
name|'bdm'
op|'['
string|"'volume_id'"
op|']'
name|'or'
name|'bdm'
op|'['
string|"'snapshot_id'"
op|']'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ebs_devices'
op|'.'
name|'append'
op|'('
name|'bdm'
op|'['
string|"'device_name'"
op|']'
op|')'
newline|'\n'
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'virtual_name'
op|'='
name|'bdm'
op|'['
string|"'virtual_name'"
op|']'
newline|'\n'
name|'if'
name|'not'
name|'virtual_name'
op|':'
newline|'\n'
indent|'                '
name|'continue'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'block_device'
op|'.'
name|'is_swap_or_ephemeral'
op|'('
name|'virtual_name'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'mappings'
op|'['
name|'virtual_name'
op|']'
op|'='
name|'bdm'
op|'['
string|"'device_name'"
op|']'
newline|'\n'
nl|'\n'
comment|"# NOTE(yamahata): I'm not sure how ebs device should be numbered."
nl|'\n'
comment|'#                 Right now sort by device name for deterministic'
nl|'\n'
comment|'#                 result.'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'ebs_devices'
op|':'
newline|'\n'
indent|'            '
name|'nebs'
op|'='
number|'0'
newline|'\n'
name|'ebs_devices'
op|'.'
name|'sort'
op|'('
op|')'
newline|'\n'
name|'for'
name|'ebs'
name|'in'
name|'ebs_devices'
op|':'
newline|'\n'
indent|'                '
name|'mappings'
op|'['
string|"'ebs%d'"
op|'%'
name|'nebs'
op|']'
op|'='
name|'ebs'
newline|'\n'
name|'nebs'
op|'+='
number|'1'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'return'
name|'mappings'
newline|'\n'
nl|'\n'
DECL|member|get_metadata
dedent|''
name|'def'
name|'get_metadata'
op|'('
name|'self'
op|','
name|'address'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
name|'search_opts'
op|'='
op|'{'
string|"'fixed_ip'"
op|':'
name|'address'
op|','
string|"'deleted'"
op|':'
name|'False'
op|'}'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'instance_ref'
op|'='
name|'self'
op|'.'
name|'compute_api'
op|'.'
name|'get_all'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'search_opts'
op|'='
name|'search_opts'
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
name|'instance_ref'
op|'='
name|'None'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'instance_ref'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'None'
newline|'\n'
nl|'\n'
comment|'# This ensures that all attributes of the instance'
nl|'\n'
comment|'# are populated.'
nl|'\n'
dedent|''
name|'instance_ref'
op|'='
name|'db'
op|'.'
name|'instance_get'
op|'('
name|'ctxt'
op|','
name|'instance_ref'
op|'['
number|'0'
op|']'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
nl|'\n'
name|'mpi'
op|'='
name|'self'
op|'.'
name|'_get_mpi_data'
op|'('
name|'ctxt'
op|','
name|'instance_ref'
op|'['
string|"'project_id'"
op|']'
op|')'
newline|'\n'
name|'hostname'
op|'='
string|'"%s.%s"'
op|'%'
op|'('
name|'instance_ref'
op|'['
string|"'hostname'"
op|']'
op|','
name|'FLAGS'
op|'.'
name|'dhcp_domain'
op|')'
newline|'\n'
name|'host'
op|'='
name|'instance_ref'
op|'['
string|"'host'"
op|']'
newline|'\n'
name|'services'
op|'='
name|'db'
op|'.'
name|'service_get_all_by_host'
op|'('
name|'ctxt'
op|'.'
name|'elevated'
op|'('
op|')'
op|','
name|'host'
op|')'
newline|'\n'
name|'availability_zone'
op|'='
name|'ec2utils'
op|'.'
name|'get_availability_zone_by_host'
op|'('
name|'services'
op|','
nl|'\n'
name|'host'
op|')'
newline|'\n'
nl|'\n'
name|'ip_info'
op|'='
name|'ec2utils'
op|'.'
name|'get_ip_info_for_instance'
op|'('
name|'ctxt'
op|','
name|'instance_ref'
op|')'
newline|'\n'
name|'floating_ips'
op|'='
name|'ip_info'
op|'['
string|"'floating_ips'"
op|']'
newline|'\n'
name|'floating_ip'
op|'='
name|'floating_ips'
name|'and'
name|'floating_ips'
op|'['
number|'0'
op|']'
name|'or'
string|"''"
newline|'\n'
nl|'\n'
name|'ec2_id'
op|'='
name|'ec2utils'
op|'.'
name|'id_to_ec2_id'
op|'('
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'image_ec2_id'
op|'='
name|'ec2utils'
op|'.'
name|'image_ec2_id'
op|'('
name|'instance_ref'
op|'['
string|"'image_ref'"
op|']'
op|')'
newline|'\n'
name|'security_groups'
op|'='
name|'db'
op|'.'
name|'security_group_get_by_instance'
op|'('
name|'ctxt'
op|','
nl|'\n'
name|'instance_ref'
op|'['
string|"'id'"
op|']'
op|')'
newline|'\n'
name|'security_groups'
op|'='
op|'['
name|'x'
op|'['
string|"'name'"
op|']'
name|'for'
name|'x'
name|'in'
name|'security_groups'
op|']'
newline|'\n'
name|'mappings'
op|'='
name|'self'
op|'.'
name|'_format_instance_mapping'
op|'('
name|'ctxt'
op|','
name|'instance_ref'
op|')'
newline|'\n'
name|'data'
op|'='
op|'{'
nl|'\n'
string|"'user-data'"
op|':'
name|'base64'
op|'.'
name|'b64decode'
op|'('
name|'instance_ref'
op|'['
string|"'user_data'"
op|']'
op|')'
op|','
nl|'\n'
string|"'meta-data'"
op|':'
op|'{'
nl|'\n'
string|"'ami-id'"
op|':'
name|'image_ec2_id'
op|','
nl|'\n'
string|"'ami-launch-index'"
op|':'
name|'instance_ref'
op|'['
string|"'launch_index'"
op|']'
op|','
nl|'\n'
string|"'ami-manifest-path'"
op|':'
string|"'FIXME'"
op|','
nl|'\n'
string|"'block-device-mapping'"
op|':'
name|'mappings'
op|','
nl|'\n'
string|"'hostname'"
op|':'
name|'hostname'
op|','
nl|'\n'
string|"'instance-action'"
op|':'
string|"'none'"
op|','
nl|'\n'
string|"'instance-id'"
op|':'
name|'ec2_id'
op|','
nl|'\n'
string|"'instance-type'"
op|':'
name|'instance_ref'
op|'['
string|"'instance_type'"
op|']'
op|'['
string|"'name'"
op|']'
op|','
nl|'\n'
string|"'local-hostname'"
op|':'
name|'hostname'
op|','
nl|'\n'
string|"'local-ipv4'"
op|':'
name|'address'
op|','
nl|'\n'
string|"'placement'"
op|':'
op|'{'
string|"'availability-zone'"
op|':'
name|'availability_zone'
op|'}'
op|','
nl|'\n'
string|"'public-hostname'"
op|':'
name|'hostname'
op|','
nl|'\n'
string|"'public-ipv4'"
op|':'
name|'floating_ip'
op|','
nl|'\n'
string|"'reservation-id'"
op|':'
name|'instance_ref'
op|'['
string|"'reservation_id'"
op|']'
op|','
nl|'\n'
string|"'security-groups'"
op|':'
name|'security_groups'
op|','
nl|'\n'
string|"'mpi'"
op|':'
name|'mpi'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
comment|'# public-keys should be in meta-data only if user specified one'
nl|'\n'
name|'if'
name|'instance_ref'
op|'['
string|"'key_name'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'meta-data'"
op|']'
op|'['
string|"'public-keys'"
op|']'
op|'='
op|'{'
nl|'\n'
string|"'0'"
op|':'
op|'{'
string|"'_name'"
op|':'
name|'instance_ref'
op|'['
string|"'key_name'"
op|']'
op|','
nl|'\n'
string|"'openssh-key'"
op|':'
name|'instance_ref'
op|'['
string|"'key_data'"
op|']'
op|'}'
op|'}'
newline|'\n'
nl|'\n'
dedent|''
name|'for'
name|'image_type'
name|'in'
op|'['
string|"'kernel'"
op|','
string|"'ramdisk'"
op|']'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'instance_ref'
op|'.'
name|'get'
op|'('
string|"'%s_id'"
op|'%'
name|'image_type'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'ec2_id'
op|'='
name|'ec2utils'
op|'.'
name|'image_ec2_id'
op|'('
nl|'\n'
name|'instance_ref'
op|'['
string|"'%s_id'"
op|'%'
name|'image_type'
op|']'
op|','
nl|'\n'
name|'ec2utils'
op|'.'
name|'image_type'
op|'('
name|'image_type'
op|')'
op|')'
newline|'\n'
name|'data'
op|'['
string|"'meta-data'"
op|']'
op|'['
string|"'%s-id'"
op|'%'
name|'image_type'
op|']'
op|'='
name|'ec2_id'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
name|'if'
name|'False'
op|':'
comment|'# TODO(vish): store ancestor ids'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'ancestor-ami-ids'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'if'
name|'False'
op|':'
comment|'# TODO(vish): store product codes'
newline|'\n'
indent|'            '
name|'data'
op|'['
string|"'product-codes'"
op|']'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
DECL|member|print_data
dedent|''
name|'def'
name|'print_data'
op|'('
name|'self'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'output'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'key'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'key'
op|'=='
string|"'_name'"
op|':'
newline|'\n'
indent|'                    '
name|'continue'
newline|'\n'
dedent|''
name|'output'
op|'+='
name|'key'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'if'
string|"'_name'"
name|'in'
name|'data'
op|'['
name|'key'
op|']'
op|':'
newline|'\n'
indent|'                        '
name|'output'
op|'+='
string|"'='"
op|'+'
name|'str'
op|'('
name|'data'
op|'['
name|'key'
op|']'
op|'['
string|"'_name'"
op|']'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                        '
name|'output'
op|'+='
string|"'/'"
newline|'\n'
dedent|''
dedent|''
name|'output'
op|'+='
string|"'\\n'"
newline|'\n'
comment|'# Cut off last \\n'
nl|'\n'
dedent|''
name|'return'
name|'output'
op|'['
op|':'
op|'-'
number|'1'
op|']'
newline|'\n'
dedent|''
name|'elif'
name|'isinstance'
op|'('
name|'data'
op|','
name|'list'
op|')'
op|':'
newline|'\n'
indent|'            '
name|'return'
string|"'\\n'"
op|'.'
name|'join'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'str'
op|'('
name|'data'
op|')'
newline|'\n'
nl|'\n'
DECL|member|lookup
dedent|''
dedent|''
name|'def'
name|'lookup'
op|'('
name|'self'
op|','
name|'path'
op|','
name|'data'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'items'
op|'='
name|'path'
op|'.'
name|'split'
op|'('
string|"'/'"
op|')'
newline|'\n'
name|'for'
name|'item'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'item'
op|':'
newline|'\n'
indent|'                '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'data'
op|','
name|'dict'
op|')'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'data'
newline|'\n'
dedent|''
name|'if'
name|'not'
name|'item'
name|'in'
name|'data'
op|':'
newline|'\n'
indent|'                    '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'data'
op|'['
name|'item'
op|']'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'data'
newline|'\n'
nl|'\n'
dedent|''
op|'@'
name|'webob'
op|'.'
name|'dec'
op|'.'
name|'wsgify'
op|'('
name|'RequestClass'
op|'='
name|'wsgi'
op|'.'
name|'Request'
op|')'
newline|'\n'
DECL|member|__call__
name|'def'
name|'__call__'
op|'('
name|'self'
op|','
name|'req'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'remote_addr'
newline|'\n'
name|'if'
name|'FLAGS'
op|'.'
name|'use_forwarded_for'
op|':'
newline|'\n'
indent|'            '
name|'remote_address'
op|'='
name|'req'
op|'.'
name|'headers'
op|'.'
name|'get'
op|'('
string|"'X-Forwarded-For'"
op|','
name|'remote_address'
op|')'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'meta_data'
op|'='
name|'self'
op|'.'
name|'get_metadata'
op|'('
name|'remote_address'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'Exception'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'exception'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|')'
op|','
nl|'\n'
name|'remote_address'
op|')'
newline|'\n'
name|'msg'
op|'='
name|'_'
op|'('
string|"'An unknown error has occurred. '"
nl|'\n'
string|"'Please try your request again.'"
op|')'
newline|'\n'
name|'exc'
op|'='
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPInternalServerError'
op|'('
name|'explanation'
op|'='
name|'unicode'
op|'('
name|'msg'
op|')'
op|')'
newline|'\n'
name|'return'
name|'exc'
newline|'\n'
dedent|''
name|'if'
name|'meta_data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'LOG'
op|'.'
name|'error'
op|'('
name|'_'
op|'('
string|"'Failed to get metadata for ip: %s'"
op|')'
op|','
name|'remote_address'
op|')'
newline|'\n'
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'data'
op|'='
name|'self'
op|'.'
name|'lookup'
op|'('
name|'req'
op|'.'
name|'path_info'
op|','
name|'meta_data'
op|')'
newline|'\n'
name|'if'
name|'data'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'raise'
name|'webob'
op|'.'
name|'exc'
op|'.'
name|'HTTPNotFound'
op|'('
op|')'
newline|'\n'
dedent|''
name|'return'
name|'self'
op|'.'
name|'print_data'
op|'('
name|'data'
op|')'
newline|'\n'
dedent|''
dedent|''
endmarker|''
end_unit
