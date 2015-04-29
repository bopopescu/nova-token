begin_unit
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
name|'import'
name|'functools'
newline|'\n'
name|'import'
name|'re'
newline|'\n'
nl|'\n'
name|'from'
name|'oslo_log'
name|'import'
name|'log'
name|'as'
name|'logging'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'timeutils'
newline|'\n'
name|'from'
name|'oslo_utils'
name|'import'
name|'uuidutils'
newline|'\n'
nl|'\n'
name|'from'
name|'nova'
name|'import'
name|'context'
newline|'\n'
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
name|'_LI'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'network'
name|'import'
name|'model'
name|'as'
name|'network_model'
newline|'\n'
name|'from'
name|'nova'
name|'import'
name|'objects'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'objects'
name|'import'
name|'base'
name|'as'
name|'obj_base'
newline|'\n'
name|'from'
name|'nova'
op|'.'
name|'openstack'
op|'.'
name|'common'
name|'import'
name|'memorycache'
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
comment|'# NOTE(vish): cache mapping for one week'
nl|'\n'
DECL|variable|_CACHE_TIME
name|'_CACHE_TIME'
op|'='
number|'7'
op|'*'
number|'24'
op|'*'
number|'60'
op|'*'
number|'60'
newline|'\n'
DECL|variable|_CACHE
name|'_CACHE'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|memoize
name|'def'
name|'memoize'
op|'('
name|'func'
op|')'
op|':'
newline|'\n'
indent|'    '
op|'@'
name|'functools'
op|'.'
name|'wraps'
op|'('
name|'func'
op|')'
newline|'\n'
DECL|function|memoizer
name|'def'
name|'memoizer'
op|'('
name|'context'
op|','
name|'reqid'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'global'
name|'_CACHE'
newline|'\n'
name|'if'
name|'not'
name|'_CACHE'
op|':'
newline|'\n'
indent|'            '
name|'_CACHE'
op|'='
name|'memorycache'
op|'.'
name|'get_client'
op|'('
op|')'
newline|'\n'
dedent|''
name|'key'
op|'='
string|'"%s:%s"'
op|'%'
op|'('
name|'func'
op|'.'
name|'__name__'
op|','
name|'reqid'
op|')'
newline|'\n'
name|'key'
op|'='
name|'str'
op|'('
name|'key'
op|')'
newline|'\n'
name|'value'
op|'='
name|'_CACHE'
op|'.'
name|'get'
op|'('
name|'key'
op|')'
newline|'\n'
name|'if'
name|'value'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'            '
name|'value'
op|'='
name|'func'
op|'('
name|'context'
op|','
name|'reqid'
op|')'
newline|'\n'
name|'_CACHE'
op|'.'
name|'set'
op|'('
name|'key'
op|','
name|'value'
op|','
name|'time'
op|'='
name|'_CACHE_TIME'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'value'
newline|'\n'
dedent|''
name|'return'
name|'memoizer'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|reset_cache
dedent|''
name|'def'
name|'reset_cache'
op|'('
op|')'
op|':'
newline|'\n'
indent|'    '
name|'global'
name|'_CACHE'
newline|'\n'
name|'_CACHE'
op|'='
name|'None'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|image_type
dedent|''
name|'def'
name|'image_type'
op|'('
name|'image_type'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Converts to a three letter image type.\n\n    aki, kernel => aki\n    ari, ramdisk => ari\n    anything else => ami\n\n    """'
newline|'\n'
name|'if'
name|'image_type'
op|'=='
string|"'kernel'"
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'aki'"
newline|'\n'
dedent|''
name|'if'
name|'image_type'
op|'=='
string|"'ramdisk'"
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'ari'"
newline|'\n'
dedent|''
name|'if'
name|'image_type'
name|'not'
name|'in'
op|'['
string|"'aki'"
op|','
string|"'ari'"
op|']'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"'ami'"
newline|'\n'
dedent|''
name|'return'
name|'image_type'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|resource_type_from_id
dedent|''
name|'def'
name|'resource_type_from_id'
op|'('
name|'context'
op|','
name|'resource_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get resource type by ID\n\n    Returns a string representation of the Amazon resource type, if known.\n    Returns None on failure.\n\n    :param context: context under which the method is called\n    :param resource_id: resource_id to evaluate\n    """'
newline|'\n'
nl|'\n'
name|'known_types'
op|'='
op|'{'
nl|'\n'
string|"'i'"
op|':'
string|"'instance'"
op|','
nl|'\n'
string|"'r'"
op|':'
string|"'reservation'"
op|','
nl|'\n'
string|"'vol'"
op|':'
string|"'volume'"
op|','
nl|'\n'
string|"'snap'"
op|':'
string|"'snapshot'"
op|','
nl|'\n'
string|"'ami'"
op|':'
string|"'image'"
op|','
nl|'\n'
string|"'aki'"
op|':'
string|"'image'"
op|','
nl|'\n'
string|"'ari'"
op|':'
string|"'image'"
nl|'\n'
op|'}'
newline|'\n'
nl|'\n'
name|'type_marker'
op|'='
name|'resource_id'
op|'.'
name|'split'
op|'('
string|"'-'"
op|')'
op|'['
number|'0'
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'known_types'
op|'.'
name|'get'
op|'('
name|'type_marker'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'memoize'
newline|'\n'
DECL|function|id_to_glance_id
name|'def'
name|'id_to_glance_id'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert an internal (db) id to a glance id."""'
newline|'\n'
name|'return'
name|'objects'
op|'.'
name|'S3ImageMapping'
op|'.'
name|'get_by_id'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'memoize'
newline|'\n'
DECL|function|glance_id_to_id
name|'def'
name|'glance_id_to_id'
op|'('
name|'context'
op|','
name|'glance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert a glance id to an internal (db) id."""'
newline|'\n'
name|'if'
name|'not'
name|'glance_id'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'objects'
op|'.'
name|'S3ImageMapping'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'glance_id'
op|')'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'s3imap'
op|'='
name|'objects'
op|'.'
name|'S3ImageMapping'
op|'('
name|'context'
op|','
name|'uuid'
op|'='
name|'glance_id'
op|')'
newline|'\n'
name|'s3imap'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'return'
name|'s3imap'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ec2_id_to_glance_id
dedent|''
dedent|''
name|'def'
name|'ec2_id_to_glance_id'
op|'('
name|'context'
op|','
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'image_id'
op|'='
name|'ec2_id_to_id'
op|'('
name|'ec2_id'
op|')'
newline|'\n'
name|'return'
name|'id_to_glance_id'
op|'('
name|'context'
op|','
name|'image_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|glance_id_to_ec2_id
dedent|''
name|'def'
name|'glance_id_to_ec2_id'
op|'('
name|'context'
op|','
name|'glance_id'
op|','
name|'image_type'
op|'='
string|"'ami'"
op|')'
op|':'
newline|'\n'
indent|'    '
name|'image_id'
op|'='
name|'glance_id_to_id'
op|'('
name|'context'
op|','
name|'glance_id'
op|')'
newline|'\n'
name|'if'
name|'image_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'return'
name|'image_ec2_id'
op|'('
name|'image_id'
op|','
name|'image_type'
op|'='
name|'image_type'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ec2_id_to_id
dedent|''
name|'def'
name|'ec2_id_to_id'
op|'('
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert an ec2 ID (i-[base 16 number]) to an instance id (int)."""'
newline|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'ec2_id'
op|'.'
name|'split'
op|'('
string|"'-'"
op|')'
op|'['
op|'-'
number|'1'
op|']'
op|','
number|'16'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'raise'
name|'exception'
op|'.'
name|'InvalidEc2Id'
op|'('
name|'ec2_id'
op|'='
name|'ec2_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|image_ec2_id
dedent|''
dedent|''
name|'def'
name|'image_ec2_id'
op|'('
name|'image_id'
op|','
name|'image_type'
op|'='
string|"'ami'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Returns image ec2_id using id and three letter type."""'
newline|'\n'
name|'template'
op|'='
name|'image_type'
op|'+'
string|"'-%08x'"
newline|'\n'
name|'return'
name|'id_to_ec2_id'
op|'('
name|'image_id'
op|','
name|'template'
op|'='
name|'template'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ip_info_for_instance_from_nw_info
dedent|''
name|'def'
name|'get_ip_info_for_instance_from_nw_info'
op|'('
name|'nw_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'not'
name|'isinstance'
op|'('
name|'nw_info'
op|','
name|'network_model'
op|'.'
name|'NetworkInfo'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nw_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'nw_info'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'ip_info'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'fixed_ips'
op|'='
name|'nw_info'
op|'.'
name|'fixed_ips'
op|'('
op|')'
newline|'\n'
name|'ip_info'
op|'['
string|"'fixed_ips'"
op|']'
op|'='
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'ip'
name|'in'
name|'fixed_ips'
nl|'\n'
name|'if'
name|'ip'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|']'
newline|'\n'
name|'ip_info'
op|'['
string|"'fixed_ip6s'"
op|']'
op|'='
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'ip'
name|'in'
name|'fixed_ips'
nl|'\n'
name|'if'
name|'ip'
op|'['
string|"'version'"
op|']'
op|'=='
number|'6'
op|']'
newline|'\n'
name|'ip_info'
op|'['
string|"'floating_ips'"
op|']'
op|'='
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
name|'for'
name|'ip'
name|'in'
name|'nw_info'
op|'.'
name|'floating_ips'
op|'('
op|')'
op|']'
newline|'\n'
nl|'\n'
name|'return'
name|'ip_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ip_info_for_instance
dedent|''
name|'def'
name|'get_ip_info_for_instance'
op|'('
name|'context'
op|','
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a dictionary of IP information for an instance."""'
newline|'\n'
nl|'\n'
name|'if'
name|'isinstance'
op|'('
name|'instance'
op|','
name|'obj_base'
op|'.'
name|'NovaObject'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'nw_info'
op|'='
name|'instance'
op|'.'
name|'info_cache'
op|'.'
name|'network_info'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
comment|'# FIXME(comstud): Temporary as we transition to objects.'
nl|'\n'
indent|'        '
name|'info_cache'
op|'='
name|'instance'
op|'.'
name|'info_cache'
name|'or'
op|'{'
op|'}'
newline|'\n'
name|'nw_info'
op|'='
name|'info_cache'
op|'.'
name|'get'
op|'('
string|"'network_info'"
op|')'
newline|'\n'
comment|'# Make sure empty response is turned into the model'
nl|'\n'
dedent|''
name|'if'
name|'not'
name|'nw_info'
op|':'
newline|'\n'
indent|'        '
name|'nw_info'
op|'='
op|'['
op|']'
newline|'\n'
dedent|''
name|'return'
name|'get_ip_info_for_instance_from_nw_info'
op|'('
name|'nw_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|id_to_ec2_id
dedent|''
name|'def'
name|'id_to_ec2_id'
op|'('
name|'instance_id'
op|','
name|'template'
op|'='
string|"'i-%08x'"
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert an instance ID (int) to an ec2 ID (i-[base 16 number])."""'
newline|'\n'
name|'return'
name|'template'
op|'%'
name|'int'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|id_to_ec2_inst_id
dedent|''
name|'def'
name|'id_to_ec2_inst_id'
op|'('
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get or create an ec2 instance ID (i-[base 16 number]) from uuid."""'
newline|'\n'
name|'if'
name|'instance_id'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'elif'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'instance_id'
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
name|'int_id'
op|'='
name|'get_int_id_from_instance_uuid'
op|'('
name|'ctxt'
op|','
name|'instance_id'
op|')'
newline|'\n'
name|'return'
name|'id_to_ec2_id'
op|'('
name|'int_id'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'id_to_ec2_id'
op|'('
name|'instance_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ec2_inst_id_to_uuid
dedent|''
dedent|''
name|'def'
name|'ec2_inst_id_to_uuid'
op|'('
name|'context'
op|','
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'""""Convert an instance id to uuid."""'
newline|'\n'
name|'int_id'
op|'='
name|'ec2_id_to_id'
op|'('
name|'ec2_id'
op|')'
newline|'\n'
name|'return'
name|'get_instance_uuid_from_int_id'
op|'('
name|'context'
op|','
name|'int_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'memoize'
newline|'\n'
DECL|function|get_instance_uuid_from_int_id
name|'def'
name|'get_instance_uuid_from_int_id'
op|'('
name|'context'
op|','
name|'int_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'imap'
op|'='
name|'objects'
op|'.'
name|'EC2InstanceMapping'
op|'.'
name|'get_by_id'
op|'('
name|'context'
op|','
name|'int_id'
op|')'
newline|'\n'
name|'return'
name|'imap'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|id_to_ec2_snap_id
dedent|''
name|'def'
name|'id_to_ec2_snap_id'
op|'('
name|'snapshot_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get or create an ec2 volume ID (vol-[base 16 number]) from uuid."""'
newline|'\n'
name|'if'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'snapshot_id'
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
name|'int_id'
op|'='
name|'get_int_id_from_snapshot_uuid'
op|'('
name|'ctxt'
op|','
name|'snapshot_id'
op|')'
newline|'\n'
name|'return'
name|'id_to_ec2_id'
op|'('
name|'int_id'
op|','
string|"'snap-%08x'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'id_to_ec2_id'
op|'('
name|'snapshot_id'
op|','
string|"'snap-%08x'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|id_to_ec2_vol_id
dedent|''
dedent|''
name|'def'
name|'id_to_ec2_vol_id'
op|'('
name|'volume_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get or create an ec2 volume ID (vol-[base 16 number]) from uuid."""'
newline|'\n'
name|'if'
name|'uuidutils'
op|'.'
name|'is_uuid_like'
op|'('
name|'volume_id'
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
name|'int_id'
op|'='
name|'get_int_id_from_volume_uuid'
op|'('
name|'ctxt'
op|','
name|'volume_id'
op|')'
newline|'\n'
name|'return'
name|'id_to_ec2_id'
op|'('
name|'int_id'
op|','
string|"'vol-%08x'"
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'id_to_ec2_id'
op|'('
name|'volume_id'
op|','
string|"'vol-%08x'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ec2_vol_id_to_uuid
dedent|''
dedent|''
name|'def'
name|'ec2_vol_id_to_uuid'
op|'('
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the corresponding UUID for the given ec2-id."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(jgriffith) first strip prefix to get just the numeric'
nl|'\n'
name|'int_id'
op|'='
name|'ec2_id_to_id'
op|'('
name|'ec2_id'
op|')'
newline|'\n'
name|'return'
name|'get_volume_uuid_from_int_id'
op|'('
name|'ctxt'
op|','
name|'int_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_ms_time_regex
dedent|''
name|'_ms_time_regex'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'^\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}\\.\\d{3,6}Z$'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|status_to_ec2_attach_status
name|'def'
name|'status_to_ec2_attach_status'
op|'('
name|'volume'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the corresponding EC2 attachment state.\n\n    According to EC2 API, the valid attachment status in response is:\n    attaching | attached | detaching | detached\n    """'
newline|'\n'
name|'volume_status'
op|'='
name|'volume'
op|'.'
name|'get'
op|'('
string|"'status'"
op|')'
newline|'\n'
name|'attach_status'
op|'='
name|'volume'
op|'.'
name|'get'
op|'('
string|"'attach_status'"
op|')'
newline|'\n'
name|'if'
name|'volume_status'
name|'in'
op|'('
string|"'attaching'"
op|','
string|"'detaching'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ec2_attach_status'
op|'='
name|'volume_status'
newline|'\n'
dedent|''
name|'elif'
name|'attach_status'
name|'in'
op|'('
string|"'attached'"
op|','
string|"'detached'"
op|')'
op|':'
newline|'\n'
indent|'        '
name|'ec2_attach_status'
op|'='
name|'attach_status'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'        '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Unacceptable attach status:%s for ec2 API."'
op|')'
op|'%'
name|'attach_status'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'Invalid'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'return'
name|'ec2_attach_status'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|is_ec2_timestamp_expired
dedent|''
name|'def'
name|'is_ec2_timestamp_expired'
op|'('
name|'request'
op|','
name|'expires'
op|'='
name|'None'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Checks the timestamp or expiry time included in an EC2 request\n    and returns true if the request is expired\n    """'
newline|'\n'
name|'timestamp'
op|'='
name|'request'
op|'.'
name|'get'
op|'('
string|"'Timestamp'"
op|')'
newline|'\n'
name|'expiry_time'
op|'='
name|'request'
op|'.'
name|'get'
op|'('
string|"'Expires'"
op|')'
newline|'\n'
nl|'\n'
DECL|function|parse_strtime
name|'def'
name|'parse_strtime'
op|'('
name|'strtime'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'_ms_time_regex'
op|'.'
name|'match'
op|'('
name|'strtime'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(MotoKen): time format for aws-sdk-java contains millisecond'
nl|'\n'
indent|'            '
name|'time_format'
op|'='
string|'"%Y-%m-%dT%H:%M:%S.%fZ"'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'time_format'
op|'='
string|'"%Y-%m-%dT%H:%M:%SZ"'
newline|'\n'
dedent|''
name|'return'
name|'timeutils'
op|'.'
name|'parse_strtime'
op|'('
name|'strtime'
op|','
name|'time_format'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'timestamp'
name|'and'
name|'expiry_time'
op|':'
newline|'\n'
indent|'            '
name|'msg'
op|'='
name|'_'
op|'('
string|'"Request must include either Timestamp or Expires,"'
nl|'\n'
string|'" but cannot contain both"'
op|')'
newline|'\n'
name|'LOG'
op|'.'
name|'error'
op|'('
name|'msg'
op|')'
newline|'\n'
name|'raise'
name|'exception'
op|'.'
name|'InvalidRequest'
op|'('
name|'msg'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'expiry_time'
op|':'
newline|'\n'
indent|'            '
name|'query_time'
op|'='
name|'parse_strtime'
op|'('
name|'expiry_time'
op|')'
newline|'\n'
name|'return'
name|'timeutils'
op|'.'
name|'is_older_than'
op|'('
name|'query_time'
op|','
op|'-'
number|'1'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'timestamp'
op|':'
newline|'\n'
indent|'            '
name|'query_time'
op|'='
name|'parse_strtime'
op|'('
name|'timestamp'
op|')'
newline|'\n'
nl|'\n'
comment|'# Check if the difference between the timestamp in the request'
nl|'\n'
comment|'# and the time on our servers is larger than 5 minutes, the'
nl|'\n'
comment|'# request is too old (or too new).'
nl|'\n'
name|'if'
name|'query_time'
name|'and'
name|'expires'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'timeutils'
op|'.'
name|'is_older_than'
op|'('
name|'query_time'
op|','
name|'expires'
op|')'
name|'or'
name|'timeutils'
op|'.'
name|'is_newer_than'
op|'('
name|'query_time'
op|','
name|'expires'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'LOG'
op|'.'
name|'info'
op|'('
name|'_LI'
op|'('
string|'"Timestamp is invalid."'
op|')'
op|')'
newline|'\n'
name|'return'
name|'True'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'memoize'
newline|'\n'
DECL|function|get_int_id_from_instance_uuid
name|'def'
name|'get_int_id_from_instance_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'instance_uuid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'imap'
op|'='
name|'objects'
op|'.'
name|'EC2InstanceMapping'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'instance_uuid'
op|')'
newline|'\n'
name|'return'
name|'imap'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'imap'
op|'='
name|'objects'
op|'.'
name|'EC2InstanceMapping'
op|'('
name|'context'
op|')'
newline|'\n'
name|'imap'
op|'.'
name|'uuid'
op|'='
name|'instance_uuid'
newline|'\n'
name|'imap'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'return'
name|'imap'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'memoize'
newline|'\n'
DECL|function|get_int_id_from_volume_uuid
name|'def'
name|'get_int_id_from_volume_uuid'
op|'('
name|'context'
op|','
name|'volume_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'volume_uuid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'vmap'
op|'='
name|'objects'
op|'.'
name|'EC2VolumeMapping'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'volume_uuid'
op|')'
newline|'\n'
name|'return'
name|'vmap'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'vmap'
op|'='
name|'objects'
op|'.'
name|'EC2VolumeMapping'
op|'('
name|'context'
op|')'
newline|'\n'
name|'vmap'
op|'.'
name|'uuid'
op|'='
name|'volume_uuid'
newline|'\n'
name|'vmap'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'return'
name|'vmap'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'memoize'
newline|'\n'
DECL|function|get_volume_uuid_from_int_id
name|'def'
name|'get_volume_uuid_from_int_id'
op|'('
name|'context'
op|','
name|'int_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'vmap'
op|'='
name|'objects'
op|'.'
name|'EC2VolumeMapping'
op|'.'
name|'get_by_id'
op|'('
name|'context'
op|','
name|'int_id'
op|')'
newline|'\n'
name|'return'
name|'vmap'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|ec2_snap_id_to_uuid
dedent|''
name|'def'
name|'ec2_snap_id_to_uuid'
op|'('
name|'ec2_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Get the corresponding UUID for the given ec2-id."""'
newline|'\n'
name|'ctxt'
op|'='
name|'context'
op|'.'
name|'get_admin_context'
op|'('
op|')'
newline|'\n'
nl|'\n'
comment|'# NOTE(jgriffith) first strip prefix to get just the numeric'
nl|'\n'
name|'int_id'
op|'='
name|'ec2_id_to_id'
op|'('
name|'ec2_id'
op|')'
newline|'\n'
name|'return'
name|'get_snapshot_uuid_from_int_id'
op|'('
name|'ctxt'
op|','
name|'int_id'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
op|'@'
name|'memoize'
newline|'\n'
DECL|function|get_int_id_from_snapshot_uuid
name|'def'
name|'get_int_id_from_snapshot_uuid'
op|'('
name|'context'
op|','
name|'snapshot_uuid'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'snapshot_uuid'
name|'is'
name|'None'
op|':'
newline|'\n'
indent|'        '
name|'return'
newline|'\n'
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'smap'
op|'='
name|'objects'
op|'.'
name|'EC2SnapshotMapping'
op|'.'
name|'get_by_uuid'
op|'('
name|'context'
op|','
name|'snapshot_uuid'
op|')'
newline|'\n'
name|'return'
name|'smap'
op|'.'
name|'id'
newline|'\n'
dedent|''
name|'except'
name|'exception'
op|'.'
name|'NotFound'
op|':'
newline|'\n'
indent|'        '
name|'smap'
op|'='
name|'objects'
op|'.'
name|'EC2SnapshotMapping'
op|'('
name|'context'
op|','
name|'uuid'
op|'='
name|'snapshot_uuid'
op|')'
newline|'\n'
name|'smap'
op|'.'
name|'create'
op|'('
op|')'
newline|'\n'
name|'return'
name|'smap'
op|'.'
name|'id'
newline|'\n'
nl|'\n'
nl|'\n'
dedent|''
dedent|''
op|'@'
name|'memoize'
newline|'\n'
DECL|function|get_snapshot_uuid_from_int_id
name|'def'
name|'get_snapshot_uuid_from_int_id'
op|'('
name|'context'
op|','
name|'int_id'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'smap'
op|'='
name|'objects'
op|'.'
name|'EC2SnapshotMapping'
op|'.'
name|'get_by_id'
op|'('
name|'context'
op|','
name|'int_id'
op|')'
newline|'\n'
name|'return'
name|'smap'
op|'.'
name|'uuid'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|variable|_c2u
dedent|''
name|'_c2u'
op|'='
name|'re'
op|'.'
name|'compile'
op|'('
string|"'(((?<=[a-z])[A-Z])|([A-Z](?![A-Z]|$)))'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|camelcase_to_underscore
name|'def'
name|'camelcase_to_underscore'
op|'('
name|'str'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
name|'_c2u'
op|'.'
name|'sub'
op|'('
string|"r'_\\1'"
op|','
name|'str'
op|')'
op|'.'
name|'lower'
op|'('
op|')'
op|'.'
name|'strip'
op|'('
string|"'_'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|_try_convert
dedent|''
name|'def'
name|'_try_convert'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Return a non-string from a string or unicode, if possible.\n\n    ============= =====================================================\n    When value is returns\n    ============= =====================================================\n    zero-length   \'\'\n    \'None\'        None\n    \'True\'        True case insensitive\n    \'False\'       False case insensitive\n    \'0\', \'-0\'     0\n    0xN, -0xN     int from hex (positive) (N is any number)\n    0bN, -0bN     int from binary (positive) (N is any number)\n    *             try conversion to int, float, complex, fallback value\n\n    """'
newline|'\n'
DECL|function|_negative_zero
name|'def'
name|'_negative_zero'
op|'('
name|'value'
op|')'
op|':'
newline|'\n'
indent|'        '
name|'epsilon'
op|'='
number|'1e-7'
newline|'\n'
name|'return'
number|'0'
name|'if'
name|'abs'
op|'('
name|'value'
op|')'
op|'<'
name|'epsilon'
name|'else'
name|'value'
newline|'\n'
nl|'\n'
dedent|''
name|'if'
name|'len'
op|'('
name|'value'
op|')'
op|'=='
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'return'
string|"''"
newline|'\n'
dedent|''
name|'if'
name|'value'
op|'=='
string|"'None'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'None'
newline|'\n'
dedent|''
name|'lowered_value'
op|'='
name|'value'
op|'.'
name|'lower'
op|'('
op|')'
newline|'\n'
name|'if'
name|'lowered_value'
op|'=='
string|"'true'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'True'
newline|'\n'
dedent|''
name|'if'
name|'lowered_value'
op|'=='
string|"'false'"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'False'
newline|'\n'
dedent|''
name|'for'
name|'prefix'
op|','
name|'base'
name|'in'
op|'['
op|'('
string|"'0x'"
op|','
number|'16'
op|')'
op|','
op|'('
string|"'0b'"
op|','
number|'2'
op|')'
op|','
op|'('
string|"'0'"
op|','
number|'8'
op|')'
op|','
op|'('
string|"''"
op|','
number|'10'
op|')'
op|']'
op|':'
newline|'\n'
indent|'        '
name|'try'
op|':'
newline|'\n'
indent|'            '
name|'if'
name|'lowered_value'
op|'.'
name|'startswith'
op|'('
op|'('
name|'prefix'
op|','
string|'"-"'
op|'+'
name|'prefix'
op|')'
op|')'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'int'
op|'('
name|'lowered_value'
op|','
name|'base'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'            '
name|'pass'
newline|'\n'
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'_negative_zero'
op|'('
name|'float'
op|'('
name|'value'
op|')'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|dict_from_dotted_str
dedent|''
dedent|''
name|'def'
name|'dict_from_dotted_str'
op|'('
name|'items'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""parse multi dot-separated argument into dict.\n    EBS boot uses multi dot-separated arguments like\n    BlockDeviceMapping.1.DeviceName=snap-id\n    Convert the above into\n    {\'block_device_mapping\': {\'1\': {\'device_name\': snap-id}}}\n    """'
newline|'\n'
name|'args'
op|'='
op|'{'
op|'}'
newline|'\n'
name|'for'
name|'key'
op|','
name|'value'
name|'in'
name|'items'
op|':'
newline|'\n'
indent|'        '
name|'parts'
op|'='
name|'key'
op|'.'
name|'split'
op|'('
string|'"."'
op|')'
newline|'\n'
name|'key'
op|'='
name|'str'
op|'('
name|'camelcase_to_underscore'
op|'('
name|'parts'
op|'['
number|'0'
op|']'
op|')'
op|')'
newline|'\n'
name|'if'
name|'isinstance'
op|'('
name|'value'
op|','
name|'str'
op|')'
name|'or'
name|'isinstance'
op|'('
name|'value'
op|','
name|'unicode'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(vish): Automatically convert strings back'
nl|'\n'
comment|'#             into their respective values'
nl|'\n'
indent|'            '
name|'value'
op|'='
name|'_try_convert'
op|'('
name|'value'
op|')'
newline|'\n'
nl|'\n'
name|'if'
name|'len'
op|'('
name|'parts'
op|')'
op|'>'
number|'1'
op|':'
newline|'\n'
indent|'                '
name|'d'
op|'='
name|'args'
op|'.'
name|'get'
op|'('
name|'key'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'args'
op|'['
name|'key'
op|']'
op|'='
name|'d'
newline|'\n'
name|'for'
name|'k'
name|'in'
name|'parts'
op|'['
number|'1'
op|':'
op|'-'
number|'1'
op|']'
op|':'
newline|'\n'
indent|'                    '
name|'k'
op|'='
name|'camelcase_to_underscore'
op|'('
name|'k'
op|')'
newline|'\n'
name|'v'
op|'='
name|'d'
op|'.'
name|'get'
op|'('
name|'k'
op|','
op|'{'
op|'}'
op|')'
newline|'\n'
name|'d'
op|'['
name|'k'
op|']'
op|'='
name|'v'
newline|'\n'
name|'d'
op|'='
name|'v'
newline|'\n'
dedent|''
name|'d'
op|'['
name|'camelcase_to_underscore'
op|'('
name|'parts'
op|'['
op|'-'
number|'1'
op|']'
op|')'
op|']'
op|'='
name|'value'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'args'
op|'['
name|'key'
op|']'
op|'='
name|'value'
newline|'\n'
nl|'\n'
dedent|''
dedent|''
dedent|''
name|'return'
name|'args'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|search_opts_from_filters
dedent|''
name|'def'
name|'search_opts_from_filters'
op|'('
name|'filters'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'return'
op|'{'
name|'f'
op|'['
string|"'name'"
op|']'
op|'.'
name|'replace'
op|'('
string|"'-'"
op|','
string|"'_'"
op|')'
op|':'
name|'f'
op|'['
string|"'value'"
op|']'
op|'['
string|"'1'"
op|']'
nl|'\n'
name|'for'
name|'f'
name|'in'
name|'filters'
name|'if'
name|'f'
op|'['
string|"'value'"
op|']'
op|'['
string|"'1'"
op|']'
op|'}'
name|'if'
name|'filters'
name|'else'
op|'{'
op|'}'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|regex_from_ec2_regex
dedent|''
name|'def'
name|'regex_from_ec2_regex'
op|'('
name|'ec2_re'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Converts an EC2-style regex to a python regex.\n    Approach is based on python fnmatch.\n    """'
newline|'\n'
nl|'\n'
name|'iter_ec2_re'
op|'='
name|'iter'
op|'('
name|'ec2_re'
op|')'
newline|'\n'
nl|'\n'
name|'py_re'
op|'='
string|"''"
newline|'\n'
name|'for'
name|'char'
name|'in'
name|'iter_ec2_re'
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'char'
op|'=='
string|"'*'"
op|':'
newline|'\n'
indent|'            '
name|'py_re'
op|'+='
string|"'.*'"
newline|'\n'
dedent|''
name|'elif'
name|'char'
op|'=='
string|"'?'"
op|':'
newline|'\n'
indent|'            '
name|'py_re'
op|'+='
string|"'.'"
newline|'\n'
dedent|''
name|'elif'
name|'char'
op|'=='
string|"'\\\\'"
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'next_char'
op|'='
name|'iter_ec2_re'
op|'.'
name|'next'
op|'('
op|')'
newline|'\n'
dedent|''
name|'except'
name|'StopIteration'
op|':'
newline|'\n'
indent|'                '
name|'next_char'
op|'='
string|"''"
newline|'\n'
dedent|''
name|'if'
name|'next_char'
op|'=='
string|"'*'"
name|'or'
name|'next_char'
op|'=='
string|"'?'"
op|':'
newline|'\n'
indent|'                '
name|'py_re'
op|'+='
string|"'[%s]'"
op|'%'
name|'next_char'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'                '
name|'py_re'
op|'+='
string|"'\\\\\\\\'"
op|'+'
name|'next_char'
newline|'\n'
dedent|''
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'py_re'
op|'+='
name|'re'
op|'.'
name|'escape'
op|'('
name|'char'
op|')'
newline|'\n'
dedent|''
dedent|''
name|'return'
string|"'\\A%s\\Z(?s)'"
op|'%'
name|'py_re'
newline|'\n'
dedent|''
endmarker|''
end_unit
