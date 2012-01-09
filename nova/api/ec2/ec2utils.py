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
name|'import'
name|'re'
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
name|'import'
name|'network'
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
nl|'\n'
nl|'\n'
DECL|variable|FLAGS
name|'FLAGS'
op|'='
name|'flags'
op|'.'
name|'FLAGS'
newline|'\n'
DECL|variable|LOG
name|'LOG'
op|'='
name|'logging'
op|'.'
name|'getLogger'
op|'('
string|'"nova.api.ec2.ec2utils"'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|image_type
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
string|'"""Convert an ec2 ID (i-[base 16 number]) to an instance id (int)"""'
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
name|'try'
op|':'
newline|'\n'
indent|'        '
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
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
comment|'#TODO(wwolf): once we have ec2_id -> glance_id mapping'
nl|'\n'
comment|'# in place, this wont be necessary'
nl|'\n'
indent|'        '
name|'return'
string|'"ami-00000000"'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ip_info_for_instance_from_nw_info
dedent|''
dedent|''
name|'def'
name|'get_ip_info_for_instance_from_nw_info'
op|'('
name|'nw_info'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'ip_info'
op|'='
name|'dict'
op|'('
name|'fixed_ips'
op|'='
op|'['
op|']'
op|','
name|'fixed_ip6s'
op|'='
op|'['
op|']'
op|','
name|'floating_ips'
op|'='
op|'['
op|']'
op|')'
newline|'\n'
name|'for'
name|'vif'
name|'in'
name|'nw_info'
op|':'
newline|'\n'
indent|'        '
name|'vif_fixed_ips'
op|'='
name|'vif'
op|'.'
name|'fixed_ips'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'fixed_ips'
op|'='
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'vif_fixed_ips'
name|'if'
name|'ip'
op|'['
string|"'version'"
op|']'
op|'=='
number|'4'
op|']'
newline|'\n'
name|'fixed_ip6s'
op|'='
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'vif_fixed_ips'
name|'if'
name|'ip'
op|'['
string|"'version'"
op|']'
op|'=='
number|'6'
op|']'
newline|'\n'
name|'floating_ips'
op|'='
op|'['
name|'ip'
op|'['
string|"'address'"
op|']'
nl|'\n'
name|'for'
name|'ip'
name|'in'
name|'vif'
op|'.'
name|'floating_ips'
op|'('
op|')'
op|']'
newline|'\n'
name|'ip_info'
op|'['
string|"'fixed_ips'"
op|']'
op|'.'
name|'extend'
op|'('
name|'fixed_ips'
op|')'
newline|'\n'
name|'ip_info'
op|'['
string|"'fixed_ip6s'"
op|']'
op|'.'
name|'extend'
op|'('
name|'fixed_ip6s'
op|')'
newline|'\n'
name|'ip_info'
op|'['
string|"'floating_ips'"
op|']'
op|'.'
name|'extend'
op|'('
name|'floating_ips'
op|')'
newline|'\n'
nl|'\n'
dedent|''
name|'return'
name|'ip_info'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_ip_info_for_instance_from_cache
dedent|''
name|'def'
name|'get_ip_info_for_instance_from_cache'
op|'('
name|'instance'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
op|'('
name|'not'
name|'instance'
op|'.'
name|'get'
op|'('
string|"'info_cache'"
op|')'
name|'or'
nl|'\n'
name|'not'
name|'instance'
op|'['
string|"'info_cache'"
op|']'
op|'.'
name|'get'
op|'('
string|"'network_info'"
op|')'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(jkoelker) Raising ValueError so that we trigger the'
nl|'\n'
comment|'#                fallback lookup'
nl|'\n'
indent|'        '
name|'raise'
name|'ValueError'
newline|'\n'
nl|'\n'
dedent|''
name|'cached_info'
op|'='
name|'instance'
op|'['
string|"'info_cache'"
op|']'
op|'['
string|"'network_info'"
op|']'
newline|'\n'
name|'nw_info'
op|'='
name|'network_model'
op|'.'
name|'NetworkInfo'
op|'.'
name|'hydrate'
op|'('
name|'cached_info'
op|')'
newline|'\n'
nl|'\n'
name|'return'
name|'get_ip_info_for_instance_from_nw_info'
op|'('
name|'nw_info'
op|')'
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
string|'"""Return a list of all fixed IPs for an instance"""'
newline|'\n'
nl|'\n'
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'get_ip_info_for_instance_from_cache'
op|'('
name|'instance'
op|')'
newline|'\n'
dedent|''
name|'except'
op|'('
name|'ValueError'
op|','
name|'KeyError'
op|','
name|'AttributeError'
op|')'
op|':'
newline|'\n'
comment|'# NOTE(jkoelker) If the json load (ValueError) or the'
nl|'\n'
comment|'#                sqlalchemy FK (KeyError, AttributeError)'
nl|'\n'
comment|'#                fail fall back to calling out to he'
nl|'\n'
comment|'#                network api'
nl|'\n'
indent|'        '
name|'network_api'
op|'='
name|'network'
op|'.'
name|'API'
op|'('
op|')'
newline|'\n'
nl|'\n'
name|'nw_info'
op|'='
name|'network_api'
op|'.'
name|'get_instance_nw_info'
op|'('
name|'context'
op|','
name|'instance'
op|')'
newline|'\n'
name|'return'
name|'get_ip_info_for_instance_from_nw_info'
op|'('
name|'nw_info'
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|get_availability_zone_by_host
dedent|''
dedent|''
name|'def'
name|'get_availability_zone_by_host'
op|'('
name|'services'
op|','
name|'host'
op|')'
op|':'
newline|'\n'
indent|'    '
name|'if'
name|'len'
op|'('
name|'services'
op|')'
op|'>'
number|'0'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'services'
op|'['
number|'0'
op|']'
op|'['
string|"'availability_zone'"
op|']'
newline|'\n'
dedent|''
name|'return'
string|"'unknown zone'"
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
string|'"""Convert an instance ID (int) to an ec2 ID (i-[base 16 number])"""'
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
DECL|function|id_to_ec2_snap_id
dedent|''
name|'def'
name|'id_to_ec2_snap_id'
op|'('
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert an snapshot ID (int) to an ec2 snapshot ID\n    (snap-[base 16 number])"""'
newline|'\n'
name|'return'
name|'id_to_ec2_id'
op|'('
name|'instance_id'
op|','
string|"'snap-%08x'"
op|')'
newline|'\n'
nl|'\n'
nl|'\n'
DECL|function|id_to_ec2_vol_id
dedent|''
name|'def'
name|'id_to_ec2_vol_id'
op|'('
name|'instance_id'
op|')'
op|':'
newline|'\n'
indent|'    '
string|'"""Convert an volume ID (int) to an ec2 volume ID (vol-[base 16 number])"""'
newline|'\n'
name|'return'
name|'id_to_ec2_id'
op|'('
name|'instance_id'
op|','
string|"'vol-%08x'"
op|')'
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
name|'valueneg'
op|'='
name|'value'
op|'['
number|'1'
op|':'
op|']'
name|'if'
name|'value'
op|'['
number|'0'
op|']'
op|'=='
string|"'-'"
name|'else'
name|'value'
newline|'\n'
name|'if'
name|'valueneg'
op|'=='
string|"'0'"
op|':'
newline|'\n'
indent|'        '
name|'return'
number|'0'
newline|'\n'
dedent|''
name|'if'
name|'valueneg'
op|'=='
string|"''"
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'value'
newline|'\n'
dedent|''
name|'if'
name|'valueneg'
op|'['
number|'0'
op|']'
op|'=='
string|"'0'"
op|':'
newline|'\n'
indent|'        '
name|'if'
name|'valueneg'
op|'['
number|'1'
op|']'
name|'in'
string|"'xX'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'value'
op|','
number|'16'
op|')'
newline|'\n'
dedent|''
name|'elif'
name|'valueneg'
op|'['
number|'1'
op|']'
name|'in'
string|"'bB'"
op|':'
newline|'\n'
indent|'            '
name|'return'
name|'int'
op|'('
name|'value'
op|','
number|'2'
op|')'
newline|'\n'
dedent|''
name|'else'
op|':'
newline|'\n'
indent|'            '
name|'try'
op|':'
newline|'\n'
indent|'                '
name|'return'
name|'int'
op|'('
name|'value'
op|','
number|'8'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
op|':'
newline|'\n'
indent|'                '
name|'pass'
newline|'\n'
dedent|''
dedent|''
dedent|''
name|'try'
op|':'
newline|'\n'
indent|'        '
name|'return'
name|'int'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
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
name|'return'
name|'float'
op|'('
name|'value'
op|')'
newline|'\n'
dedent|''
name|'except'
name|'ValueError'
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
name|'return'
name|'complex'
op|'('
name|'value'
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
dedent|''
endmarker|''
end_unit
